---
title: "20. Posn Util"
date: 2017-12-14T08:09:55-06:00
draft: false
#type: slide
#theme: white
weight: 10
---

The functions in 20.5 are all useful later. When you do them, you should 
save them in a file called `posn-util.rkt`. (Please use that name.)

## Require and provide

The `provide` command makes functions available for other files to use.
One way to use it is to list all of the functions you want to allow
other files to use:
```racket
(provide add-posn sub-posn scale-posn distance)
```
Sometimes you just want to make every function in the file available. 
There is a shortcut to do that:
```racket
(provide (all-defined-out))
```

In order to use the functions in another file, you need to `require` that file.
You already know `(require picturing-programs)` but when we use require 
we need to give the whole filename.
```racket
(require "posn-util.rkt")
```
You need to save your work in the same folder as your "posn-util.rkt" file, since Racket only looks in the current folder for other files.

