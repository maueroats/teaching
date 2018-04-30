---
title: "Universe Overview"
date: 2018-04-30T09:22:06-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "Overview of the Universe."
---

* `(make-package model message)`: Returned from a handler to update the model and send a message.
* Any handler (for example: `key`,`mouse`,`tick`) can return a `package`, which updates your own model and sends a message to the server. 
* New handler: `on-receive`. 

        receive-h: model message -> model

    Update your model based on a message you receive from the server.

Reading the Racket Documentation:

* `model` is called `WorldState`
* `HandlerResult` means either a model or a `package`.

## Miscellaneous

* The `on-receive` handler can return a `package` if needed.

## Code

[Generic server](generic-server-v1.rkt)

