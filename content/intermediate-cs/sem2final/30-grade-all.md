---
title: "Sem.II Final Exam 9-11"
date: 2018-06-11T20:40:26-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Full length final exam for intermediate computer science."
---

{{< use-goodlists >}}

This is the Spring 2018 final exam for Intermediate Computer Science. The exam is 60 points. There are 40 points for the paper questions and 20 points for the computer program.

## Paper analysis

You may not use the computer to do anything but read this section. Turn in your paper when you are done and ready to begin the next section (coding). You cannot come back to this section after you turn in your paper.

1. (5 points) Write the output from each. If an error results, indicate why.

    1. `(list 1 20 30 empty)`
    2. `(list 20 40 (list 60 80) 100)`
    3. `(list* (list 1 2 3) 4)`
    4. `(list 11 12 (list* 13 14 empty))`
    5. `(cons 2 (cons 8 (list* 16 (cons 32 empty))))`

2. (5 points) The code below is intended to make a list of all of the
integers in the `data` that are above 50. Of the numbers that are above 50, the ones below 100 should be replaced with 100.

    Give an example of a test case that it can pass and a test case that it fails.

        (define (add-ex data)
          (cond [(> 50 (first data))
                 (list* (first data) 
                        (add-ex (rest data)))]
                [(< 50 (first data) 100)
                 100]
                [else (add-ex (rest data))]))

4. In a universe program, there are plants (circles) at various coordinates. Each one naturally grows at a 1mm (radius) per tick.  There are two possible actions: click an area to "fertilize" and "reset".

    * The "fertilize" message will affect every player within distance of 10 units from the place it was applied. 
    * The spread message causes each world to grow +2 faster than previously.
    * The "reset" message will affect everyone. The reset message resets them to their initial growth rate.
    * A single player can fertilize their plant by hitting "f" and trim their plant (shrinking radius by 9) by hitting "t". 

    Your job is:

    1. (5 points) List some essential items in the model, and explain your choice.
    2. (5 points) Describe a possible message struct.
    3. (10 points) Explain in detail the receive-handler, including any changes 
    to the model or messages sent. 
    4. (10 points) Write the key handler.

## Coding on the computer

You may use the Racket Help Desk and the class blog to write this function. 

3. (20 points) The function `shuffle`: list(deck) -> list is supposed to split the deck into two pieces `(a1 a2 a3 ...)` and `(b1 b2 b3 ...)` and then put them back together by interleaving the two pieces: `(a1 b1 a2 b2 ...)`. There should be no randomization.

    Design and implement the `shuffle` function, including all "edge cases" (so the function will always work). As always, you may use helper functions.

        (check-expect (shuffle (list 10 20 30 40)) 
                               (list 10 30 20 40))
		(check-expect (shuffle (list 10 20 30 40 50))
                               (list 10 40 20 50 30))

Points for testing (5 points) and function correctness (15 points).

