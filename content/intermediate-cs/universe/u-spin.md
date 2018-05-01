---
title: "Universe Spin"
date: 2018-04-30T10:22:34-05:00
weight: 40
draft: false
#type: slide
#theme: white
description: "Take turns making an image spin."
---

Each world has its own image which spins. Hitting a key makes that world's image start spinning and the other worlds' images stop spinning.

## Big-bang model

We will remember:

* our image
* our world number (1, 2, ...)
* the number of the world that should be spinning

## Universe model

The message will be a single number indicating which world should spin.

## Handlers

* draw-handler: model -> image
* tick-handler: model -> model
* key-handler: model key -> package
* message-handler: model message -> model
* main: string(name) image number(our-world-number) -> runs big-bang

