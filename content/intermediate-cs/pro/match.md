---
title: "Match"
date: 2018-02-21T15:01:29-06:00
weight: 30
draft: false
#type: slide
#theme: white
---

Pattern matching lets you take apart structures into their component
variables in a simple way. 

You can use `(require racket/match)` to activate [pattern matching](https://docs.racket-lang.org/guide/match.html?q=pattern%20match).

## Matching

The `match` function is like `cond` except it checks to see if a value
matches a certain "literal" pattern or question. It can create
variables to use immediately instead of requiring a helper function.

### Problem

Write a function that takes in a number or a posn and returns the
distance to the correct origin (either 0 or (0,0)) depending on which
type it gets.

### Example Solution: Cond 

    (define (cond-to-zero w)
      (cond [(posn? w)    (sqrt (+ (sqr (posn-x w))
                                   (sqr (posn-y w))))]
            [(number? w)  (abs w)]))

### Example Solution: Match

    (define (match-to-zero w)
      (match n
        [(posn x y)  (sqrt (+ (sqr x)
                              (sqr y)))]
        [number?     (abs w)]))


Notice how 

## Ignoring parts of a model

You can use the underscore `_` to match places that you want to
ignore. This example shows how to pull out two scores from a model and
use them to find the total number of points in the game.

    (define-struct game (p1pos p1score p2pos p2score))
    (define (total-score model)
      (match model
        [(game _ s1 _ s2)
         (+ s1 s2)]
