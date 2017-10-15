---
title: "Animation Examples"
date: 2017-10-15T14:15:53-05:00
draft: false
---

Here is a complete example that shows how to:

* move an image down every tick
* draw three copies of the image in a row
* make the image get larger when you hit a key
* make the image get smaller when you move the mouse


## Big bang

The big bang goes last in the Racket file, but it is first here so you can see
how everything comes together.
```racket
(big-bang original-model
          (on-tick move-down)
          (on-draw three-copies)
          (on-key reset)
          (on-mouse shrink))
```

## Tick handler

Move the image down by inserting an invisible rectangle above it.
```racket
(define (move-down model)
    (above (rectangle 0 5 "solid" "white")
           model))
```

## Draw handler

Draw three copies of the same thing in a row. (Use this trick for the tires of your car!)
```racket
(define (three-copies model)
  (overlay/align "middle" "top"
   (beside model
           (rectangle 75 0 "solid" "white")
           model
           (rectangle 75 0 "solid" "white")
           model)
   (empty-scene 500 400)))
```

## Key handler

Always return the original model, no matter what. This resets the animation.

```racket
(define original-model (square 50 "solid" "purple"))
(define (reset model key)
  original-model)
```

## Mouse handler

Shrink the model by 1% any time the mouse is moved.
```racket
(define (shrink model x y event)
  (scale 0.99 model))
```
