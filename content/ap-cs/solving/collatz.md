---
title: "Collatz"
date: 2019-03-28T19:02:46-05:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Collatz sequence - maximum length in a range."
---

The [Collatz sequence](https://en.wikipedia.org/wiki/Collatz_sequence)
is a sequence of positive integers. The term after value=n is:

* value = n/2 if n is even
* value = 3*n+1 if n is odd

Example: 5 -> 16 -> 8 -> 4 -> 2 -> 1.

Source: [Project Euler Problem 14](https://projecteuler.net/problem=14).

## Problem Statement

Find the number n < 1,000,000 that gives the longest chain (before
hitting one).

{{% notice warning %}}
Test your code: print out the entire sequence of numbers beginning with
n=161439. Make sure you get about 230 numbers, ending in a 1.
{{% /notice %}}

**Suggestion**:
Insert code to check for an impossible condition, say n<1 in your
sequence generating function.
