// /Paradox/ — page behaviour
const root = document.documentElement;
root.classList.add("js");
const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

addEventListener("load", () => requestAnimationFrame(() => root.classList.add("is-loaded")));
// Don't hold the cover hostage to slow images.
setTimeout(() => root.classList.add("is-loaded"), 1200);

/* Contents (mobile menu) */
const contents = document.querySelector(".contents");
const menuBtn = document.querySelector(".menu-btn");
if (contents && menuBtn) {
  const closeBtn = contents.querySelector(".contents__close");
  const setOpen = (open) => {
    contents.classList.toggle("is-open", open);
    menuBtn.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    (open ? closeBtn : menuBtn).focus();
  };
  menuBtn.addEventListener("click", () => setOpen(true));
  closeBtn.addEventListener("click", () => setOpen(false));
  addEventListener("keydown", (e) => { if (e.key === "Escape" && contents.classList.contains("is-open")) setOpen(false); });
}

/* Photographs print in ink, then develop to colour as they enter the page */
const prints = document.querySelectorAll(".print");
if (reduced || !("IntersectionObserver" in window)) {
  prints.forEach((p) => p.classList.add("is-printed"));
} else {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add("is-printed"); io.unobserve(e.target); }
  }, { threshold: 0.35 });
  prints.forEach((p) => io.observe(p));
}

/* Folio rail: page number, year of the section in view, read progress */
const rail = document.querySelector(".rail");
if (rail) {
  const digits = rail.querySelector(".rail__digits");
  const bar = rail.querySelector(".rail__progress i");
  let current = digits.textContent.trim();

  const setYear = (year) => {
    if (!year || year === current) return;
    const old = digits.querySelector("span");
    const next = document.createElement("span");
    next.textContent = year;
    next.className = "is-in-down";
    digits.append(next);
    requestAnimationFrame(() => requestAnimationFrame(() => next.classList.remove("is-in-down")));
    if (old) { old.classList.add("is-out-up"); setTimeout(() => old.remove(), 560); }
    current = year;
  };

  const sections = document.querySelectorAll("[data-year]");
  const yio = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) setYear(e.target.dataset.year);
  }, { rootMargin: "-45% 0px -50% 0px" });
  sections.forEach((s) => yio.observe(s));

  let ticking = false;
  const progress = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.setProperty("--p", max > 0 ? (scrollY / max).toFixed(4) : 0);
    ticking = false;
  };
  addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(progress); } }, { passive: true });
  progress();
}

/* Shop index: a print of the shop follows the pointer */
const peek = document.querySelector(".peek");
if (peek && matchMedia("(hover: hover) and (min-width: 700px)").matches) {
  const img = peek.querySelector("img");
  let x = 0, y = 0, raf = 0;
  const move = () => {
    peek.style.setProperty("--x", `${x + 28}px`);
    peek.style.setProperty("--y", `${y - peek.offsetHeight / 2}px`);
    raf = 0;
  };
  document.querySelectorAll(".index a[data-peek]").forEach((a) => {
    a.addEventListener("pointerenter", () => { img.src = a.dataset.peek; peek.classList.add("is-on"); });
    a.addEventListener("pointerleave", () => peek.classList.remove("is-on"));
    a.addEventListener("pointermove", (e) => { x = e.clientX; y = e.clientY; if (!raf) raf = requestAnimationFrame(move); });
  });
}

/* Contact form */
const form = document.querySelector(".form");
if (form) {
  const status = form.querySelector(".form__status");
  const btn = form.querySelector("button[type=submit]");
  const check = (el) => {
    const err = el.closest(".field").querySelector(".err");
    let msg = "";
    if (el.validity.valueMissing) msg = "Required.";
    else if (el.validity.typeMismatch) msg = "That email doesn't look right.";
    el.setAttribute("aria-invalid", msg ? "true" : "false");
    if (err) err.textContent = msg;
    return !msg;
  };
  form.querySelectorAll("[required]").forEach((el) => el.addEventListener("blur", () => check(el)));

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const fields = [...form.querySelectorAll("[required]")];
    const ok = fields.map(check).every(Boolean);
    if (!ok) { fields.find((f) => f.getAttribute("aria-invalid") === "true")?.focus(); return; }

    const endpoint = form.dataset.endpoint;
    status.className = "form__status";
    if (!endpoint) {
      status.classList.add("is-err");
      status.textContent = "Messages aren't connected yet. DM @paradoxbarbers on Instagram.";
      return;
    }
    btn.disabled = true;
    status.textContent = "Sending…";
    try {
      const res = await fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(res.status);
      form.reset();
      status.classList.add("is-ok");
      status.textContent = "Sent. We'll get back to you.";
    } catch {
      status.classList.add("is-err");
      status.textContent = "Couldn't send. Try again, or DM @paradoxbarbers on Instagram.";
    } finally {
      btn.disabled = false;
    }
  });
}
