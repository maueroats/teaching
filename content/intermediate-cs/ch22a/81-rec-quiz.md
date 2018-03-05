---
title: "22a. Recursion Quiz"
date: 2018-03-05T07:59:54-06:00
weight: 81
draft: false
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


## Period 1 Only

3. `hollow-diagonal`: number(radius) number(n): Produce `n` circles of the given radius along a diagonal.

    {{< figure src="hollow-diagonal.png" title="(hollow-diagonal 20 5)" >}} 


## Period 5 Only

4. `circle-circle`: number(big-radius) number(little-radius) number(turn-angle) number(n) -> image. Produce `n` circles of size `little-radius` around the perimeter of a circle of size `big-radius`. In between each, have a central angle of `turn-angle`.

    {{< figure src="circle-circle.png" title="(circle-circle 100 20 45 8)" >}}
    
    
