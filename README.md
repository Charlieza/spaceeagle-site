# SpaceEagle — Redesign (May 2026)

This is a full visual redesign of spaceeagle.space. **All copy and information has been preserved.** The internal link structure (filenames) is unchanged so any external links continue to work.

## What changed

- **New design system** (`styles.css`) — dark cosmic theme, editorial serif display type (Instrument Serif), modern sans body (Geist), aurora gradient accents, glassmorphic header, animated star-field, refined micro-typography.
- **New homepage** (`index.html`) — replaces the generic card grid with a hero featuring an animated orbital SVG, stat strip, featured EagleNatureInsight card, "Why us" feature band, and a CTA strip.
- **All 11 product pages** rebuilt to the new template with unique headlines/ledes per product, custom icons, and a consistent CTA pattern. Information from the originals is preserved.
- **About / Contact / EagleNatureInsight / Dashboard** all rebuilt to match. Contact form is upgraded with an organisation field and proper styling. Dashboard preserves the Streamlit link and Earth Engine iframe.
- **Footer** is now a proper 4-column site footer with brand block, products, solutions, and company links.

## Assets to keep from your existing repo

Drop these files in alongside the new HTML/CSS (or they'll fall back gracefully):

- `img-eaglenatureinsight.png` — used on the EagleNatureInsight page hero
- Any `img-eagle*.svg` files — original product icons (the new homepage uses inline SVG icons instead, but pages still reference some). Safe to keep them or remove; not required.
- `img-space-*.svg` — referenced by the old About / Eagle product pages. The new pages no longer use them, so they can be deleted.

## New / replaced assets

- `spaceeagle-logo.svg` — **a new placeholder logo has been generated.** If you have your existing branded logo, replace this file with your original (keep the same filename).
- `styles.css` — completely replaced.
- All HTML files — completely replaced (content preserved).
- `CNAME` — preserved unchanged (`spaceeagle.space`).

## Typography

The site loads Instrument Serif + Geist from Google Fonts. No build step required — just serve the static files.

## Deployment

This is a static site. Deploy as-is to GitHub Pages, Netlify, Vercel, or any static host. The `CNAME` file is set up for your existing GitHub Pages custom domain.
