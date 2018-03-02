---
title: "22a. Recursive Helpers"
date: 2018-02-28T13:58:50-06:00
weight: 70
draft: false
#type: slide
#theme: white
description: "Exercises involving recursive functions with helper functions."
---

## Image Theory

1. `big-bullseye`: number(n) -> image. Draw n concentric circles, alternating color beginning with black on the inside. Begin with a radius of 10 and increase the radius by 10 each successive circle.

2. `sier-triangle`: number(n) number(size) -> image. Make a [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_gasket) with `n` stages in the pattern and a side length of `size`. Do this by dividing the size in two when you make a smaller triangle, and arrange those triangles themselves in a triangle (see images).

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Sierpinski_triangle_evolution.svg/320px-Sierpinski_triangle_evolution.svg.png" >}}

## Number Theory

2. `count-divisors`: positive-integer(n) -> positive-integer. Count how many integers 1,2,...,n divide the number `n`.

3. `is-prime?`: positive-integer(n) -> boolean. Determine whether or not `n` is prime. Note: this can do less checking than the previous function.

4. `smallest-factor`: positive-integer(n) -> positive-integer. Find the smallest integer divisor of `n`. 

5. `smallest-prime-factor`: positive-integer(n) -> positive-integer. Find the smallest prime factor of `n`.

