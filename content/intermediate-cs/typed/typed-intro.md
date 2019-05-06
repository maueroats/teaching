---
title: "Typed Intro"
date: 2019-05-06T07:20:10-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "All of the basics you need to start using Typed Racket."
---

In order

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

3. End of the file - you need to run the check-expects manually.

        (test)
        
