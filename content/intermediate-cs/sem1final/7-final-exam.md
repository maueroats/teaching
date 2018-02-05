---
title: "7. Final Exam"
date: 2018-01-31T22:42:36-06:00
weight: 70
draft: false
#type: slide
#theme: white
description: "Period 7 final exam."
# Final Exam
---

This is the final exam for Intermediate Computer Science, Semester I,
2017-2018. Except as noted below, you may not use materials previously
written by you or anyone else.

There are two sections: written (1/3) and programming (2/3). Before
you use a computer, you must turn in your answers to the written questions.

Write all of your solutions on a separate sheet of paper. 

## Written Questions 

**(30 points)**

In the written portion, you may not consult any sources. Suggested
time: 30 minutes.

1. (10 pts) A function `ch-col` takes in a color and changes red by a
   random amount in the [-15,15] interval, and changes blue by twice
   that same random amount.
   
    1. Write a signature for the `ch-col` function.
    2. Explain a method of testing the `ch-col` function. (That is,
       how do you go about adding testing to this situation?)

2. (10 pts) The data definition for the `game` struct is below. 

        ; STRUCT game: t1=number, t2=number, poss=number
        ; purpose: remember points for team 1 and team 2, 
        ; and which team has possession of the ball (1 or 2)

    Write the `simple-score: game -> game` function that records
    a two point score for the team that has possession (which is always 1 or 2). 

3. (10 pts) An animation uses the `game` struct from the previous
   question as a model.  What could you add to your `big-bang` to help
   you find the source of errors in your mouse handler like: "game-t1:
   expected a game, given `12`"? Explain briefly.

4. (10 pts) Meg is writing a program. She is part way done, and now
wants to finish the design and test it.

        (define (f x y z) (* x y))

     1. Write a signature.
     2. Write one good test for this function.
     3. Why might a function have a useless parameter like that?
  
## Programming Questions 

**(60 points: do both)**

In the programming portion, you may use the book _Picturing Programs_,
the Racket Help Desk, your `posn-util.rkt` file, and the class blog. 

Your work will be evaluated on the basis of correctness and how well
it demonstrates your understanding of the design process.

Suggested time: 60 minutes. 

1. **Grapher**. (30 pts) The equation `x=130*sqrt(1-(y/120)^2)` is half of an
   ellipse when the y-coordinates range from -120 to 120. 
   When the mouse is clicked, jump to the point
   on the graph with the same y-coordinate as the mouse.

    {{% figure src="half-ellipse.png" %}}
    
    * Graph using people coordinates in the formula.
    * Display in a 450x220 window.
    * Origin is (225,110) in computer coordinates.



2. **Red light, green light**. (30 pts) A light (circle on the screen) is
   always either red or green. It changes color randomly every 0.5
   seconds. The player is any small image on the screen.

    * Clicking when the light is green moves your player
      50 pixels toward the top of the screen.
    * Clicking when the light is red moves your player back to the 
      bottom of the screen.


