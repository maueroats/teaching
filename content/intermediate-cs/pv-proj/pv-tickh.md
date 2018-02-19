---
title: "Tick Handler Helpers"
date: 2018-02-19T17:03:54-06:00
weight: 25
draft: false
#type: slide
#theme: white
description: "Use multiple helper funcitons to create a tick handler that does multiple actions."
---

(Copied from the earlier [combining tick handlers]({{% relref 
"pv-tick-handler.md" %}}) page.) 
You can combine two tick-handler actions into one by using "function composition":

```racket
; first-action: model -> model
; second-action: model -> model
; tick-handler: model -> model
(define (tick-handler model)
   (second-action (first-action model)))
```

Usually `first-action` makes one object move and `second-action` makes
another object move. Writing separate functions makes it easier to test and reduces the
confusion of doing multiple actions at once.


