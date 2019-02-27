---
title: "22a. Recursion Practice 5"
date: 2019-02-26T17:17:20-06:00
weight: 96
draft: false
#type: slide
#theme: white
description: "count-w, powers of 7, double zero"
---

{{% use-mathjax %}}

1. (`count-w`) Find how many "w" letters there are in a
   word. Signature: `count-w: string -> number`.

2. (`p7`) Find the smallest power of 7 that is at least a given
   number. (So find the smallest $k$ so that $7^k \ge \text{number}$.)
   Signature: `p7: number -> number`.
   
        (check-expect (p7 1) 0)
        (check-expect (p7 7) 1)
        (check-expect (p7 8) 2)
        (check-expect (p7 49) 2)
        (check-expect (p7 50) 3)

3. (`eyeball`) Find how many pairs of consecutive zeros there are in a
   number. Signature: `eyeball: number -> number`. 
   
        (check-expect (eyeball 0) 0)
        (check-expect (eyeball 00) 0)
        (check-expect (eyeball 1007008) 2)
        (check-expect (eyeball 30008) 3)

    Explanations: the number 00 is really just 0, so there is only one
    zero. The number 30008 has two pairs of consecutive zeros: 3 **00**
    08 and 30 **00** 8.
