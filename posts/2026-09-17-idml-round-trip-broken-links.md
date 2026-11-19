---
title: The translation round trip ate my hyperlinks
slug: idml-round-trip-broken-links
date: 2026-09-17T18:05:00+02:00
tags: [indesign, idml, translation, pdf-accessibility]
meta_description: An IDML round trip through a translation tool damaged the same hyperlinks in every language. What went wrong, how I found it, and the check I now run before any PDF work.
---

Some bugs are polite enough to appear once. This one showed up in every language, in the same places, every single time.

The job was a multilingual document: InDesign source, text sent out for translation as IDML, translated IDML back, then accessible PDFs for each language. A very normal pipeline. The links in the English file were fine. In the translated files they were not.

## What I found

When I counted, the damage fell into three groups, and the numbers were identical per language:

- 20 links pointed to the wrong target.
- 12 link addresses were encoded twice, so a space that should read `%20` came back as `%2520` and the link went nowhere.
- 102 links that were meant to be hidden (their frames invisible in the PDF) came back visible.

On top of that, eight links per language arrived with no destination at all. They looked like links in InDesign and did nothing in the PDF.

The pattern was the giveaway. Random human mistakes don’t repeat with the same count in every language. Something in the round trip itself was doing this, every time, in the same way. In this case the translation tool's IDML filter had trouble with a particular way the links were nested in the file.

## How I fixed it

I didn't fix it link by link. With that many links and that many languages, manual fixing is how you introduce new errors while removing old ones.

Because IDML is a zipped bundle of XML files, the links can be read and repaired at that level. I compared each translated IDML against the source, put the correct targets back, undid the double encoding and restored the hidden flags. The links with no destination got their targets back inside InDesign before export.

After that, the only file I opened was the repaired one. The raw return from the translation tool stayed closed, even for a quick look. That habit alone saved me from mixing up versions twice.

## The gate I added

The real lesson was about timing. A broken link costs almost nothing to fix in InDesign. In a finished accessible PDF it costs a lot, because links are part of the tag structure, and the fix means another remediation pass.

So link checking is now a gate in my process. Before any Acrobat work starts, every link in every language is counted and compared with the source. If the numbers don't match, nothing moves on. Screen reader users rely on links that say where they go and actually go there, and the W3C technique on [links in PDF documents](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF11) is worth a read if you want the details of how a proper PDF link is built.

If you are sending InDesign files out for translation, two pages on my site cover the groundwork: [IDML vs INDD for translation](https://dtp-services.de/resources/indd-vs-idml-translation) and [how to prepare an InDesign file for translation](https://dtp-services.de/resources/how-to-prepare-an-indesign-file-for-translation). And if the PDFs at the end need to be accessible, that's [the part I do every day](https://dtp-services.de/services-overview/pdf-accessibility).
