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
<!--more-->

## Examples

Begin with pictures of all of the situations that can come up in the
game. 

Advanced: enthusiastic software designers may want to read about
how [user stories](https://www.alexandercowan.com/best-agile-user-story/)
used in actual software development.

<!-- page 2 of file:: gm convert FILE.pdf[1]  -crop 510x770+20+20 -->

{{% figure src="checkers-planning-1.png" %}}

{{% figure src="checkers-planning-2.png" %}}

## Board Coordinates

We considered human-friendly coordinates, like (1,4) as well as
computer-friendly coordinates like (75, 225). Using computer
coordinates would make it easier to write the draw-handler, but
writing checks would be easier with human coordinates. We chose human
coordinates because checks are important to write.

## Piece Structure

* `p`: Posn
* `c`: Player (Integer)
* `king?`: Boolean

## Model Structure

We discussed this much of the model:

* `turn`: Player (Integer)
* `ps`: (Listof Piece)

We still need to discuss the mechanics of moving pieces during a
player's turn, so there will be a little more to put in the model.

