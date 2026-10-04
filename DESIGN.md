---
name: /Paradox/
description: A contemporary barber collective published as a street-culture magazine issue.
colors:
  paper: "#f2f2ee"
  paper-2: "#e7e7e1"
  ink: "#0e0e0e"
  ink-2: "#3a3a37"
  mute: "#6b6b66"
  spot: "#00a3c4"
  spot-ink: "#00405c"
  rule: "rgba(14, 14, 14, 0.18)"
  error: "#b3261e"
typography:
  display:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(4.2rem, 17vw, 17rem)"
    fontWeight: 900
    lineHeight: 0.8
    letterSpacing: "-0.01em"
    fontVariation: "\"wdth\" 62"
  headline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(3rem, 9vw, 8.5rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.01em"
    fontVariation: "\"wdth\" 62"
  title:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 4.2vw, 3.6rem)"
    fontWeight: 900
    lineHeight: 0.88
    fontVariation: "\"wdth\" 62"
  quote:
    fontFamily: "Bodoni Moda, Didot, Georgia, serif"
    fontSize: "clamp(2.2rem, 5.4vw, 5.25rem)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  dek:
    fontFamily: "Bodoni Moda, Didot, Georgia, serif"
    fontSize: "clamp(1.15rem, 1.5vw, 1.4rem)"
    fontWeight: 500
    lineHeight: 1.2
  lede:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.25rem, 1.7vw, 1.5rem)"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "-0.005em"
  body:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
    fontVariation: "\"wdth\" 100"
  label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.03em"
    fontVariation: "\"wdth\" 88"
  mono:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    letterSpacing: "0.02em"
    fontFeature: "\"tnum\" 1"
rounded:
  none: "0"
  pill: "999px"
  disc: "50%"
spacing:
  gutter: "clamp(16px, 2.4vw, 32px)"
  rail: "64px"
  strip: "56px"
  feature: "clamp(64px, 10vw, 140px)"
components:
  button-book:
    backgroundColor: "{colors.spot}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 18px"
    height: "40px"
  button-book-hover:
    backgroundColor: "#1db4d2"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "48px"
  button-ink-hover:
    backgroundColor: "#262624"
  nav-item:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "8px 10px"
  nav-item-hover:
    backgroundColor: "{colors.paper-2}"
  nav-item-current:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  sticker:
    backgroundColor: "{colors.spot}"
    textColor: "{colors.ink}"
    rounded: "{rounded.disc}"
    size: "clamp(112px, 12vw, 168px)"
  plate:
    backgroundColor: "{colors.paper-2}"
    rounded: "{rounded.none}"
  plate-more:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
  plate-more-hover:
    backgroundColor: "{colors.spot}"
    textColor: "{colors.ink}"
  field:
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "10px 0"
---

# Design System: /Paradox/

## Overview

**Creative North Star: "The Issue"**

/Paradox/ is published, not presented. Every page is a spread from one magazine issue: a cover with a masthead and numbered cover lines, features with numbers and deks, a folio rail counting pages and years, captions that do real navigation, a paisley endpaper and a spot-blue back cover. The register is a Japanese street-culture magazine: two inks on cool newsprint, one spot colour, condensed grotesk at shouting scale set against small mono folios.

Density alternates like a printed issue. Display type runs to the edge at extreme size, then gives way to quiet measured columns of body text and generous feature padding. Photographs arrive as ink halftone prints and develop to colour as they enter the viewport; that develop is the system's signature motion. Depth is paper-flat everywhere except one physical card laid over the endpaper.

The world explicitly refuses the dark-luxury barbershop template: no black-and-gold, no centered serif hero with a Book button, no glow.

**Key Characteristics:**
- Two inks (paper, ink) plus one spot (Barbicide blue), used as solid fields and stickers.
- Archivo condensed (wdth 62, weight 900, uppercase) at extreme scale; Bodoni Moda italic for voice; Geist Mono for data only.
- The slash is the only typographic ornament: /Paradox/, /P/, /Downtown/.
- Hairline rules and numbered lists structure every page; no cards, no boxes.
- Photos print in halftone grayscale and develop to colour on entry.

## Colors

Newsprint and ink with a single spot plate, like a two-colour print job.

### Primary
- **Barbicide Blue** (spot): the one spot ink. Solid fields only: the Book button, the sticker discs, the back-cover close band, the "More at prdxsupply.com" tile on hover, drop caps, slashes in display type, focus outlines, selection, labels in the dark contents sheet and colophon. Text on it is always ink.
- **Deep Barbicide** (spot-ink): the spot darkened for small text on paper (pathway numerals, caption-link hover, "new" year in the shop index, form success). Use it wherever spot would be too light to read as text.

### Neutral
- **Newsprint** (paper): the page. Also the rail and the translucent contents strip.
- **Proof Grey** (paper-2): the unprinted plate behind photos before they load, the ground product shots multiply onto in Shop plates, and the nav-pill hover.
- **Press Ink** (ink): text, the 1px rules that open a list or close a header, the dark contents sheet, the colophon, the endpaper ground, the ink button.
- **Second Ink** (ink-2): deks, pathway copy, form labels; text that is secondary but still reading copy.
- **Folio Grey** (mute): folios, captions, cover-line descriptors, rail labels. Small mono only.
- **Hairline** (rule): the 18% ink hairline between list rows and between consecutive features. On ink grounds the hairline flips to paper at 20%.
- **Proof Red** (error): form validation only.

### Named Rules
**The Spot Plate Rule.** Barbicide blue is printed, never emitted: solid fills, discs, slashes and outlines only. No gradients, glows, tints or blue shadows.

**The Two-Ink Rule.** Every surface is paper on ink or ink on paper; the spot is the only third colour. Photographs carry all other colour, and only after they develop.

## Typography

**Display Font:** Archivo variable (with Helvetica Neue, Arial), condensed to wdth 62 at weight 900, uppercase
**Body Font:** Archivo at wdth 100 (UI labels at wdth 88)
**Voice Font:** Bodoni Moda italic (with Didot, Georgia)
**Label/Mono Font:** Geist Mono (with ui-monospace, Menlo), tabular figures

**Character:** One grotesk family stretched between a shouting condensed display and a plain reading width, with a high-contrast Didone italic as the human voice (taglines, deks, pull quotes) and a mono that only ever speaks in numbers, addresses and folios.

### Hierarchy
- **Display** (900, clamp(4.2rem, 17vw, 17rem), 0.8): page openers and the back-cover "Book now" (clamp(3.6rem, 13vw, 13rem)). Runs nearly edge to edge.
- **Headline** (900, clamp(3rem, 9vw, 8.5rem), 0.86): feature heads; shop names on Locations run larger (clamp(3.6rem, 12vw, 11rem)), shop-index names clamp(2.6rem, 8.4vw, 7.5rem) at 0.84.
- **Title** (900, clamp(2rem, 4.2vw, 3.6rem), 0.88): cover lines; small condensed titles in lists (pathway steps, founders, toc, contact aside) at 1.35 to 1.75rem.
- **Quote** (Bodoni italic 500, clamp(2.2rem, 5.4vw, 5.25rem), 1.02): statement spreads and the horizon line; opener stand-firsts at clamp(1.5rem, 2.8vw, 2.5rem).
- **Dek** (Bodoni italic 500, clamp(1.15rem, 1.5vw, 1.4rem), 1.2, ink-2): the line set beside or after a feature headline, right-aligned on desktop.
- **Lede** (500, clamp(1.25rem, 1.7vw, 1.5rem), 1.4): first paragraph of an article, with a spot drop cap.
- **Body** (400, 1.0625rem, 1.55): reading copy, max 68ch.
- **Label** (Archivo wdth 88, 600 to 700, 0.8125 to 0.875rem, 0.02 to 0.03em, uppercase): buttons, nav items, arrow links.
- **Mono** (400 / 600, 0.75rem, 0.02em, uppercase, tabular): folios, captions, numbers, years, addresses, form labels.

### Named Rules
**The Dek Rule.** A headline is introduced by nothing. Context goes in a Bodoni italic dek set beside or after it, never in a small label stacked above it.

**The Data-Only Mono Rule.** Geist Mono sets numbers, years, addresses, folios and captions. It never sets a sentence of prose or a headline.

**The Slash Rule.** The slash, in spot blue inside display type, is the only typographic ornament. In the shop index it rests at hairline grey and prints blue on hover.

## Layout

A 12-column grid (column gap = gutter, clamp(16px, 2.4vw, 32px)) under a fixed 64px folio rail on screens 1024px and wider; the body is padded by the rail width. A 56px sticky contents strip sits on top. Main breakpoint is 900px: below it everything stacks to one column and the nav collapses into a full-screen ink contents sheet; 700px switches the shop index to thumbnail rows; 1024px adds the rail.

Spreads are asymmetric: photo spans 5 to 8 columns, text takes the opposite side, and alternate shops mirror. Photos bleed into the gutter on the cover. Features are separated by clamp(64px, 10vw, 140px) block padding and a hairline (an ink rule after the cover). Reading columns cap at 68ch; stand-firsts at 26ch.

### Named Rules
**The Folio Rule.** Every page opens with a mono folio bar (volume, place, date range) ruled in ink beneath, and the rail on desktop tracks page name, scroll progress and the year of the section in view.

## Elevation & Depth

Flat paper. Depth comes from ink weight (1px ink rules open a list or close a header; 18% hairlines divide rows), from the ink and spot grounds that change the page colour, and from the sticky strip's translucent paper with a light backdrop blur. One object is physical: the card laid on the paisley endpaper, rotated -1.5deg with a soft drop shadow.

### Shadow Vocabulary
- **Laid card** (`box-shadow: 0 30px 60px -20px rgba(0,0,0,.6)`): only for a paper card sitting on the paisley endpaper.

### Named Rules
**The Flat Page Rule.** Nothing on paper casts a shadow. Elevation is reserved for a paper object laid on the endpaper.

## Shapes

Square by default: photos, fields, rules and sections have no radius. Interactive pills (Book, ink button, nav items, menu and close buttons) are fully rounded (999px), and the sticker is a disc. Two things tilt: the sticker (-12deg on the cover, 10deg on the endpaper and the Shop opener, straightening on hover) and the endpaper card (-1.5deg). The paisley bandana is the only pattern, used as the endpaper and as the endband above the colophon.

## Components

### Buttons
- **Shape:** full pill (999px), height 40px in the strip, 48px in body, 52 to 56px in the contents sheet and back cover.
- **Book (primary):** spot ground, ink label, northeast arrow; the booking action, in the strip on every page. Hover lifts to a lighter spot (#1db4d2) and nudges the arrow up-right 2px.
- **Ink:** ink ground, paper label; all other committed actions (Join the waitlist, Shop, Book on spot ground). Hover #262624.
- **Press:** both scale to 0.97 on active, 160ms ease-out.
- **Arrow link:** uppercase label with a 1px underline that wipes out to the right on hover; the companion to a button.

### Navigation
- **Order:** 01 Cover, 02 About, 03 Locations, 04 ĒDUCŌ (external), 05 Shop, 06 Contact; same numbering in the strip and the mobile contents sheet.
- **Contents strip:** logo left, numbered items (mono numeral + wdth 88 label) in pills; hover paper-2, current page ink with the numeral in spot. External items carry a small northeast arrow.
- **Mobile contents:** a full-screen ink sheet revealed top-down by clip-path (560ms), items as numbered condensed display lines staggering up 40ms apart, Book button pinned to the bottom.
- **Folio rail:** vertical page folio, a 1px progress line filling in ink, and a year counter that rolls digits as sections change.

### Cover Lines
Numbered rows under an ink rule: mono numeral, condensed title, right-aligned mono descriptor. Hover slides the title 6px and turns the numeral spot. Each row is a link.

### Print (signature)
Every editorial photograph is a print: shown grayscale at 1.35 contrast with a 4px ink halftone dot screen and a 1.06 scale, then developed to full colour and scale 1 over 1.6s when it enters the viewport. Proof-grey plate behind. Navigational previews (index thumbnails, the hover peek) show the developed image.

### Captions
**The Caption-as-Navigation Rule.** A caption names the place in mono and carries the next step: a right-aligned ink link (Visit Downtown, Get directions) underlined in its own colour, turning deep spot on hover.

### Shop Index
Full-width rows of slashed shop names at headline scale with year and mono meta right-aligned. Hover slides the name 14px, prints the slashes blue, and floats a tilted 300px photo peek at the cursor (pointer devices only). Below 700px rows gain a 72px square thumbnail.

### Product Plate
The Shop (PRDX Supply) unit, in a 2-column grid (4 at 900px+, gap 28px by gutter; the feature set staggers odd plates down 64px). Each plate is one link to the product on prdxsupply.com.
- **Plate:** square, no radius, paper-2 ground; the product shot covers it with `mix-blend-mode: multiply` so its white drops into the proof grey. Product shots are not prints: no halftone develop. Hover scales the image to 1.03 (600ms ease-out); where the device can hover, an alternate shot crossfades in (360ms). On `hover: none` the alternate is not shown at all.
- **Caption:** a 1px ink rule over a two-column grid: the name full width in condensed 900 uppercase (clamp(1.1rem, 1.6vw, 1.5rem), larger in the feature set), then mono "No. 01" in mute at left and the price in mono 600 at right, or a mono uppercase "Sold out" in mute in its place.
- **Sold out:** image grayscale at 0.45 opacity, no alternate shot, name in mute struck through at 2px.
- **More tile:** a plate-sized ink square with a centered condensed "More at prdxsupply.com" and a northeast arrow in paper; hover floods it spot with ink text (240ms). Added only when the last row has an empty cell.
- **Lead plate:** the Shop opener pairs the title with one product as a print (halftone develop, multiplied) beside it, a Sticker labelled Shop overlapping its edge (bottom-left on desktop, top-right on mobile), and a mono "Prices and stock as of [date]. Final at prdxsupply.com." line in mute under the actions.

### Sticker
A spot disc with a slowly rotating mono ring of text (24s per turn) around a condensed two-word label; tilted, straightening and growing 4% on hover. Always a link to the action it names (Book, Shop).

### Booker
Every link to getsquire.com/booking opens a native `<dialog>` instead of a new tab, built by main.js (no markup per page; links stay plain links without JS). It is a paper panel sliding in from the right (min(600px, 100%), full screen on phones) over a 55% ink backdrop: an ink header with the condensed "Book a chair" title and a ringed close, a row of pill shop tabs (the active shop fills spot), Squire's booking flow in an iframe, and a mono footer "Booking by Squire / Open in a new tab". A generic brand link opens a shop chooser first: condensed shop names with addresses, nudging right on hover. Squire's own UI inside the frame cannot be restyled; the frame keeps it on a paper ground.

### Inputs / Fields
- **Style:** underline only: transparent ground, 1px ink bottom border, no radius, 1.125rem text, mono uppercase label above, spot caret.
- **Focus:** the underline turns spot; no outline ring.
- **Error:** border and mono message in proof red; the submit button dims to 50% while sending.

### Endpaper and Endband
The paisley bandana on ink as a full section ground (900px tile) carrying a laid paper card and a sticker, and as a 72 to 120px band (700px tile) closing every page above the ink colophon.

### Scroll Reveals
Below the cover or opener, copy, lists and plates rise 14px and fade in as they enter the page: 700ms ease-out, staggered 70ms per sibling and capped at the sixth. main.js tags the children of feature heads, statements, article bodies, the pathway, shop index, founders, vision, horizon, shop plates, location heads and facts, the contact aside, the endpaper card and the close (plus the contact form). An IntersectionObserver (threshold 0.12, bottom margin -8%) adds `is-in` once. Prints and stickers are never tagged: photographs keep their own ink-to-colour develop, and stickers keep their tilt. Nothing is tagged under reduced motion or without JS.

## Do's and Don'ts

### Do:
- **Do** print every editorial photo through the halftone develop; never show a raw colour photo in a spread.
- **Do** number things: nav items, cover lines, features, pathway steps (I., II., III.), shops (1 of 5).
- **Do** set context in a Bodoni italic dek beside or after the headline.
- **Do** put the next action in the caption when a photo shows a place.
- **Do** keep Book in the strip on every page and one tap away on mobile.
- **Do** write the brand with slashes and spot-blue slashes in display type: /Paradox/, /P/.

### Don't:
- **Don't** use the spot as glow, gradient, tint or shadow.
- **Don't** add a third ink or any colour beyond paper, ink, spot and their listed derivatives.
- **Don't** stack small uppercase labels (kickers, eyebrows) above headlines.
- **Don't** set prose or headlines in Geist Mono.
- **Don't** add shadows or radius to anything on the paper page; pills and discs are for interactive controls only.
- **Don't** build the dark-luxury barbershop hero: black and gold, centered serif, centered Book button.
