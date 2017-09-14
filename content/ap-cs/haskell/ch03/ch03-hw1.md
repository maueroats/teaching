---
title: Chapter 3 Problem Set
date: 2017-09-14T10:00:00-05:00
tags:
 - haskell
 - homework
draft: false
---

The essentials of the Types and Typeclasses chapter are: writing type
signatures for functions, reading string inputs with the `Read` class,
and dealing with Integral to Fractional conversions when they are needed.
<!--more-->

1. FYI: You can explicitly say what type a number is by using two
   colons and the type you want - for example, (5::Int) or
   (5::Float). Find the types of each of the operations below, or say
   why it does not work:

    * (/)
    * (5::Int) / (10::Int)
	* (5::Int) / (10::Float)
	* (5::Float) / (10::Float)
	

2. Write a function to find the average of numbers in a list. This
   should bring up the difficulty that you cannot divide an integer by an integer(!).

3. Write a signature and function body for `add10Word` which reads an
   integer from a string and adds 10 to it.

4. Write a signature and function body for `numberInSentence`, which
   takes a number and returns the sentence "I have ___ eggs."

5. Write a signature and function body for `doubleDebt` which takes a
   String and puts out a Float. The String contains a floating point
   number that represents how much money someone owes, and the Float output
   is twice that much.

6. Write a signature and function body for `sampleStdDev` that finds
   the [sample standard deviation]
   (https://en.wikipedia.org/wiki/Standard_deviation) of a list of
   (the right kind of) numbers. Check the type signature for square
   root ([`sqrt`](http://hoogle.haskell.org/?hoogle=sqrt&scope=set%3Ahaskell-platform))!

10. _Possibly Challenging_: Write the function `median` to find the
median of a list of items that can be ordered. (Use the type `Int`, if
you prefer.)

