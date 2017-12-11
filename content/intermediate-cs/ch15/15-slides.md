---
title: "15. Slides"
date: 2017-12-08T11:52:39-06:00
draft: false
type: slide
theme: white
description: "Day 1 Exercises"
weight: 10
---

# Mystery Function

```racket
(define (scrunch x)
   (cond [(< x 10)       0]
         [else     (/ x 2)]))
```
Give 3 examples what it does.

---

# Scrunch Sum

* Scrunch three numbers
* Add the result

```racket
(scrunch-three 5 12 40) => 26
```
---

# Word Points

* Each word gets 2 points per letter. 
* Every word earns at least 7 points. 
* Find the total points earned by four words.

```racket
(sum-points "saw" "it" "workhorse" "betadyne") => 48
```
---

## Early Wake-Up

Count the number of people who wake up before `cutoff-time`.

```racket
(early-wake-up cutoff-time 
               person-1-time
               person-2-time
               person-3-time)
 ```
 
 
