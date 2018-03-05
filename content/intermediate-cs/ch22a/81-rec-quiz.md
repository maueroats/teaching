---
title: "22a. Recursion Quiz"
date: 2018-03-05T07:59:54-06:00
weight: 81
draft: true
#type: slide
#theme: white
description: "First quiz on recursion: reciprocal-squares, blank-vowels, hollow-diagonal."
---

1. `reciprocal-squares`: number(start) number(end) -> number. Find the sum of `1/n^2` for every `n` between `start` and `end` (including both).

|start|end|sum  |
|-----|---|-----|
| 1   | 1 | 1.0 |
| 1   | 2 |1.25 |
| 1   | 3 |1.36111... |

2. `blank-vowels`: string(word) -> string. Change every vowel (a,e,i,o,u) to an underscore (`_`). Example: `(blank-vowels "elephant") => "_l_ph_nt"`.


3. `hollow-diagonal`: number(radius) number(n): Produce `n` circles of the given radius along a diagonal.

    {{< figure src="hollow-diagonal.png" title="(hollow-diagonal 20 5)" >}} 

