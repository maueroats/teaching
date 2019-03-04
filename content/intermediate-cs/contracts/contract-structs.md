---
title: "Contract for Structs"
date: 2018-02-21T10:07:36-06:00
weight: 20
draft: false
#type: slide
#theme: white
#description: 
---
When you are working with a structure, the best way to make sure 
it does not get "broken" is to write a function to check that each 
part of the struct has the correct type.
<!--more-->

Here is an example of a game struct that has fields for: player-1
posn, player-2 posn, player 1 score, and player 2 score. We write a
function to use in our handlers that makes sure the fields that are
supposed to be positions are posns and the fields that are supposed to
be scores are numbers.

    (define-struct game (p1pos p2pos p1score p2score))

    (define (good-game? g)
      (and (game? g)
           (posn? (game-p1pos g))
           (posn? (game-p2pos g))
           (number? (game-p1score g))
           (number? (game-p2score g))))

When the model is a `game`, how would you write the contract for the mouse-handler?

