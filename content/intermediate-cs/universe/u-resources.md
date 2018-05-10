---
title: "Universe Resources"
date: 2018-04-30T08:58:00-05:00
weight: 90
draft: false
#type: slide
#theme: white
description: "Reference material and tutorials on the Universe."
---

This page contains only the bare-bones information.

{{% alert success %}}
{{% attachments title="Racket Code" pattern=".*\.rkt$" /%}}
{{% /alert %}}

* Generic server (see attachment).
* `(make-package model message)` to update model and send a message.
* A main function `start-big-bang` to launch the windows.

        (define (start-big-bang my-name initial-model)
          (big-bang initial-model
            (on-draw draw-h)
            (on-receive receive-h)
            (on-key key-h)

            (register LOCALHOST)
            (name my-name)
            (close-on-stop true)))

* The `launch-many-worlds` command to quickly and easily start several windows.

        (launch-many-worlds
            (start-big-bang "whale" (make-model "blue" "gray"))
            (start-big-bang "squirrel" (make-model "red" "yellow")))

## Sending Posns 

You cannot send posns without a hack. The hack is to make a separate file that contains 
a little bit of lower level Racket code and require it. This code could go in your `posn-util.rkt` file!

        #lang racket
        (provide (all-defined-out))
        (define-struct posn (x y) #:prefab)

## Additional Resources

* [Universe in Racket Documentation](https://docs.racket-lang.org/teachpack/2htdpuniverse.html). See especially [Section 2.4.7, the examples](https://docs.racket-lang.org/teachpack/2htdpuniverse.html#%28part._universe-sample%29), where a ball-bouncing example is developed.

* [Universe tutorial by Sub](https://drive.google.com/drive/folders/0BypGcwjV5LOHSlF0ZmxQT0VnelU)

