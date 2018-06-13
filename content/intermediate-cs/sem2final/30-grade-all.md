---
title: "Sem.II Final Exam 9-11"
date: 2018-06-11T20:40:26-05:00
weight: 30
draft: false
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

2. (5 points) The code below should add 7 to every number in a list of
   numbers.
   
        (define (add-7-list data)
            (list* (+ 7 (first data))
                   (add-7-list (rest data))))
                   
    What result will be produced from `(add-7-list (list 20 40 90))`?

2. (5 points) The code below is intended to make a list of all of the
integers in the `data` that are above 50. Of the numbers that are
above 50, the ones below 100 should be replaced with 100.

    The program for `add-ex` is wrong. It does not always produce the
    result that the purpose statement says it should. Answers that
    agree with the purpose statement are considered "correct".

    Give an example of a (nonempty) test case in which the `add-ex`
    function gives the correct answer, and another test case in which it
    fails to give the correct answer.

        (define (add-ex data)
          (cond [(empty? data) 
                 data]
                [(< 50 (first data))
                 (list* (first data) 
                        (add-ex (rest data)))]
                [(< 50 (first data) 100)
                 (list 100)]
                [else (add-ex (rest data))]))

4. (25 points) In a universe program, there are plants (circles) at
   various coordinates. Each one naturally grows at a 1mm (radius) per
   tick.  There are three possible actions:  "fertilize", "reset", and "trim".

    * A single player can fertilize their plant by hitting
      "f". Fertilizing also helps the plants nearby (see below).
    * Fertilizing causes each affected plant to grow +2 faster than previously.
    * Fertilizing a plant will also affect every plant within distance
      of 10 units in the same way. 
    * A single player can trim their plant (shrinking radius by 9) by
      hitting "t".
    * A single player clicking anywhere resets all plants to their
      initial growth rate of 1/tick.
    * **Simplification**: only keep the data for one plant in your
      model. You will interact with other plants as if they were in
      the same space, but you will not be able to see them.

    Your job is:

    1. (5 points) List some essential items in the model, and explain your choice.
    2. (5 points) Describe a possible message struct.
    3. (5 points) Explain in detail how the receive-handler handles
    the "fertilize" message, including any messages sent or changes 
    to the model.
    4. (10 points) Write the key handler.

## Coding on the computer

You may use the Racket Help Desk and the class blog to write this function. 

3. (20 points) The function `shuffle`: list(deck) -> list is supposed to split the deck into two pieces `(a1 a2 a3 ...)` and `(b1 b2 b3 ...)` and then put them back together by interleaving the two pieces: `(a1 b1 a2 b2 ...)`. There should be no randomization.

    Design and implement the `shuffle` function, including all "edge cases" (so the function will always work). As always, you may use helper functions.

        (check-expect (shuffle (list 10 20 30 40)) 
                      (list 10 30 20 40))
        (check-expect (shuffle (list 10 20 30 40 50))
                      (list 10 40 20 50 30))
        (check-expect (shuffle (list 1 2 3 4 10 20 30 40))
                      (list 1 10 2 20 3 30 4 40))

Points for testing (5 points) and function correctness (15 points).

