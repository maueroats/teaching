---
title: "Universe Overview"
date: 2018-04-30T09:22:06-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "Overview of the Universe."
---
Universe gives a way to have multiple big-bangs communicate.

Each big-bang is individually called a "world". They are also called "clients". There is one "universe" running, which is the "server". The universe server coordinates all of the communication between the big-bang clients.

There are some new technical additions to `big-bang`, and some recommendations for the design process.

## Technical Information

* `(make-package model message)`: Returned from a handler to update the model and send a message.
* Any handler (for example: `key`,`mouse`,`tick`) can return a `package`, which updates your own model and sends a message to the server. 
* New handler: `on-receive`. 

        receive-h: model message -> model

    Update your model based on a message you receive from the server.

Reading the Racket Documentation:

* `model` is called `WorldState`
* `HandlerResult` means either a model or a `package`.

## Design Process

* Decide your **big-bang model** first. Use the usual process (draw
  scenes, write the model that goes with those scenes).
  
* Decide your **universe model** next. This means you need to decide
what **messages** will be sent between worlds (big-bangs).


## Miscellaneous

* The `on-receive` handler can return a `package` if needed.

## Code

[Generic server](generic-server-v1.rkt)

