---
title: "Connect Four UI"
date: 2017-10-09T11:01:32-05:00
weight: 5
draft: false
---

The [user interface code](ui-connect-four.hs) for Connect Four is a little clunky.
You may use the linked code. You do not have to learn this part of writing Haskell programs (yet).

## Code Outline

main: just make board and call event loop

event loop:

* draw board
* is it won?
    - print the win message
* not won? 
    - get a move
    - recursive call to event loop with updated board, next player

## Example run

```
*Main> main
        
        
        
        
        
        
(Enter -99 to quit.)
Player 1 moves.
Column [0-7]? 5
        
        
        
        
        
     X  
(Enter -99 to quit.)
Player 2 moves.
Column [0-7]? 2
        
        
        
        
        
  O  X  
(Enter -99 to quit.)
Player 1 moves.
Column [0-7]? 5
        
        
        
        
     X  
  O  X  
(Enter -99 to quit.)
Player 2 moves.
Column [0-7]? 3
        
        
        
        
     X  
  OO X  
(Enter -99 to quit.)
Player 1 moves.
Column [0-7]? 5
        
        
        
     X  
     X  
  OO X  
(Enter -99 to quit.)
Player 2 moves.
Column [0-7]? 4
        
        
        
     X  
     X  
  OOOX  
(Enter -99 to quit.)
Player 1 moves.
Column [0-7]?   5
        
        
     X  
     X  
     X  
  OOOX  
The game is over
Player 1 won!
```
