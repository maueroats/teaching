---
title: "Animation Project"
date: 2017-10-20T14:46:03-05:00
draft: false
weight: 50
#type: slide
#theme: white
---

**Deadline**: Finish before Monday, October 23. Turn in Tuesday, October 24.

**Produce**: One sequence of big-bang animations per group. (Groups of at most two.)

**Goal**: Animation projects should demonstrate the use of draw, tick, mouse, and key handlers. 

**Time**: Spend approximately two hours on this project. 

Making an animation is a way to study for Monday's animation
test. Think of your work as a way to study and become more familiar
with animations.

## Suggestion

We don't have the technical skills to make animations that work exactly like you imagine. A compromise is to break your idea into several "scenes", put each scene into a big-bang, and then manually close the window each time to advance to the next big-bang.


## Ideas

* House of Mirrors
* Illusions
* Jump Scare (one big-bang ends and another starts)

## Requirements

* Every type of handler is used
* Design process visible for at least one big-bang.
* Please save all large images separately and load using `bitmap` (see note).

## Details

You should consider these inspirations:

* Drawing: placing a moving object behind another object.

* Motion: rotate, move by adding (above), move by subtracting (crop)

* Placing more than one moving image on a screen.

    - place-image
    - overlay/align
    

## Important Note

Save all big images separately. Put the "bigImage.png" file in the
same folder you have saved your Racket program. Load the picture like this:
```racket
(define background (bitmap "bigImage.png"))
```

Use the same method to keep transparency in images that you have found online.

