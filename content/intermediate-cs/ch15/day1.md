---
title: "15. Slides"
date: 2017-12-05T10:36:30-06:00
draft: false
type: slide
theme: white
description: "Day 1 Exercises"
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

