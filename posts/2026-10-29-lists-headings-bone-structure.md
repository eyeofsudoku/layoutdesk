---
title: I draw the skeleton before I tag the body
slug: lists-headings-bone-structure
date: 2026-10-29T19:10:00+01:00
tags: [pdf-accessibility, tagging, headings, lists]
meta_description: A simple habit for PDF remediation: map a document's lists and headings before tagging, then compare at the end. Plus three heading rules that catch most outline errors.
---

Lists are sneaky. They look fine on the page, they pass the automatic checks, and then a screen reader announces "list of 3 items" for something that clearly has seven.

I had one of those moments on a recent job, and it changed how I start every remediation.

## The bone structure

Before I tag anything now, I write down the document's skeleton. Every list: where it starts, how it is numbered, which items have sub-lists, and where it really ends. The end point is where most errors hide. A numbered list that runs from the bottom of page 4 to the top of page 5 is one list. A reader on paper sees that instantly; a tagging tool often splits it in half.

The source file helps a lot here. The InDesign file or IDML tells you which paragraphs use list styles and how the numbering runs, which is much more reliable than guessing from the look of the page.

At the end of the job, I compare the tagged lists in the PDF with that skeleton. Same number of lists, same number of items, sub-lists in the right place. If anything differs, the file isn't finished. It takes a few minutes and has caught errors that no checker reported. The W3C technique on [list tags in PDF](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF21) shows the structure that a correct list needs.

## Three heading rules I don't bend

Headings get the same treatment. These three rules catch most outline problems I see:

One H1 per document. If a cover and an inner document are combined into one PDF, the cover title is the H1 and everything inside moves down a level. Two H1s make a screen reader user wonder whether they are in one document or two.

No skipped levels. An H2 followed by an H4 leaves a gap in the outline, and navigation by headings becomes guesswork.

No heading directly followed by a heading of the same level. If an H3 is followed straight away by another H3, with nothing in between, the first one is usually a group heading. The ones after it belong one level lower. This one is easy to miss, because on the page the styles often look identical.

The W3C page on [heading tags in PDF](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF9) covers the basics if you want to read more.

## Why bother

Most people never look at a PDF's tag tree. The people who rely on it can't avoid it. For them, a list split in two or a heading one level too high is the difference between finding the information and giving up.

That's what I mean when I say [PDF accessibility](https://dtp-services.de/services-overview/pdf-accessibility) is more than a green report. If you want to know what else to check, the [PDF accessibility guide](https://dtp-services.de/resources/pdf-accessibility-guide) goes through it step by step, and writing good alt text for charts has [its own page](https://dtp-services.de/resources/how-to-write-alt-text-for-charts).
