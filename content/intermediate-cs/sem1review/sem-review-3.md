---
title: "I.3 Semester I Review 3"
date: 2018-01-21T23:14:35-06:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Practice: red-blue, spam-circle, rectangle limitations. Review reading."
---

At home you may want to do some review reading and practice. You should be able to do review questions 1 and 2 in one day, and question 3 in a second day. Ask if you have questions!

## Review Reading

Reading the book and looking at old exercises is a very productive way to study. Struggling in Chapter 21 (new structures)? 

* Read 21.5 ("Functions returning user-defined structs") and do the exercises. 
* Read the extended example in 21.6 (moving-x). 

Other good chapters to read are: 20 (posn and color), and 17 (animations using cond).


## Review Questions 

1. **Red-blue**. Standard dice have 6 sides, numbered 1 through 6. Play a game with a standard blue die and two standard red dice. The number of points you get is ten times the blue roll plus three times the sum of the other two. Except you get zero points if your red dice total 4. Design and test the `red-blue` function.

    ```text
    red-blue: any(ignore) -> number(points)
    ```

    [Solution to red-blue.](red-blue-soln.rkt)

2. **Spam-circle**. Every time you click, a circle appears centered on
the mouse.  The color of the circle changes is red the first click,
green the second, blue the third, red the fourth, and so on. Choose one option:

    1. display one circle at a time
    2. display all of the circles made so far

    Advanced variations:

    * Enter resets the color to red. 
    * The "c" key clears the screen. 
    * After five seconds, the game quits. 
    * When it quits, show how many circles the person currently has showing on the screen.

    [Solution to spam-circle.](spam-circle.rkt)

3. **Rectangle Limitations**. 
This will take a while. As you work on it, keep the design process in mind. Have a signature, purpose, and tests for every function. 

    The animation: as you move the mouse on the screen, a small circle follows the mouse.

       + At the start of the game, the circle is restricted to the rectangle 100<=x<=200 and 150 <= y <= 250. 

         That means that if the mouse is outside of that rectangle, the circle will stick to one of the rectangle's walls.
       + After t seconds, the circle can move in the larger rectangle 100-10t <= x <= 200+10t and 150-5t <= y <= 250 + 5t. 
       + After 10 seconds the animation ends.

    Breakdown of the creation process:
    
      - What model? Call it "m". It should be able to remember three posns: upper left, lower right, and a point anywhere on the screen.
      - Design and test `m-set-pt: m(model) posn(new-point) -> m(new-model)`... what should this function do? Look back at Chapter 21 Worksheets B and C if needed.
      - Design and test `limit-pt: posn(upper-left) posn(lower-right) posn(pt) -> posn (new-pt)`. This function makes a point that stays on the edge of the rectangle if pt is outside of the rectangle. Otherwise it does not change pt.
      - Mouse-handler: remember the actual real position of the mouse.
      - Draw-handler: use `limit-pt` to put the current mouse coordinates into the rectangle defined by the upper-left and lower-right posns in the model, then draw a circle there.
      - Tick-handler: change the upper-left and lower-right posns by (10,5) in the correct direction (add or subtract).
    
