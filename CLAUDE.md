# Writing for the DTP Services Berlin work journal

This repo publishes Onur's work journal (Bear Blog) for DTP Services Berlin. Use these rules for every new article.

## What an article is

- One real job or task from Onur's multilingual DTP or PDF accessibility work: what went wrong, how it was found, how it was fixed, what he checks now.
- 450 to 650 words. Short paragraphs, two or three `##` subheadings in sentence case, at most one short bullet list.
- Story feel: open with a few lines of real-life texture (season, Berlin weather, the time of year, the dog, the coffee, how the week felt), then the problem, how it was found, the fix, and what Onur checks now. Light and a bit funny; plain, concrete explanation. Easy to follow for a project manager, still useful for a DTP specialist.
- No invented news events or facts: keep the life texture general and true (seasons, daylight, clocks changing).

## Never

- Client names, end-client names, industries tied to a named client, project codes, file names, exact page or link counts, dates of a specific delivery, languages lists that point to one job, or anything else that could identify a client or job. The blog has an Impressum, so the author is public: client confidentiality is the rule that never bends. Say "a multilingual report", "an agency client", "a few dozen links".
- Internal scripts or tooling details (names, code). Describe the method, not the tool.
- Em dashes. "We", "our team". Emojis.
- Links to competitors (other DTP or remediation providers).

## Always

- First person "I". UK English.
- Load and follow the no-ai-tells skill while writing, then run its scanner and fix every real hit (contrast frames, filler words, uniform rhythm).
- One to three links to relevant dtp-services.de pages (services, resources, free tools), worked into the text.
- One useful outside resource that is not a competitor: W3C/WCAG techniques, PAC, NVDA, Unicode, W3C layout requirements, Adobe documentation.
- Check that every link resolves before publishing.

## File format

`posts/YYYY-MM-DD-slug.md`:

```
---
title: Sentence-case title, no colon if avoidable
slug: short-english-address
date: 2026-11-19T10:00:00+01:00
tags: [pdf-accessibility, indesign]
meta_description: One or two plain sentences for search results.
---
Article text in Markdown (no H1; the title is the H1).
```

Pushing the file to `main` publishes it. Editing it and pushing again updates the same post.

## dtp-services.de pages worth linking

Services: /services-overview/pdf-accessibility, /services-overview/multilingual-dtp, /services-overview/publishing-consulting
Guides: /resources/pdf-accessibility-guide, /resources/pdf-correction-workflow, /resources/how-to-prepare-an-indesign-file-for-translation, /resources/indd-vs-idml-translation, /resources/fonts-in-multilingual-dtp, /resources/right-to-left-languages-indesign, /resources/text-expansion-in-translation, /resources/overset-text-indesign-translation, /resources/indesign-tables-translation-fix, /resources/indesign-preflight-package-translation-print, /resources/how-to-write-alt-text-for-charts, /resources/alt-text-scientific-figures, /resources/dtp-glossary
Free tools: /resources/text-expansion-calculator, /resources/multilingual-dtp-risk-checker, /dtp-project-brief-generator
Samples: /dtp-projects/accessible-pdf-sample, /dtp-projects/multilingual-dtp-sample
Contact: /contact

## Article ideas (queue)

- Why I built the text expansion calculator (/resources/text-expansion-calculator): the planning problem it solves. Ask Onur for the real trigger before writing.
- Why the multilingual DTP risk checker exists (/resources/multilingual-dtp-risk-checker).
- The project brief generator (/dtp-project-brief-generator): the questions that are always missing at the start of a job.
- An RTL flyer for a small nonprofit: choosing a Farsi font and the RTL settings that matter (/resources/right-to-left-languages-indesign). No organisation name.
- Writing alt text for charts and scientific figures (/resources/how-to-write-alt-text-for-charts, /resources/alt-text-scientific-figures).
- Devanagari in accessible PDFs: confirm the exact composer finding with Onur before writing.

## Theme

`theme/theme.css` (colours from dtp-services.de, automatic dark mode) and `theme/fonts.css` (embedded Montserrat Alternates, no outside requests). Pushing either file updates the blog's CSS.
