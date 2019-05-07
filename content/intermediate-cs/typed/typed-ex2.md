---
title: "Typed Exercises 2"
date: 2019-05-07T07:41:36-05:00
weight: 60
draft: false
#type: slide
#theme: white
description: "Additional practice writing typed functions, includes lists and recursion."
---

1. `ezn`: Create a list of `n` numbers, counting from n down to 0.

        (check-expect (ezn 5) (list 5 4 3 2 1 0))
        (check-expect (ezn 7) (list 7 6 5 4 3 2 1 0))
        
2. `rpt`: Given a word and a number, make a list containing that word
   the given number of times.
   
        (check-expect (rpt "word" 4) (list "word" "word" "word" "word"))
        (check-expect (rpt "cat" 2) (list "cat" "cat"))
        
3. `perfect-squares`: Given a list of integers, return a list of all
   of the perfect squares contained in that list. If you work with
   real numbers, you probably want `Nonnegative-Real` numbers.
   
4. `grow-sq`: Given a start and end integer, make a list of images,
   all squares beginning at side length start, and ending at side
   length <= end.
   
5. `sqc`: Given two integers `start` and `end`, draw one image which
   is an overlay of images as n goes from `start` to `end` increasing
   by 10 each time. The image is a circle of radius n when n is even
   and a square of side length 2*n when n is odd.
