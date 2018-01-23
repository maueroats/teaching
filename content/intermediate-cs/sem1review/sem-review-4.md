---
title: "I.4 Semester I Review 4"
date: 2018-01-23T14:36:09-06:00
draft: false
weight: 40
#type: slide
#theme: white
---

Remember to practice writing check-expects for your functions, so you
have a way to make progress.

1. Analyze the program segment below. 

        (define initial "large fluffy bunny")
        (define (f model) (+ 1 (string-length model)))
        (define (g model) (text model 25 "black"))
        (define (k model x y e) (string-append model x))
        (define (p model w) (substring model 1))
        (big-bang initial ...)
        
    1. Is `f` suitable for a tick handler? Explain.
    2. What could `g` be used for?
    3. Are either `k` or `p` suitable handlers? If so, for what?
    4. Write a useful, correct `check-expect` for the function `p`.
    5. Write a useful, correct `check-expect` for the function `k`.

2. The [median](https://www.mathsisfun.com/definitions/median.html) is
   the middle number in a list of sorted numbers. Write the function
   `median` that works for three numbers.
   
            median: number number number -> number

    Writing tests is the most important part of this exercise.

5. **Structures** 

    1. Make a structure `scn` that has fields for a string, 
       a color, and a number.

    2. Create an example of your structure and put it in a variable.

    3. Write a function that gets the number out of your structure 
       and adds one to it. 
    
            sincr: scn -> int

    4. The `sdraw` function draws a circle with the given color, using
       the number for the radius. Unless the string is `square`, in
       which case draw a square in the same way.
        
            sdraw: scn -> image

    5. Write a function `scolor` that makes a new structure with the
       given color, not changing any of the other fields.
    
            scolor: scn color(new) -> scn

    6. The `scat` function takes in two structures and combines them
       by appending the strings and adding the numbers. The color of
       the result will be the same as the first structure's color.
       
            scat: scn scn -> scn
             
