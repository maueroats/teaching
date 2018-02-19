---
title: "Draw Handler Helpers"
date: 2018-02-19T13:39:39-06:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Use multiple helper functions to create a big draw handler."
---

Combining draw handlers works just like [combining tick handlers]({{% relref 
"pv-tick-handler.md" %}})

The best signature for a draw handler helper is:

     draw-handler-helper: model image(background) -> image

This helper draws its result on top of a background that it is given.
Giving the answer from one draw handler helper to another lets you combine the images.

     (define (real-draw-handler model)
         (draw-handler-helper-1 model 
             (draw-handler-helper-2 model UNMOVING-BACKGROUND)))
             
             
