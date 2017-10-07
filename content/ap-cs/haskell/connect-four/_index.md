---
title: "Connect Four"
date: 2017-10-06T09:53:05-05:00
tags: 
 - haskell
 - project
draft: false
description: "Connect Four project description, including function signatures."
---

**Due Thursday, October 12**

Familiarize yourself with the game of 
[Connect Four][2], possibly [playing a few games][1]. 

## Functions to write

This is a minimum set of functions to write:

* `draw_board :: Board -> String`
* `make_move :: Board -> Player -> Position -> Board`
* `is_legal_move :: Board -> Player -> Position -> Bool`
* `is_won :: Board -> Bool`
* `winner :: Board -> Player`

## Advanced functions

When you are done with the minimum set of functions, consider writing
functions that make better and better moves.

* `any_legal` gives the first legal move it finds.

* `win_or_any_move` is an improvement over `any_legal` that makes a
  winning move if there is one.

* `win_or_get_three` is an improvement over `win_or_random_move` that
  plays to get three in a row if it cannot get four in a row.

* `best_move` picks a move that will lead to a win if one exists and
  avoids moves that lead to losing. 
  
The last function is the most interesting, but will require doing some outside
reading on the [minimax algorithm][3], perhaps looking at an [implementation for Connect Four][5].

## Design process

Make a plan before you start writing code! I recommend the top-down
design that we discussed last year.

Please have each step of the design process visible for each
function. It will speed your work and made it easier to understand!

1. Purpose for the function
2. Signature for the function
3. Example(s) showing how the function will work. 

     Put the examples for the function called `work` into a function called `test_work`.

4. Write the function. 


## Technical details

1. Question: How do you print on more than one line?

    Answer: Put "\n" in your string. For example: "One line\nSecond line".

    Example: 
```haskell
    drawBoard xs = "__XX\n_OOO"
    main = do putStrLn $ drawBoard [[0,0,1,1],[0,2,2,2]]
```

2. Question: What is the difference between 'X' and "X"?

    Answer: 'x' is a character (Char), and "X" is a String, which is a list of characters.

3. Question: How do you define a type shortcut?

    Answer: `type Board = [[Int]]`

4. Question: How do you define a struct?

   Answer: it will be easier if you do not do this, but [Chapter 8 in LYaH][4] has all of the information you need. 

[1]: https://www.mathsisfun.com/games/connect4.html
[2]: https://en.wikipedia.org/wiki/Connect_Four
[3]: http://www.cs.cornell.edu/courses/cs2110/2014sp/assignments/a4/A4ConnectFour.pdf
[4]: http://learnyouahaskell.com/making-our-own-types-and-typeclasses#record-syntax
[5]: https://github.com/erikackermann/Connect-Four
