---
title: "Number Models 3"
date: 2017-10-30T09:59:11-05:00
draft: false
#type: slide
#theme: white
---

## Repetition (without conditionals)

What does this tick-hander do? Write checks for the results when num=0, num=1, and num=4.
```racket
(define (repeat-it num)
    (remainder (+ num 1) 5))
```

## Class practice

1a. Make a shape of your choice start at x=100, y=40, then move to x=100,y=110, then to x=100,y=180, then back to x=100, y=40. The motion should happen every second.

1b. Hit a key to make the shape go to a random one of those three locations.

## Homework

Add one colored circle at a random location on the screen every half second.


