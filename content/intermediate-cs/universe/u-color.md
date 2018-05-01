---
title: "Universe Color"
date: 2018-04-30T11:11:58-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Change the color on all of the clients by hitting a key."
---

We will make a client that knows "its own color" and the color that is showing on the screen. When a key is hit, the client sends its own color to the server. When a client receives a color message, it changes the color that is showing on the screen to that color. This means that hitting a key will change the color on everyone's screen to your color.

## Model and Message Structure

The model needs two colors, one to remember as "your color" and the
other to show on the screen.

There will only be one kind of message, the color.

## Process

Review the [universe overview]({{% relref "u-overview" %}}).

* Define the structure.
* Make two examples, one which has "your color" blue and is showing orange, the other which has "your color" blue and is showing blue.
* Write and test the draw handler.
* Design and test the message handler (`on-receive`).
* Design and test the key handler.

## Code

* [Server](generic-server-v1.rkt). You do not need to understand this code now.
* [Color changing client from period 1](color-client.rkt)


