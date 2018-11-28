---
title: "Number Model Review II"
date: 2018-11-28T07:25:03-06:00
weight: 60
draft: false
#type: slide
#theme: white
description: "Review with focus on graphing functions."
---

Definitions: people coordinates are coordinates where (0,0) refers to
the origin where the axes cross and positive y numbers are above the
x-axis. Computer coordinates have (0,0) in the upper left corner and
positive y means "down".

1. You are making a viewing window that ranges from x=-300 to x=500 and
from y=-200 to y=600.

     1. Write three check-expects for the function `x-people`, which takes in a computer x-coordinate and produces a "people" x-coordinate.

     2. Write three check-expects for the function `y-computer`, which takes in a people y-coordinate and produces a "computer" y-coordinate.

     3. Write the functions `x-people` and `y-computer`. Make sure
     they pass your tests
     
     4. Write `x-computer` and `y-people` just in case you need them...

     4. Make a model t goes from 0 to 314 repeatedly. Animation:

            x-people = 250*cos(t / 100)
            y-people = 150*sin(t / 100)


