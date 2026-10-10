# Space Eagle website

Static public website at **https://spaceeagle.space/**, served from this repository through the existing GitHub Pages setup. `CNAME` and established page addresses are preserved.

## Ecosystem update

- Familiar dark background, editorial headings and Eagle product pages retained.
- Nature intelligence leads the homepage and About; mission and vision explain the purpose in plain language.
- Shared platform palette: Space Eagle blue `#0560a9`, CFMadcon magenta `#a91b60`, deep navy `#081323`.
- High-resolution original Space Eagle artwork, with no repeated wordmark beside it.
- Dedicated Connectivity page after EagleNatureInsight in navigation; former connectivity product pages stay accessible.
- Real, locally packaged photographs with visible credits. See [ASSET_SOURCES.md](ASSET_SOURCES.md).
- EagleNatureInsight's dashboard actions and the historical `dashboard.html` gateway point to **https://natureinsight.spaceeagle.space/**.

## Preview and release

No build or package installation is needed. Serve this directory locally and inspect desktop and mobile layouts. Run `python3 scripts/check_site.py` for local-link, image and release checks.

**Release dependency:** the new platform domain must be live and serving its verified sign-in page before these dashboard links are published to the public site. The release checker supports `--check-platform` to verify the HTTPS endpoint. Keep changes on a review branch while that deployment is pending.

The contact form opens the visitor's email application to prepare a message to `info@spaceeagle.space`; it does not submit data to a web backend.
