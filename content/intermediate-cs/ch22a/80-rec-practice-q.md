---
title: "22a. Recursion Quiz Practice"
date: 2018-03-02T08:00:42-06:00
weight: 80
draft: false
#type: slide
#theme: white
---

Use `define/contract` for each function.

1. `hawaiian-earring`: number(stage) number(radius) -> image. Create `stage` circles with each successive circle 80% of the radius of the previous one.

    {{< figure src="hawaiian-earring.png" 
               caption="(hawaiian-earring 10 100)" 
               >}}


2. `double-ss`: string -> string. Double each `s` appearing in the string.

        (check-expect (slash-vowels "The snake was silent.") 
                      "The ssnake wass ssilent.")

3. `math-mess`: number(start) number(end) -> number. Add the square of every even number, subtract the square root of every odd number.

        (math-mess 10 10) => (* 10 10)
        (math-mess 11 11) => (- (sqrt 11))
        (math-mess 10 11) => (- (* 10 10) (sqrt 11))


