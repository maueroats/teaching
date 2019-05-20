---
title: "Checkers Model"
date: 2019-05-20T10:01:45-05:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Illustrations from class discussion listing situations that should happen in the game."
---

This is the written record of an analysis. You should practice doing
your own analysis of a game, not just copying this one.

{{% figure src="checkers-planning-1.png" %}}

{{% figure src="checkers-planning-2.png" %}}

## Board Coordinates

We considered human-friendly coordinates, like (1,3) as well as
computer-friendly coordinates like (75, 225). Using computer
coordinates would make it easier to write the draw-handler, but
writing checks would be easier with human coordinates. We chose human
coordinates because checks are important to write.

## Piece Structure

* `p`: Posn
* `c`: Player (Integer)
* `king?`: Boolean

## Model

We discussed this much of the model:

* `turn`: Player (Integer)
* `ps`: (Listof Piece)

We still need to discuss the mechanics of moving pieces during a
player's turn, so there will be a little more to put in the model.

