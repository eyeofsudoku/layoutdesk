---
title: Please don't touch the finished accessible PDF
slug: dont-edit-accessible-pdf
date: 2026-11-13T15:30:00+01:00
tags: [pdf-accessibility, workflow, corrections]
meta_description: Why small edits to a remediated PDF can break its accessibility, and the correction workflow that saves everyone from paying for remediation twice.
---

The email came a few days after delivery. Friendly, short, and very reasonable: a number on the cover was wrong. Could someone just change it in the PDF?

Someone could. It's a two-minute edit in Acrobat. And that's exactly why I asked them not to.

## Why a tiny edit is not tiny

An accessible PDF has two layers. There is what you see on the page, and there is the tag structure underneath that tells a screen reader what each piece is: this is a heading, this is a list, this is the reading order, this image means this.

When you edit text directly in Acrobat, you change the visible layer. The tags underneath don't always follow. Sometimes the new text ends up untagged. Sometimes it lands in the wrong place in the reading order. Sometimes the edit looks perfect and the screen reader still reads the old number. None of this shows on screen, so nobody notices until a user does.

So I made the correction myself, in the source, exported again, ran the checks again and sent new files with fresh PAC reports. It cost me a little time. It saved the client a file that looked fixed and wasn't.

## The pattern behind it

This wasn't a one-off. On a bigger multilingual job earlier this autumn, a round of language corrections arrived after the accessible PDFs were already delivered. Every one of those corrections meant a new export and a new remediation pass, per language.

Nobody did anything wrong. The order of steps was the problem: wording was still changing after the accessibility work was finished.

## What I suggest now

Before anything goes into final layout and remediation, I send a plain draft PDF: the text in reading order, without the final layout or tags. The client reads it, corrects it and says "final". Then the real work starts.

That one extra step moves all the cheap corrections to the moment when they are cheap. Changing a word in a draft costs nothing. Changing it in a remediated PDF costs a remediation pass.

And when a correction does come later, which happens, the rule is simple. Fixes go into the source file, never into the accessible PDF, and the PDF is rebuilt and checked again.

I wrote the full process up as a guide: [the PDF correction workflow](https://dtp-services.de/resources/pdf-correction-workflow). If you're planning a document that has to be accessible in the end, the [PDF accessibility guide](https://dtp-services.de/resources/pdf-accessibility-guide) explains what makes a file accessible in the first place, and the [project brief generator](https://dtp-services.de/dtp-project-brief-generator) helps you collect the details before the first file changes hands.
