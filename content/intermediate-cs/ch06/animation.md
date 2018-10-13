---
title: "Intro to Animations"
date: 2018-10-12T21:34:49-05:00
draft: false
type: slide
theme: white
description: "The basics of big-bang: on-tick, on-draw."
weight: 1
---

# Intro to Animation

---

# Opener

Write two functions:

* `rotator: image -> image` that turns the image 10 degrees.

* `middle-placer: image -> image` that places the given
image in the center of a yellow circle of radius 200.

---

# Animation Code

```racket
(define starter (rectangle 50 200 "solid" "purple"))
(define delay-time 3)
(big-bang starter
          (on-tick rotator delay-time)
          (on-draw middle-placer))
```

---

# Animation Vocabulary

* model: the part that changes

* on-tick: model -> model

  Moves to next time.

* on-draw: model -> image

  Shows the result. Draw things that do not move here.

--- 

# Paper Exercise I

* A shape is shown on a yellow circle of radius 200. 

* The shape grows 25% larger every tick, but the circle does not.

1. Write a tick handler.

2. Write the big-bang.

---

# Paper Exercise II

* A shape starts in the center of a circle.

* The shape moves to the right 10 pixels every tick.

## Write the tick handler

---

# Class work

Exercises 6.4.2 and 6.4.3 (pdf page 106)

Bonus: 6.4.4

# Homework

Read Section 6.3 (beginner mistakes)

---

# Animation more vocab

* on-key: model key -> model

* on-mouse: model number(x) number(y) event -> model

---

You found [the code!](animation-day1.rkt)
