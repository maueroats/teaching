---
title: "6. Animations I"
date: 2017-10-04T13:03:22-05:00
draft: false
weight: 60
description: "Big-bang for animations. Essential information and walkthroughs."
---

## Essentials

These essentials are on page 100 (PDF page 111) or page 138 (PDF page
149). **There is a detailed checklist on page 105 (PDF page 116)**. Use it!
You should memorize them.

* `model`: What the computer remembers.

* `draw-handler: model -> image`: Draw the model on the screen; adds non-moving parts to the image. (`on-draw`)

* `tick-handler: model -> model`: Update the model as time passes. (`on-tick`)

* `key-handler: model key -> model`: Update the model when a key is hit. (`on-key`)

* `mouse-handler: model x y event -> model`: Update the model when the
  mouse is moved or clicked. The inputs x and y are numbers, the event is a string. (`on-mouse`)

## Topics

{{% children %}}
