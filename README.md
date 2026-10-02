# Anthony Obinugwu — Portfolio

Personal developer portfolio of **Anthony Chinedu Obinugwu** — Backend Developer based in Lagos, Nigeria; COO & Co-Founder of Trix Mart.

A single-page site with a tech-green and black theme, animated particle background, typewriter hero, and four views: Home, About, Projects, and Resume/CV.

## Tech
- Static HTML, CSS, and vanilla JavaScript
- Zero-dependency Node.js HTTP server (`server.js`)
- Pages are generated from `generate_html.py`; SVG assets from `generate_assets.py`

## Project structure
```
index.html              # Home (SPA entry)
about/ project/ resume/ # Direct routes for each view
assets/css/style.css    # Theme styles
assets/js/main.js       # Particles, typewriter, SPA router
assets/images/          # Logo, hero, about card, project thumbnails
generate_html.py        # Source of truth for all 4 HTML pages
generate_assets.py      # Source of truth for SVG assets
server.js               # Local static server
```

## Run locally
```bash
node server.js
# then open http://localhost:3000
```

## Regenerate pages
```bash
python3 generate_html.py
```

## Links
- GitHub: https://github.com/Anthony-Obinugwu
- LinkedIn: https://linkedin.com/in/anthony-obinugwu-03ba23199
- X: https://x.com/1xnedu
