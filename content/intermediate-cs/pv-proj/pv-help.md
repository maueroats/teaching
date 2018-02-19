---
title: "Help with Corrupted Models"
date: 2018-02-18T17:31:40-06:00
weight: 20
draft: false
#type: slide
#theme: white
description: "How to debug corrupted model errors by using your own check-with function."
---

We have not talked about writing your own `check-with?` function. That can really help if you have not been careful about signatures and some of your functions do not do what they are supposed to do. Here is a brief tutorial how to create a really good checker function.

In the big-bang, `(check-with game?)` makes sure that the model is
always a game. That saves you from the problem of returning a number
from a tick handler that is supposed to return a game. It doesn't
prevent you from messing up the things inside the `game` struct (like
putting a number where a posn is supposed to be).

To debug problems with your model being corrupted, you need to write
your own check-with function that makes sure everything _inside_ the
model is OK too.

## Simple check-with 

This example shows how to check a model that has two posns and a
number.

``` racket
(define-struct game (pos1 pos2 n)) 

(define (good-game? w)
  (and (game? w)
       (posn? (game-pos1 w))
       (posn? (game-pos2 w))
       (number? (game-n w))))
       
(big-bang ...
   (check-with good-game?))
```

## Advanced check-with

If your model is supposed to be a PV and a number, then you should write a really elaborate
checker that makes sure everything has the right types.

```racket
(define-struct pv (p v))
(define-struct game (pv n))

(define (good-pv? w)
  (and (pv? w)
       (posn? (pv-p w))
       (posn? (pv-v w))))

(define (good-game? ww)
  (and (game? ww)
       (good-pv? (game-pv ww))
       (number? (game-n ww))))
```
