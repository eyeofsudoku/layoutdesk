# Writing for the DTP Services Berlin work journal

This repo publishes Layout Desk (layoutdesk.bearblog.dev), Onur's work journal for DTP Services Berlin. Use these rules for every new article.

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

Suggested order: 1, then 3. Always ask Onur for the facts marked "needs" before writing; never guess technical details in public.

1. **Why I built a text expansion calculator** → /resources/text-expansion-calculator. Needs: the real trigger from Onur (two or three sentences).
2. ~~**Setting a script I can't read**~~ (published 2026-11-23): the Farsi flyer for a small nonprofit (Nov 2026): choosing a font and checking RTL text in a language Onur doesn't speak. → /resources/right-to-left-languages-indesign, /resources/fonts-in-multilingual-dtp. No organisation name.
3. **It looks right, it copies as gibberish**: Hindi/Gujarati InDesign files whose PDF text breaks when copied or read aloud; the free file check before quoting. → /services-overview/multilingual-dtp, /resources/fonts-in-multilingual-dtp, Unicode. Needs: the exact cause and fix from Onur.
4. **Eleven languages, one small flyer**: what a short multilingual flyer involves (scripts, fonts, length, direction). No client, no language list. → /resources/multilingual-dtp-risk-checker, /resources/text-expansion-in-translation.
5. **A template is only half a template**: an accessible Word template needs an author guide and a final check. → /services-overview/pdf-accessibility, /resources/process-guides.
6. **Some files never leave my desk**: confidential client files stay on Onur's own computer; the principle only, no tool names. → /about, /contact.
7. **Who writes the alt text?**: photos in production, charts by someone who knows the data. → /resources/how-to-write-alt-text-for-charts, /resources/alt-text-scientific-figures.
8. **The same-day fix**: a small Arabic mark problem in a PDF fixed in an afternoon; small jobs still get the full check. → /dtp-projects/accessible-pdf-sample, PAC. Needs: the exact cause and fix from Onur.
9. Devanagari in accessible PDFs (composer finding): needs Onur's confirmation before writing; publishing a wrong rule could harm readers' files.

## Published

| Date | Slug | Topic |
|---|---|---|
| 2026-08-27 | cjk-copyfit-kinsoku | CJK copyfit by point size × leading; empty kinsoku tables |
| 2026-09-17 | idml-round-trip-broken-links | IDML round trip through a CAT tool damaging links; link gate before Acrobat |
| 2026-10-08 | pac-passed-nvda-disagreed | InDesign ME writing ar-SA as document language; PAC vs NVDA; Arabic copy/paste and font version |
| 2026-10-29 | lists-headings-bone-structure | List "bone structure" check; one H1, no skipped levels, same-level heading rule |
| 2026-11-13 | dont-edit-accessible-pdf | Why not to edit a remediated PDF; draft-PDF-first correction workflow |
| 2026-11-23 | farsi-flyer-script-i-cant-read | Farsi flyer: missing Arabic-script glyphs in the font, pasted bidi marks, reversed phone groups, checking RTL text without reading it |

Keep this table updated when a post goes live. New posts are dated on the day they are written (backdating was only for the first five).

## How publishing works

- Blog: https://layoutdesk.bearblog.dev (Bear Blog, upgraded). Repo: github.com/eyeofsudoku/layoutdesk.
- `publish.py` talks to the Bear API (`https://bearblog.dev/layoutdesk/api/v1/`). The key is the repo secret `BEAR_API_KEY`; it never goes into chat or files.
- `.github/workflows/publish.yml` runs on every push to `main` that touches `posts/*.md`, `blog.json` or `theme/*.css`: it applies blog settings + theme, then creates or updates posts. `posts/published.json` (written by the workflow) maps slug → Bear uid so edits update instead of duplicating. Manual run: Actions → Publish journal → Run workflow (posts or blog).
- Posts are `publish: true`, `discoverable: true` (Bear Discover feed) and `lang: en` by default; a header line `publish: false` keeps a post as a draft.
- Bear's Cloudflare blocks Python's default User-Agent (error 1010); `publish.py` sends its own.
- Checking from a Claude session: the shell can reach `https://layoutdesk.bearblog.dev` and the public GitHub API (`api.github.com/repos/eyeofsudoku/layoutdesk/actions/runs`) to confirm a run and the live page. Pushing: attach the repo with add_repo (push access), clone, commit, `git -c push.negotiate=true push`.

## Blog setup decisions

- Name "Layout Desk", English, first person "I", UK English. Navigation: Home · Journal · Impressum & privacy (link to dtp-services.de/impressum; a business-linked blog needs an Impressum under § 5 DDG, so the author is public and client confidentiality is absolute).
- Home page text is in `blog.json` (with `{{ posts }}` for the list).

## Theme

`theme/theme.css` (colours from dtp-services.de, automatic dark mode) and `theme/fonts.css` (embedded Montserrat Alternates, no outside requests). Pushing either file updates the blog's CSS.
