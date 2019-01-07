---
title: "12. Arrays Exercises 3"
date: 2019-01-07T11:11:07-06:00
weight: 50
draft: false
#type: slide
#theme: white
description: "Exercises to bring back to your mind basic facts about arrays."
---

## Compactor

Given an array of integers `nums`, return an array containing only the
indices `k` for which `nums[k]` is one.

Example: `compactor({1,0,1,1}) => {0,2,3}`.

Example:

    {//               0 1 2 3 4 5 6 7
        int[] nums = {0,0,1,0,1,0,0,1};
        int[] cpct = compactor(nums);
        int[] expected = {2,4,7};
    }

## Prime Number Sieve

Write a function `public static int[] primeSieve (int n)` that returns
an array of length n with a 1 in index k when k is a prime number, and
0 otherwise.

Use some [tester code](PrimeSieve.java) to show the results of your
function.

Recommended process:

1. Mark every number that is at least two as prime. Run your function
   and make sure that at this stage `primeSieve(10)` gives
   `{0,0,1,1,1,1,1,1,1,1}`. 
   
2. Change every multiple of 2 to a zero. At this stage,
   `primeSieve(10)` should give `{0,0,1,1,0,1,0,1,0,1}`.

3. Automate the process of giving multiples a value of zero for every
   other number. 
   
## Prime Factorization

Use the tools you have to write a program to find the prime
factorization of a number. It is OK to limit your program to working
with numbers with less than 20 factors.

Signature: `public static int[] pf (int n)`.

Examples:

* `pf(8) => {2,2,2}`
* `pf(18) => {2,3,3}`

