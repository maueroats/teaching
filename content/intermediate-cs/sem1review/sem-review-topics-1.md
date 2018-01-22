---
title: "Semester Review Topics List"
date: 2018-01-21T23:01:04-06:00
draft: false
#type: slide
#theme: white
description: "Major topics missed on Chapter 20 test: randomness, consistent signatures for big-bang, good testing."
---

We have learned about randomness, writing consistent signatures for
big-bang, writing high quality tests, and how to limit numerical values.

## Recent major topics

* Randomness

    - Work with a non-random function first. 
        - Non-random function has more parameters than random version.
        - Testable.
    - Random function
        - Calls non-random function with random input.
        - Not usually tested.

* Signatures / Big-Bang

    - Information flow must be consistent
    - Write signatures for everything
    - Test everything individually
    - Use `check-with` to catch signature errors. (See below.)

* Numerical functions that limit or convert values:

    - `min`, `max` to limit values
    - `real->int`
    - `round`, `ceiling`, `floor`

* Testing

    - Write two tests for each function.
    - **Especially** when you do not know how to make it work! (Fight instinct to just hack.) 
    - Use different numbers for each argument in a test. (Why is this important?)
    
    
### Details on check-with

Example in `big-bang` is: `(check-with posn?)`. 
[More in click-circle writeup]({{< relref "click-circle.md" >}}).
The `check-with` command is first introduced in Chapter 8, book page 137, PDF page 148.

