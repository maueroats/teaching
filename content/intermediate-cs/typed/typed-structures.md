---
title: "Typed Structures"
date: 2019-05-06T14:21:12-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Using define-struct in Typed Racket. Additional info on struct-copy and limit for use with make-color."
---

## Defining new structures

A new structure need type information just like a function. There are
also some incantations you will want to use.

* `#:transparent` - Always include this.
* `#:type-name` - Usually include, should be name of struct with a
  capital letter at the start.

Example:

    (define-struct ship ([ name : String ]
                         [ pos : (Listof Posn) ])
                        #:transparent
                        #:type-name Ship)

## Copying Structures

Racket has a method called
[struct-copy](https://docs.racket-lang.org/reference/struct-copy.html?q=struct-copy#%28form._%28%28lib._racket%2Fprivate%2Fbase..rkt%29._struct-copy%29%29)
for copying a structure and changing some of the entries. 

     (struct-copy STRUCT-NAME VARIABLE [field NEW-VALUE])

Example:

    (define a-ship1 (make-ship "Dingy" (list (make-posn 5 2))))
    (define a-ship2 (struct-copy ship a-ship1 [name "Sailboat"]))

## Colors

It can be tricky to write the limit function that restricts a number
to the range 0 to 255 for use in a color.

    (define (limit [n : Integer])
      : Byte
      (min 255 (max 0 n)))

If you need to handle real number inputs, add in `(round (inexact->exact n))`.

