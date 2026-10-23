# Favour Ogazi Website

Personal website and portfolio for Favour Ogazi.

- `public/`: the live site files Cloudflare serves
- `site-src/`: the source. Edit content in `site-src/build.py` and styles in `site-src/assets/`, then run `python3 site-src/build.py` to regenerate `public/`
- `wrangler.jsonc`: Cloudflare settings that point to `public/`
- Photos: drop them in `public/assets/img/` using the names in `README.txt` there

Every push to `main` deploys automatically through Cloudflare.
