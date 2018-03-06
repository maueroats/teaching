---
title: "Count Divisors"
date: 2018-03-06T10:37:37-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

## Warmup

Write a function `count-div`: number(n) number(k) -> number that gives
1 if k divides n and 0 otherwise.

## Warmup Solution

     (define (count-div n k)
        (cond [(= 0 (remainder n k))
                1]
              [else
                0]

## Count-divisors example

     (count-divisors 2) => 1 + 1
     (count-divisors 3) => 1 + 0 + 1
     (count-divisors 4) => 1 + 1 + 0 + 1
     (count-divisors 5) => 1 + 0 + 0 + 0 + 1

Notice that there is _not_ a pattern of repeating previously used results!

## Count-divisors walkthrough

It really looks like I need to keep track of two things: 

* what number we are counting the divisors for (always the same, let's call it `num`)
* the number that we are test dividing (changes, let's call it `current`)

Skeleton:

    (define (count-divisors-help num current)
      ; finish
      0)

Now you write examples. 

