---
title: "Battleship Outline"
date: 2018-04-16T15:05:11-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Game logic, draw handler, mouse handler."
---

In order for all of us to be working with a similar model, this page
uses the definitions below for `ship` and `game`.

        (define-struct ship (name posns))
        (define-struct game (ships shots))
        
## Game logic

* `shot-hit-ship?`: posn(shot) list-of-posns(ps) -> boolean. True if
  the shot hit the ship specified by the posns.
  
* `shot-hit-any-ship?`: posn(shot) list-of-ships -> boolean. True if
  the shot hits any one of the ships.

## Drawing

* You should have constants defined for the width and height of the board. 
Call them `COLUMNS` and `ROWS`.

There are two different, equally valid, ways to draw:

1. Draw the grid, filling in the correct coloring for each square as you go.
2. Draw an empty grid, then fill in each shot using `place-image`. 

This discussion will use the second method.

### Sizes

How big should each grid square be? You get to decide, but make a
constant instead of just writing "40" or "50" everywhere in your code.

### Draw grid

Hopefully you've done this before. Usually two functions combine to make a grid. 

1. `horizontal-stack`: number(m) image -> image. Repeat the image
   (which will be a grid square) M times.
   
2. `vertical-stack`: number(n) image -> image. Repeat the image (which
   will be a row of squares) N times.

### Grid coordinates

When we talk about the square at grid coordinates (0,2), we mean row 0
(the top row) and column 2 (which is the third column, since we start
counting from zero).

Image coordinates are usually numbers like (20,100), representing the
actual location in the image of the center of the grid square.

### Draw shots

Drawing the shots means we have to translate from grid coordinates to image coordinates.

When each square is 40x40, what are the coordinates of the center of grid square (2,1)? 
Draw a picture and figure it out now!

* `grid->image-coords`: posn -> posn. Translate the grid coordinates
  to image coordinates. should depend on the size of the square.

* `draw-one-shot`: game posn(shot) image(bg) -> image. Draw one shot
  on the background. You will need to decide if the shot is a hit or
  a miss before you draw it.

* `draw-all-shots`: game list-of-posn(shots) image(bg) -> image. Draw
  all shots on the background.
  
## Mouse handler

When you click on a square, it should make a "shot" that hits that square.

Example: grid squares are huge, 100x100. You click on (310, 190). What
board square contains that click?

Answer: (3,1). Just divide each coordinate by the size of one grid square.

* Signature: `mouse-handler`: game(old-model) x y event -> game(new-model). 

* Purpose: when the event is a click, add the corresponding square to
  the list of shots in the model.
