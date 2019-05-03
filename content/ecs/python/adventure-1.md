---
title: "Adventure 1"
date: 2019-05-03T11:34:50-05:00
weight: 120
draft: false
#type: slide
#theme: white
description: "A simple adventure game with a sidewalk and a store."
---

There are at least two locations:

* Sidewalk:
On the sidewalk you have a 30% chance of finding $5.

* Store:
In the store you can buy a sandwich ($10) or a key ($5).

You win the game when you end up on the sidewalk with a sandwich and a
key.


## Using random numbers

    import random
    a = random.randint(1,100)
    if a <= 25:
        print("25% chance - you won")
    else:
        print("75% chance - you lost")
    
