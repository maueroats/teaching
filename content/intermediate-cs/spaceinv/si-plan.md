---
title: "SI Plan"
date: 2017-11-29T10:13:17-06:00
draft: false
#type: slide
#theme: white
weight: 10
description: "Planning for the space invaders game."
---

{{% figure src="si-plan-screen.jpg" %}}

## Game State

There are many quantities in the game that can change. Label them on
your diagram. For example, in my diagram I used `direction` to be `+1`
for moving right and `-1` when the enemy is moving left.

If you later discover that you want more information, add it to your diagram. 

## Constants

Make variables to represent the quantities that are not going to
change, but could. You may find a use for these, or add your own:

* WIDTH
* HEIGHT
* ENEMY-WIDTH
* ENEMY-HEIGHT
* TURRET-WIDTH
* TURRET-HEIGHT
* BULLET-HEIGHT

## Functions

You will need to decide what information each function takes in. 

* `enemy-turn-right-edge?`
* `enemy-turn-left-edge?`
* `bullet-hit-enemy?` 
* `enemy-hit-turret?`
* `bullet-on-screen?`
* `game-over?`

## Examples are required

Write examples with actual coordinate numbers before you write the functions! 

One in-class example was:
```text
WIDTH = 300
ENEMY-WIDTH = 50
x = 270
dir = +1
(check-expect (enemy-right-edge? x dir) true)
```

