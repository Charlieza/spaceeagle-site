"""Verify static routes/assets and the platform destination before release."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PLATFORM = 'https://natureinsight.spaceeagle.space/'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.links = []
        self.ids = set()
        self.images = []
        self.headings = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
        if tag in ('img', 'script', 'link'):
            src = a.get('src') if tag != 'link' else a.get('href')
            if src:
                self.links.append(src)
        if tag == 'img':
            self.images.append(a)
            for item in a.get('srcset', '').split(','):
                if item.strip():
                    self.links.append(item.strip().split()[0])
        if tag == 'h1':
            self.headings.append(tag)


def check_local():
    pages = {}
    errors = []
    for path in ROOT.glob('*.html'):
        page = Page(path)
        page.feed(path.read_text())
        pages[path.name] = page
        if len(page.headings) != 1:
            errors.append(f'{path.name}: expected one main heading')
        if 'main' not in page.ids:
            errors.append(f'{path.name}: missing main landmark target')
        for img in page.images:
            if not img.get('alt'):
                errors.append(f'{path.name}: missing image description')
    for name, page in pages.items():
        for href in page.links:
            link = urlsplit(href)
            if link.scheme or link.netloc:
                continue
            target = ROOT / unquote(link.path or name)
            if not target.is_file():
                errors.append(f'{name}: missing local destination {href}')
            elif link.fragment and target.suffix == '.html':
                target_page = pages.get(target.name)
                if target_page and link.fragment not in target_page.ids:
                    errors.append(f'{name}: missing section {href}')
    for name in ['eaglenatureinsight.html', 'dashboard.html']:
        if PLATFORM not in pages[name].links:
            errors.append(f'{name}: missing current platform destination')
    source = (ROOT / 'index.html').read_text()
    if any(f'href="{name}.html"' in source for name in ['eaglenet', 'eaglehome', 'eaglevillage']):
        errors.append('index.html: connectivity products should be on Connectivity')
    if (ROOT / 'CNAME').read_text().strip() != 'spaceeagle.space':
        errors.append('CNAME: established website domain changed')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return False
    print(f'PASS: {len(pages)} pages, local routes, section links, image variants and platform destinations.')
    return True


def check_platform():
    try:
        req = urllib.request.Request(PLATFORM, headers={'User-Agent': 'SpaceEagle-release-check/1.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            body = response.read(1_000_000).decode('utf-8')
            final = urlsplit(response.url)
            if response.status != 200 or final.hostname != 'natureinsight.spaceeagle.space':
                raise ValueError('Platform did not serve its custom domain')
            # Branding alone can belong to a parked site; require the prepared app's
            # actual frontend entry point and authentication form as well.
            if 'EagleNatureInsight' not in body or 'app.js' not in body or 'auth' not in body.lower():
                raise ValueError('Platform sign-in page was not verified')
        print('PASS: platform HTTPS destination and sign-in page verified.')
        return True
    except Exception as error:
        print(f'RELEASE PENDING: platform destination is not verified ({type(error).__name__}).', file=sys.stderr)
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check-platform', action='store_true', help='Require the real platform HTTPS sign-in page before publishing.')
    args = parser.parse_args()
    passed = check_local()
    if passed and args.check_platform:
        passed = check_platform()
    raise SystemExit(0 if passed else 1)
