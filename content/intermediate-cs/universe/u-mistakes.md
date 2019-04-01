---
title: "Universe Mistakes"
date: 2018-05-09T10:38:49-05:00
weight: 80
draft: false
#type: slide
#theme: white
description: "A list of common mistakes made when writing universe animations."
---

* A `package` must have the entire model as its first argument. You can't put part of the model in the first argument and another part in the second argument (where the message goes). 

* Do not write recursive functions that take a `model` as an input.
It is a bad idea. Your code gets more complicated and there is no benefit.
Instead, write a helper function that takes in the list part of the model
(along with any other needed information).

## Advice

* Send only the minimum amount of information that needs to be sent.

* Split actions between local key/mouse/tick handlers and the receive handler.

    - changes affecting only one world's model should be
  done in a key or mouse handler (or the first argument of
  `make-package`)
  
    - changes in every world's model should be done in the receive
      handler
      
