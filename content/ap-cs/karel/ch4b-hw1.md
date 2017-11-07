---
title: "4.6: PrettyBoxBot"
date: 2017-11-07T10:27:49-06:00
draft: false
#type: slide
#theme: white
---

A `PrettyBoxBot` makes a square box on the screen. In order to let a person easily configure it without learning how to design new robots, the PrettyBoxBot accepts two strategies in its constructor.

* Side laying strategy: controls how long the side is
* Corner beautifying strategy: controls how many beepers get put on a corner.

Putting lots of beepers on the corners of a box makes it more beautiful in robot-land.

The PrettyBoxBot itself should have some abilities that help make the box:

* `putAndGo()`: Build a single unit of the box wall.
* `makeBox()`: Build the entire box.

In the `PrettyBoxBot` constructor you will want to accept the side laying and corner beautifying strategies and remember them.

As usual, there is sample code from our discussion on the [class GitHub](https://github.com/2017-2018-wy-ap-cs/apcs-karel) in the `karelCh4.drjava` project.

