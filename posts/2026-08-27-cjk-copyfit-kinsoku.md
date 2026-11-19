---
title: Counting characters won't fit Japanese into your box
slug: cjk-copyfit-kinsoku
date: 2026-08-27T16:40:00+02:00
tags: [cjk, indesign, multilingual-dtp]
meta_description: Why character counts mislead when fitting Chinese and Japanese text in InDesign, and why a kinsoku table only works once it is actually set.
---

Late August in Berlin. Half the city is on holiday, the U-Bahn suddenly has free seats, and the air in my office stands still by three in the afternoon. A good week for quiet, fiddly work, and I had some: fitting Chinese and Japanese text into a layout that was designed for English. Sidebars, cards, a few tight boxes with fixed heights. The usual brief: same design, every language, nothing spills over.

My first instinct was the one most of us have. English text is 300 characters, the Japanese is 180, so there is plenty of room. Right?

Wrong, and in a slightly funny way.

## Characters are the wrong ruler

A Latin character is narrow. A CJK character sits in a full square, as wide as the type is tall. So 180 Japanese characters can easily take more horizontal space than 300 English ones. The character count tells you how much was said. It tells you almost nothing about how much space it needs.

What I ended up measuring was point size times leading. Each line of CJK text takes the same height, the characters take a predictable width, and from there a box's capacity becomes simple arithmetic. Once I switched to that, the guessing stopped. I could see in advance which boxes would overflow and by how much, and decide per box: reduce the size a step, tighten the leading a little, or ask whether the text can be shortened.

The order mattered too. I fixed the sidebars first, then nudged sizes in small steps, and only then touched the card layouts. Doing it the other way round meant fixing the same box twice.

## The kinsoku table that did nothing

Then came the line breaks. Japanese and Chinese have rules about which characters may not start or end a line. A closing bracket or a small kana at the start of a line looks wrong to a native reader, much like a lonely comma at the start of an English line would.

InDesign handles this with kinsoku tables. Here is the catch I ran into: the paragraph styles in the file had no kinsoku table assigned at all. The setting was simply empty. So InDesign broke lines wherever it liked, and some lines started with exactly the characters that should never start one.

The software worked as designed: an empty setting has nothing to apply. After I assigned the right table to every CJK paragraph style, the bad breaks disappeared in one go.

If you want to see what the rules actually are, the W3C has a very readable document on it: [Requirements for Japanese Text Layout](https://www.w3.org/TR/jlreq/). It is long, but the sections on line breaking explain more in ten minutes than any forum thread.

## What I check now on every CJK job

- Box capacity from point size and leading, never from character counts.
- A kinsoku table assigned in every paragraph style that holds CJK text.
- The right InDesign setup. Some CJK features only show up when InDesign runs with the Asian feature set, so I check that before I start.

Expansion and contraction between languages is a planning question long before it is a layout one. If you are estimating space for a new language, the [text expansion calculator](https://dtp-services.de/resources/text-expansion-calculator) gives a quick first idea, and the [multilingual DTP service page](https://dtp-services.de/services-overview/multilingual-dtp) shows how I handle jobs like this from start to finish.
