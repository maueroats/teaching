---
title: "Typed Structures"
date: 2019-05-06T14:21:12-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Using define-struct in Typed Racket."
---

## Defining new structures

A new structure need type information just like a function. There are
also some incantations you will want to use.

* `#:transparent` - Always include this.
* `#:type-name` - Usually include, should be name of struct with a
  capital letter at the start.
* `#:constructor-name` - Usually want `make-STRUCT-NAME`.

Example:

    (define ship ([ name : String ]
                  [ pos : (Listof Posn) ])
                  #:transparent
                  #:type-name Ship
                  #:constructor-name make-ship)
                  
