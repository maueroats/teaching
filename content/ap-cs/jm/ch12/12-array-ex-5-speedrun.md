---
title: "12. Array Speedrun"
date: 2019-01-10T09:41:00-06:00
weight: 60
draft: false
#type: slide
#theme: white
describe: "A two dimensional array making exercise."
---

Make create a two dimensional array of a given width and height filled
in a snake pattern with 0 and 1 as described below.

The snake pattern starts with a 1, then has longer and longer
sequences of zeros separated by ones: 0 zeros, one, 1 zero, one, 2
zeroes, one, 3 zeroes, one, etc.

    11010010001000010000010000001

The array is filled in by rows, first going to the right, then going
to the left, in the pattern shown by these "ascii arrows":

    --1-->>
    <<--2--
    --3-->>
    <<--4--
    --5-->>

The filled in result of `snakeSpeedrun(6,5)` would be:

     110100
     010001
     000100
     001000
     000010
     
You write the function:
`public static int[] snakeSpeedrun(int width, int height)`
