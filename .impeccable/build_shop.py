# Builds .impeccable/parts/shop.html from a PRDX Supply (Shopify) products.json snapshot.
# Refresh: curl -sL "https://www.prdxsupply.com/products.json?limit=250" -o .impeccable/supply-products.json
#          python .impeccable/build_shop.py && python .impeccable/build_pages.py
import datetime, html, json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
STORE = "https://www.prdxsupply.com"
LEAD = "rila-x-paradox-airbrushed-barbedwire-cap"
snap = root / ".impeccable/supply-products.json"
products = [p for p in json.loads(snap.read_text(encoding="utf8"))["products"] if p["images"]]
d = datetime.date.fromtimestamp(snap.stat().st_mtime); as_of = f"{d:%b} {d.day}, {d.year}"

ARROW = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 9l6-6M4 3h5v5"/></svg>'
NEWTAB = '<span class="sr">(opens prdxsupply.com)</span>'


def img(src, w):
    return f"{src}{'&' if '?' in src else '?'}width={w}"


def srcset(src):
    return f'src="{img(src, 800)}" srcset="{img(src, 400)} 400w, {img(src, 800)} 800w" sizes="(min-width: 900px) 22vw, 46vw"'


def price(p):
    return f"${min(float(v['price']) for v in p['variants']):,.0f}"


def sold(p):
    return not any(v["available"] for v in p["variants"])


def item(p, n):
    title = html.escape(p["title"])
    a = p["images"][0]["src"]
    b = p["images"][1]["src"] if len(p["images"]) > 1 and not sold(p) else None
    second = f'<img class="plate__alt" {srcset(b)} alt="" loading="lazy" width="800" height="800">' if b else ""
    state = '<span class="plate__state">Sold out</span>' if sold(p) else f'<span class="plate__price">{price(p)}</span>'
    return f'''      <li class="plate{' is-sold' if sold(p) else ''}">
        <a href="{STORE}/products/{p['handle']}" target="_blank" rel="noopener">
          <span class="plate__img"><img {srcset(a)} alt="" loading="lazy" width="800" height="800">{second}</span>
          <span class="plate__cap"><span class="plate__name">{title}</span><span class="plate__no">No. {n:02d}</span>{state}</span>{NEWTAB}
        </a>
      </li>'''


rila = [p for p in products if p["handle"].startswith("rila-x-paradox")]
rest = [p for p in products if p not in rila]
numbered = rila + rest
lead = next(p for p in products if p["handle"] == LEAD)
lead_no = numbered.index(lead) + 1

rila_items = [item(p, i + 1) for i, p in enumerate(rila)]
rest_items = [item(p, len(rila) + i + 1) for i, p in enumerate(rest)]
spare = (-len(rest)) % 4
more = f'''      <li class="plate plate--more"><a href="{STORE}/" target="_blank" rel="noopener"><span class="plate__img"><span class="plate__more">More at<br>prdxsupply.com{ARROW}</span></span>{NEWTAB}</a></li>''' if spare else ""

body = f'''  <section class="opener opener--short wrap" data-year="2026" aria-labelledby="shop-title">
    <div class="folio-bar mono"><span>Vol. 11 — Est. 2015</span><span>PRDX Supply</span><span>{len(products)} pieces</span></div>
    <div class="shop-open">
      <div>
        <h1 class="display opener__title" id="shop-title">Clothes by <span class="slash">/</span>P<span class="slash">/</span></h1>
        <p class="opener__stand">PRDX Supply, the clothing line of /Paradox/. Every piece links straight to the store.</p>
        <div class="shop__actions"><a class="btn-ink" href="{STORE}/" target="_blank" rel="noopener">Shop all at prdxsupply.com{ARROW}</a></div>
        <p class="mono shop-asof">Prices and stock as of {as_of}. Final at prdxsupply.com.</p>
      </div>
      <figure class="print shop-lead">
        <a href="{STORE}/products/{lead['handle']}" target="_blank" rel="noopener" class="print__img shop-lead__img"><img src="{img(lead['images'][0]['src'], 1200)}" alt="{html.escape(lead['title'])}" width="1200" height="1200" fetchpriority="high"></a>
        <figcaption><span>No. {lead_no:02d} — {html.escape(lead['title'])} — {price(lead)}</span><a href="{STORE}/products/{lead['handle']}" target="_blank" rel="noopener">View piece{ARROW}</a></figcaption>
        <a class="sticker" href="{STORE}/" target="_blank" rel="noopener" aria-label="Shop all at prdxsupply.com">
          <svg class="ring" viewBox="0 0 100 100" aria-hidden="true">
            <defs><path id="ring-shop-page" d="M50,50 m-40,0 a40,40 0 1,1 80,0 a40,40 0 1,1 -80,0"/></defs>
            <text><textPath href="#ring-shop-page">prdxsupply.com · prdxsupply.com · prdxsupply.com · </textPath></text>
          </svg>
          <b>Shop</b>
        </a>
      </figure>
    </div>
  </section>

  <section class="feature wrap" data-year="2026" aria-labelledby="rila-title">
    <header class="feature__head">
      <h2 class="display" id="rila-title">Rila × <span class="slash">/</span>Paradox<span class="slash">/</span></h2>
      <p class="dek">Four caps, one collaboration.</p>
    </header>
    <ul class="plates plates--feature">
{chr(10).join(rila_items)}
    </ul>
  </section>

  <section class="feature wrap" data-year="2026" aria-labelledby="line-title">
    <header class="feature__head">
      <h2 class="display" id="line-title">The line</h2>
      <p class="dek">Caps, knits, shirts, shorts and the chrome /P/ cape.</p>
    </header>
    <ul class="plates">
{chr(10).join(rest_items)}
{more}
    </ul>
  </section>
'''
(root / ".impeccable/parts/shop.html").write_text(body, encoding="utf8")
print(f"shop: {len(rila)} collab + {len(rest)} line items, as of {as_of}")
