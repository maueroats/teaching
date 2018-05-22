---
title: "P1. Jackpot"
date: 2018-05-21T11:47:02-05:00
weight: 10
draft: false
#type: slide
#theme: white
---

Give each world an id number (1, 2, 3, ...).
The worlds are all lined up according to their id number.
Every world has some money.  When a "jackpot" happens, the money from
one world is distributed to its neighbors (each gets half).

Consider the first world to be the neighbor of the last world, so half of the money from world 1 would go to world 4 in the example below.

Once the world distributes its money, it has no money left.

Write down your **model**, **message**, and **reaction** to the
message in detail before programming.

{{% figure src="jackpot.jpg" %}}
