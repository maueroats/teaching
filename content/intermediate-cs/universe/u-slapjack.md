---
title: "Universe Slapjack"
date: 2018-05-16T14:57:00-05:00
weight: 70
draft: false
#type: slide
#theme: white
description: "Once the screen shows green, hit a key fast and get a point."
---

A bunch of players connect to the server. (One player per window.) The
screen is yellow for a random amount of time (say 1-10 seconds). When
the screen turns green, the first window to hit a key gets a
point. The others are locked out until the next time the screen turns green.

* Show points on screen.
* Any key hit in a window scores for that window.
* Only one point per green screen.
* No points can be earned when the screen is yellow.

## Planning

* Model
* Message(s)
* What will happen when the message is received?

## Images

The grey background and the line are not part of the animation; they just separate the active worlds.

{{% figure src="slapjack-green.png" title="Ready to score" %}}
{{% figure src="slapjack-yellow.png" title="Waiting, cannot score" %}}


## Hints

* Show the time remaining until someone can score again. (The color gray is unobtrusive.)
