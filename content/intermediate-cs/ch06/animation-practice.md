---
title: "Animation Practice"
date: 2017-10-05T21:58:10-05:00
draft: false
description: "Practice writing big-bang code and identifying common errors."
---

## Progress bar 1

Make a solid purple bar that starts in the middle of the left side of the screen and grows to the right at a constant rate.

1. Model

2. Draw handler

3. Tick handler

Add in a feature so that the bar shrinks when you wiggle the mouse.

([Solution code](purple-bar.rkt))

## Errors #1

What is wrong?

The variable [indoors](http://img10.deviantart.net/cb20/i/2009/014/2/4/indoor_scene_by_thekeyofe.png) is an indoor picture.

```racket
(define indoors ...)
(define model (overlay pic:stick-figure 
                       (empty-scene 300 200)))
(define (tick-h img)
   (overlay img indoors))
```

## Errors #2

What is wrong? 

```racket
(define start pic:stick-figure)
(define tick-h (beside (square 10 "solid" "white") start))
(big-bang start
          (on-draw show-it)
          (on-tick tick-h)

```
