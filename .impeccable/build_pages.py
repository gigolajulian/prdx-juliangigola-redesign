# Builds about/locations/contact from index.html's shell + .impeccable/parts/*.html
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf8")
head, rest = src.split('<main id="main">', 1)
_, foot = rest.split("</main>", 1)

pages = {
    "about": ("About — /Paradox/", "Founded in San Jose in 2015, /Paradox/ is a barber collective led by JR Soriano, Don Gomez, Jeff Phan and Jordan Benigno.", "P. 02 — About", "2011", "img/team-4-1600.webp"),
    "locations": ("Locations — /Paradox/", "Five /Paradox/ shops across the Bay Area: Downtown San Jose, Fremont, Japantown, Midtown and Anomaly.", "P. 03 — Locations", "2015", None),
    "contact": ("Contact — /Paradox/", "Reach out to /Paradox/ with questions or comments about the shops, ĒDUCŌ Academy or PRDX Supply.", "P. 06 — Contact", "2026", None),
}
for name, (title, desc, folio, year, pre) in pages.items():
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head)
    h = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', h)
    h = h.replace('  <link rel="preload" as="image" href="img/nape-1600.webp">\n', f'  <link rel="preload" as="image" href="{pre}">\n' if pre else "")
    h = h.replace("P. 01 — Cover", folio).replace("<span>2015</span></div></div>", f"<span>{year}</span></div></div>")
    h = h.replace('<a href="index.html" aria-current="page">', '<a href="index.html">')
    h = h.replace(f'<a href="{name}.html"><small>', f'<a href="{name}.html" aria-current="page"><small>', 1)
    body = (root / ".impeccable/parts" / f"{name}.html").read_text(encoding="utf8")
    (root / f"{name}.html").write_text(h + '<main id="main">\n' + body + "</main>" + foot, encoding="utf8")
print("built", ", ".join(pages))
