---
title: "Typed Excercises 2"
date: 2019-05-07T07:41:36-05:00
weight: 50
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
        
