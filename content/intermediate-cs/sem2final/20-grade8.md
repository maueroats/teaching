---
title: "Sem.II Final 8"
date: 2018-06-06T22:38:48-05:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Exam for everyone, final for grade eight students."
---

You should write all of your answers.
You may use the Racket help desk and the blog, if necessary.


## Drawing

You are planning a graphics animation. Description:

   * right,left: control number of blue circles
   * up,down: control radius of big red circle and height of box (4 times diameter of circle)
   * mouse: set width of box with a click

   {{% figure src="circ-demo1.png" %}}
   {{% figure src="circ-demo2.png" %}}

   1. What model should you use?
   2. How will you position the red circle just above and to the right of the green box, as shown in the picture? Be specific.
   3. Write a `check-expect` that shows what the key-handler does when you hit the right arrow key.
   4. The left-most blue circle has a radius equal to the diameter of the red circle. Each blue circle has a 10% smaller radius than the one to its left. Write the `draw-blue-circles` (`dbs`) function, including contract and Racket code. You can make the signature as needed 

## Logic

1. Middle age is defined as being age 30 through 55, inclusive. It can
be hard to find out how old someone is, so we will just estimate based
on the year. Write `is-middle-age?: string(birthday) number(current year) -> boolean`. Note the different formats of birthday we accept (below). 

          (check-expect (is-middle-age? "1/4/1960" 2000) true)
          (check-expect (is-middle-age? "11/30/1955" 2015) false)
          (check-expect (is-middle-age? "6/25/2000" 2018) false)

2. *Number list*. Create a list of all of the numbers from start to end that are divisible by 7. Except if you discover a number divisible by 49 then stop your list there. `n7: number(start) number(end) -> list of numbers`.



## Four-Square


The game of four square is a childen's game. There are some [pretty
official rules](http://www.squarefour.org/rules) as well as a [short
Wikipedia description of four
square](https://en.wikipedia.org/wiki/Four_square). Summarizing and
interpreting for a computer game:

* ball speeds up a lot if you hit it when the velocity is nearly zero
* ball speeds up a little if it is going down when you hit it
* ball can be passed to any other square
* we need to see the ball move to play the game
* Squares are numbered 1 through 4. Players enter in square 4 and move up to square one as players above them are eliminated.
* A player is eliminated when the ball hits their square and they do not hit it before it bounces again.
* When a player is eliminated, the other players move up (in order) and a new player joins the board in square four. 

1. Struct for the player
2. Struct for the ball
3. An AI player called "hater" is randomly sends the ball to square 1 (75% of the time) or square 2 (25% of the time).  Unless the player is in one of those squares, in which case it attacks the strongest two opponents that it can (with the same likelihoods). Write the function `play: player ball -> ball` that has the AI play. Assume there is a `hit: ball -> ball` function that updates the ball velocity.
4. What handler(s) should be responsible for actually making the ball move from one "square" (world) to another? Explain carefully.

