---
title: "Checkers Outline"
date: 2019-05-20T07:21:56-05:00
weight: 20
draft: false
#type: slide
#theme: white
description: "An outline of all of the functions you could use to make checkers."
---

The game development process has several steps:

1. Examples: write down several examples showing different situations
   that will occur in the game. Make sure you consider all of the
   possiblities. In checkers, this should include winning and you
   should consider whether you are going to allow double jumps and
   forced jumps. (Both of those can be added in later. I consider them
   "advanced" topics.)
   
2. Model: decide on the model you will use for the game.

3. Draw handler.

4. Support functions:

    * `is-occupied?: (Listof Piece) Posn -> Boolean`
    * `is-my-piece?: Integer Piece -> Boolean`
    * `legal-move?: Game Posn -> Boolean`
    * `take-piece: (Listof Piece) Posn -> (Listof Piece)`
    
    


