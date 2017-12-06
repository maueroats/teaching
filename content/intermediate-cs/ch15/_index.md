---
title: "15. Conditionals"
date: 2017-12-05T10:22:50-06:00
draft: false
#type: slide
#theme: white
weight: 150
description: "Making choices in what racket does using 'cond'."
---

See slides for introductory material.

## Assignment 15.A

Read the first three sections of Chapter 15. Do Exercises 15.3.{1,2,4,5,6}. 

Advice:

* 15.3.4: The first input is the candidate for whom you are counting votes. (For example "Clinton".) The next four inputs are votes cast for a person. (For example "Trump" "Clinton" "Sanders" "Trump".) You are supposed to return the number of votes for the candidate from the first input. (For example: `1` in this case.)

* 15.3.7: Keep using `build-image` not `build3-image`. 

Advanced students can do the image making functions 15.3.{3,7-11}.

## Assignment 15.B

Exercises 15.5.{1,2,3,4,5}

## Assignment 15.C

Read 15.6 ("Unnecessary conditionals").

Do Exercises 15.8.{2,3,5}. Exercise 15.5.6.

## Advanced: build-image

The [build-image](http://docs.racket-lang.org/picturing-programs/index.html?q=build-image#%28def._%28%28lib._picturing-programs%2Fprivate%2Fmap-image..rkt%29._build-image%29%29) uses a function that specifies the pixel color to create a rectangular image.

The first example is a function that always returns orange, so it makes an orange square:
```racket
(define (pixel-color x y)
  "orange")
(build-image 300 200 pixel-color)
```
Notice that `pixel-color` does not appear in parentheses. The build-image command needs to activate (run) the `pixel-color` function over and over again, so needs to know the name of the function.

The second example is to give different colors in different circumstances. This example uses a mathematical formula to make a nice picture. Try it.
```racket
(define (pixel-color-ii x y)
  (cond [(<= (abs (- y x)) 30)
         "orange"]
        [else 
         "blue"]))
(build-image 300 200 pixel-color-ii)
```
