---
title: "Reversi"
date: 2018-05-16T21:37:34-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "The game of Reversi."
---

The game of [Reversi](https://en.wikipedia.org/wiki/Reversi) is played with black and white pieces on an 8x8 board. 

Read the [official rules](https://en.wikipedia.org/wiki/Reversi#Rules); this is just a summary: 

* A play must flip at least one piece to the player's color. (See the rules for when pieces flip.)
* Pieces are never removed from the board.
* The winner has the most pieces on the board when no more moves are possible.

## Notes on design

Making a two-player, one-screen game is most of the effort. Making two
players on two screens is a short addition to that.

### Board Coordinates

What you read will suggest labeling columns with letters a-h and rows with numbers 1-8.
I recommend using typical computer coordinates 0-7 for each, and representing a location on the board by a posn.

### Player Naming

You could identify your players by colors (dark or light) or numbers (0 or 1). The draw handler is easier if your players are "black" and "white", but other functions may be more annoying. I suggest 0 and 1.

## Model

There are two possibilities, both have advantages and drawbacks. My guidance will focus on the first method.

1. Keep the color (light/dark) and position inside a `piece` structure, and then the whole state of the board is represented by a list of pieces. 

        (define-struct piece (player posn))
        (define-struct game (turn piece-list))

2. Keep a separate list of light and dark piece positions.

        (define-struct game (turn light-list dark-list))
        ; light-list: (listof posn?)
        ; dark-list: (listof posn?)
        
## Useful functions

It is a lot simpler to build something complex like Reversi by building helper functions first.

* `off-board?: posn -> boolean`. Is the posn off the board?
* `opponent: player -> player`. Return the opponent.
* `flip: piece -> piece`. Return a new piece with the same position but the opposite player.
* `draw-one-piece: piece image(bg) -> image`. Draw one piece on a given background image.
* `draw-all-pieces: listof-piece image(bg) -> image`. Draw a whole list of pieces on a background image.
* `has-piece?: listof-piece posn -> boolean`. Returns true if there is a piece at the given posn in the list.
* `get-piece: listof-piece posn -> piece`. Get the piece at the given position out of the list. You could return `false` if the piece is not in the list, or give an `error`.

## Warmup Exercises

* `take-flippable: listof-number(data) number(player) -> listof-number`: Get a list of the numbers from the start of `data` that do not match `player` (i.e., opponent's pieces) and the first occurrence of `player` if there is one.

        (take-sequence (list 1 1 2 1) 1) => (list 1 1 2)
        (take-sequence (list 1 1 2 1) 2) => (list 1)
        (take-sequence (list 1 1 1) 2) => (list 1 1 1)

    Why is this useful? When we play, we need to flip at least one piece. Pieces that are flipped must be sandwiched between two pieces of the same color. The pieces that do not match the player will be flipped. We need the first matching piece in order make sure the sequence does not stop at the edge of the board (like the third example above).
    

# Wrong stuff below = fixme

## Flipping pieces

The trickiest part is making the pieces flip over. This is important to get right because a move is not even legal if it does not flip any pieces. I suggest checking in each direction from a given position to see if there are any pieces that will flip.

* `take-flip-dir?: listof-piece posn(start) posn(direction) player -> boolean`. Will placing a piece for `player` at `start` cause any pieces in the given `direction` to flip?
 
    Assume we have already constucted a variable `pieces` with dark as `X` and light as `O`, representing the board below:

        #|
            0123
         0  -OOX
         1  XXOO
         2  X-OX
         3  ----
         |#
         
        (will-flip-dir? pieces (make-posn 0 0) (make-posn  1  0) 'X') => true
        (will-flip-dir? pieces (make-posn 0 0) (make-posn  0  1) 'X') => false
        (will-flip-dir? pieces (make-posn 1 2) (make-posn  0 -1) 'X') => false
        (will-flip-dir? pieces (make-posn 1 2) (make-posn  0 -1) 'O') => true
        (will-flip-dir? pieces (make-posn 1 2) (make-posn  1 -1) 'X') => true
        (will-flip-dir? pieces (make-posn 1 2) (make-posn  1  0) 'X') => true
        (will-flip-dir? pieces (make-posn 3 3) (make-posn -1 -1) 'X') => true
        (will-flip-dir? pieces (make-posn 2 3) (make-posn  0 -1) 'X') => false

    A careful consideration of all of the possibilities on a small board
    is a good idea. Obviously you need lots of checks!
* `will-flip-any-dir?: listof-piece posn(start) color(player) -> boolean`. Will placing the `player` color piece at `start` cause any pieces in any direction? This should be straightforwad to write once you have `will-flip-dir?`.

* `flip-pieces: listof-piece posn(start) posn(direction) player -> listof-piece`. Flip the pieces from `start` going in the given `direction`.
* `flip-all-pieces: listof-piece posn(start) -> listof-piece`. Make all of the flips caused by placing a piece at the given position.
