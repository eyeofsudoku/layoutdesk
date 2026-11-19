---
title: PAC said pass. NVDA read English in an Arabic voice.
slug: pac-passed-nvda-disagreed
date: 2026-10-08T17:20:00+02:00
tags: [arabic, pdf-accessibility, nvda, pac]
meta_description: A PDF that passed the PAC checker still had the wrong document language. How a screen reader test caught it, and two more Arabic PDF lessons.
---

The first properly grey week of October: rain on the window all day, and the radiator clicking on for the first time since spring. Perfect weather for staring at tag trees.

I like green ticks as much as anyone. PAC, the free PDF/UA checker, had given my file a clean report, and I was about to call it done.

Then I opened the PDF with NVDA, the free screen reader, and it started reading English text with an Arabic voice. It sounded like a robot trying very hard to be polite in the wrong language.

## What was going on

The file came from InDesign with the Middle Eastern feature set, which you need for Arabic layout. On export, that version wrote Arabic (Saudi Arabia) as the main language of the whole document, whatever language the document was actually in.

A checker like PAC tests whether a language is set. It can't tell whether it is the right one. To PAC, "ar-SA" on an English page is a valid language entry, so the report stays green. A screen reader has no such luck. It picks the voice from that entry and reads every word with it.

The fix itself took a minute: set the correct language in Acrobat, on the document and on the passages that really are in another language. The W3C describes both parts clearly, the [document language](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF16) and the [language of a passage](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF19).

Finding it took a listen, and that is the point of this post.

## Two more things Arabic PDFs taught me

Copy and paste lies. If you copy Arabic text out of a PDF to check it, the clipboard can scramble letter order and joining, even when the PDF itself is fine. To check what a screen reader will get, I export the PDF as accessible text and read that instead.

Fonts change under your feet. On one job, a newer release of an Arabic font stored its vowel marks in a different way, and the text in the PDF lost the information a screen reader needs to read those marks. The older release of the same font worked. Nothing in PAC flagged it. Since then I note the exact font version on every Arabic job and only change it on purpose.

## My rule now

Every accessible PDF gets two checks, and they answer different questions:

- PAC tells me whether the structure follows the PDF/UA rules.
- NVDA tells me whether a person can actually use the file.

[PAC](https://pac.axes4.com/) and [NVDA](https://www.nvaccess.org/) are both free, and if you produce accessible PDFs, having both installed is the cheapest quality step there is. I wrote more about why a clean report is only half the story on my [accessible PDF sample page](https://dtp-services.de/dtp-projects/accessible-pdf-sample), and the RTL side of InDesign is covered in [Arabic and Hebrew in InDesign](https://dtp-services.de/resources/right-to-left-languages-indesign).
