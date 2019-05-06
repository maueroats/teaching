---
title: "Store"
date: 2019-05-03T11:31:26-05:00
weight: 110
draft: false
#type: slide
#theme: white
description: "A store where you can buy items and get charged for them."
---

* Offer choices with prices
* Ask what they want
* "I don't have that" if you do not recognize the item.
* "quit" = stop asking.
* Print what they have purchased so far.

## Template

    want = "get started"
    while want != "quit":
        want = input("What do you want to buy?")
        if want == "avocado":
            money -= price
            avocado += 1
        elif ...:

