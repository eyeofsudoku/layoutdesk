---
title: Setting a script I can't read
slug: farsi-flyer-script-i-cant-read
date: 2026-11-23T14:00:00+01:00
tags: [rtl, farsi, indesign, fonts, multilingual-dtp]
meta_description: A Farsi flyer whose letters fell apart in InDesign. Why the cause was the font, what happened to the phone number, and how I check right-to-left text in a language I don't speak.
---

Late November. The leaves are gone, the light goes before five, and the dog has started to look at the rain with real suspicion before every walk.

A small nonprofit sent me a folded flyer in Farsi. The German version was finished and printed. The Farsi one had been translated, pasted into the same InDesign layout, and then everything went wrong. Letters that should join stood apart. Some lines seemed to run backwards. Someone had tried to fix it by hand, with extra spaces, tabs and line breaks pushed into the text until it looked roughly right on one screen.

I don't read Farsi. I can recognise the script and I know how it should behave. That turned out to be enough to find the problem, and a good reason to be careful about everything after it.

## The direction was fine

When Persian or Arabic text breaks in InDesign, people usually blame the direction settings first. So I checked those first. Paragraph direction: right to left. Composer: the World-Ready one, which is the composer that can join Arabic-script letters. Both were already correct.

The real cause was the font. The layout used a Latin typeface for everything, and that typeface has no Arabic-script letters at all. InDesign filled the gaps from somewhere else, and the shaping fell apart. On top of that, the pasted text carried invisible direction marks from wherever it had been copied, so even a font swap alone would have left some lines in odd places.

The fix had three parts. A proper Persian font on every Farsi run, chosen after looking at the German original so both versions still feel like one family. Out with the hidden direction marks and the manual spacing hacks. Then new line breaks, set by the composer instead of by hand.

For the font I picked a free one whose Latin letters are based on the same design the German layout uses. Mixed lines with an email address or a web link inside Farsi text now look like they belong together.

## The phone number that turned around

One small thing nearly slipped through. Inside right-to-left text, a phone number written in groups can come out with its groups in reverse order. Every digit is correct, the number is still wrong. Non-breaking spaces between the groups did not stop it.

What worked was giving the contact lines (phone, email, social handles) their own left-to-right paragraph. A social handle on its own also needed a tiny invisible left-to-right mark, or the @ jumped to the wrong end.

## How I check a language I can't read

I can't proofread Farsi, and I say so to the client. What I can do:

- compare the shape of every line against the source text, not against the exported PDF (searching Persian in a PDF turns the half-spaces inside some words into normal spaces, so the PDF can't prove that anything is missing)
- flag anything that looks off as a pointer, by its position on the page, and let a Farsi reader decide
- check numbers, addresses and links character by character, since those don't need the language

A few of my pointers turned out to be real typos, which the client confirmed before the print file went out. The ones that were fine cost nobody more than a minute.

If you have a right-to-left version coming up, my [guide to right-to-left languages in InDesign](https://dtp-services.de/resources/right-to-left-languages-indesign) covers the settings, and [fonts in multilingual DTP](https://dtp-services.de/resources/fonts-in-multilingual-dtp) explains why the font is the first thing to check. For the detail behind Persian and Arabic line layout, the W3C's [Arabic and Persian layout requirements](https://www.w3.org/TR/alreq/) are worth an evening.
