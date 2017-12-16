---
title: "20. Click Circle"
date: 2017-12-15T15:38:59-06:00
draft: false
#type: slide
#theme: white
weight: 30
description: "A circle moves around the screen randomly. You win if you can click on it."
---

Exercises 20.6.3 and 20.6.4.

* A circle moves to a random position on the screen every so often. (20.6.3) 

* Clicking on the circle displays a win screen. (20.6.4) Note: I recommend using a special `posn` as the model to indicate when to display the win screen.

## Stop-when

There is a new clause in `big-bang` called `stop-when`. It works like the [linked demo code](stop-when.rkt). The `big-bang` looks like this:
```racket
(big-bang 0
          (on-tick add1 0.1)
          (on-draw draw-num 300 200)
          (stop-when above-ten? draw-done))
```
The `above-ten?` method takes in a model and produces a boolean value. The big-bang stops if this function returns true.

The `draw-done` method is a draw handler called when to produce the last frame of the animation - regarless of why the big-bang is ending.

## Notes

* Never place randomness in the draw handler. The draw handler can be called lots more frequently than you imagine (for example, when you drag the window and it needs to redraw).
* Your model should not be an image any more. Use a better model.

* [Complete big-bang documentation](https://docs.racket-lang.org/teachpack/2htdpuniverse.html) so you can look up any unusual keys or functions that you need. For example: `button-down`.

