---
title: "I.7 Semester I Review 7"
date: 2019-01-23T17:34:54-06:00
weight: 70
draft: false
#type: slide
#theme: white
description: "Additional review exercises."
---

This page contains additional review exercises.

## Basic Spanish

We will write a function to conjugate regular
verbs "-ar" and "-er" verbs according to the following chart. Use the
ending letters to decide how to categorize a given verb. We will only
consider the present and past tense (preterit) of the verbs.

| Verb   | Subject | Past? | Result is base + | Example ("andar"/"correr")   |
|--------|---------|-------|------------------|-----------|
| -ar    |   yo    | false |  -o              | ando      |
| -ar    |   yo    | true  |  -é              | andé      |
| -ar    |   tu    | false |  -as             | andas     |
| -ar    |   tu    | true  |  -aste           | andaste   |
| -er    |   yo    | false |  -o              | corro     |
| -er    |   yo    | true  |  -é              | corré      |
| -er    |   tu    | false |  -as             | corres     |
| -er    |   tu    | true  |  -iste           | corriste   |

Example: 
```
(define past-tense? true)
(check-expect (conjugate "correr" "tu" past-tense?) 
              "corriste")
```

Note: ignore accents.

**Too much?** Try the simplified, present tense only function:

| Verb   | Subject | Result is base + | Example ("andar"/"correr")   |
|--------|---------|------------------|-----------|
| -ar    |   yo    |   -o             | ando      |
| -ar    |   tu    |  -as             | andas     |
| -er    |   yo    |   -o             | corro     |
| -er    |   tu    |  -as             | corres     |


## Placed objects

An `image-posn` is an image together with a posn.

   1. `draw-it: ip image(background) -> image`
   2. `teleport: ip(shape1) ip(shape2) -> ip(new-shape1)`: Produce a new `ip` whose image is the same as `shape1` but whose position is the same as `shape2`. This has the effect of moving shape1 on top of shape2.
   3. Make an animation that remembers _two_ images with their positions.
   4. When you hit the "t" key, the first image teleports to the second image.
   5. When you click the mouse, the first image jumps to the mouse's position.
   6. The second image slowly moves left and up from its original position, maybe 6 pixels every 0.5 seconds.
        
