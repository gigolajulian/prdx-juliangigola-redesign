# /Paradox/ — redesign concept

A redesign concept for [prdx.us](https://www.prdx.us/) by Julian Gigola. Static HTML/CSS/JS, no build step. Photography, logo and copy belong to /Paradox/.

- `index.html`, `about.html`, `locations.html`, `contact.html`, `styles.css`, `main.js`
- Subpages share the header/footer from `index.html`: edit content in `.impeccable/parts/`, then run `python .impeccable/build_pages.py`.
- Contact form: set `data-endpoint` on the form to a form backend URL to receive messages.
- Design system: `DESIGN.md`.

Run locally: `python -m http.server` and open http://localhost:8000.
