---
title: "Quiz 4 (Medium)"
date: 2019-03-04T07:34:29-06:00
weight: 99
draft: true
#type: slide
#theme: white
---

1. `ssm: number(start) number(end) -> number`. Find the sum of all of
   the square roots of odd numbers between `start` and `end`
   (inclusive). Except skip taking the square roots of any perfect
   squares like 49
   
        (check-within (ssm 21 27) 
                      (+ (sqrt 21) (sqrt 23) (sqrt 25) (sqrt 27))
                      0.01)
                      
        (check-within (ssm 7 12)
                      (+ (sqrt 7) (sqrt 11)) ; skip 9 - perfect square
                        0.01)


2. The `pairorder: string -> string` function takes a string and puts
   each adjacent pair of letters in alphabetical order, beginning at
   the left.
   
        (check-expect (pairorder "ba") "ab")
        (check-expect (pairorder "cba") "bac")

        
   
