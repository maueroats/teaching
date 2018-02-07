---
title: "21.7.6 Tick Handler"
date: 2018-02-06T21:47:06-06:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Combining actions into one big tick handler."
---

You can combine two tick-handler actions into one by using "function composition":

```racket
; first-action: model -> model
; second-action: model -> model
; tick-handler: model -> model
(define (tick-handler model)
   (second-action (first-action model)))
```

Try combining the ball bouncing and ball moving actions in this way.

