---
title: "Typed Intro"
date: 2019-05-06T07:20:10-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "All of the basics you need to start using Typed Racket."
---


## Initial Setup

1. One time per computer:

    File -> "Install Package..." -> Enter "2htdp-typed" and choose the
    "Install" button.
    
2. Beginning of every file:

        #lang typed/racket
        (require typed/lang/posn)
        (require typed/2htdp/image)
        (require typed/2htdp/universe)
        (require typed/test-engine/racket-tests)
        
## Defining new structures

A new structure need type information just like a function. There are
also some incantations you will want to use

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
                  
