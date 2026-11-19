# Writing for the DTP Services Berlin work journal

This repo publishes Onur's work journal (Bear Blog) for DTP Services Berlin. Use these rules for every new article.

## What an article is

- One real job or task from Onur's multilingual DTP or PDF accessibility work: what went wrong, how it was found, how it was fixed, what he checks now.
- 450 to 650 words. Short paragraphs, two or three `##` subheadings in sentence case, at most one short bullet list.
- A light, slightly funny opening line or two, then plain, concrete explanation. Easy to follow for a project manager, still useful for a DTP specialist.

## Never

- Client names, end-client names, project codes, file names, page counts or anything else that could identify a client or job. Say "a multilingual report", "an insurance document", "an agency client".
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
