---
title: "Primes"
date: 2019-03-28T19:02:50-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Create a class to hold prime numbers. Use it to solve some prime-using problems."
---

Create a class `PrimeNumbers`. It should have:

* an `boolean isPrime(int n)` function to determine if a number is prime
* a `int get(int k)` function to return the k-th prime, starting with
  `get(0)` returning `2`.

You can make these (and everything else inside the `PrimeNumbers`
class) static, but that makes it complicated to initialize the prime
list in phase two, so I decided not to do that.

The class looks like this:

    public class PrimeNumbers {
	  public boolean isPrime(int n);
	  public int get(int index); // prime#0 is 2
    }

Usage:

    PrimeNumbers pnums = new PrimeNumbers();
	System.out.println(pnums.isPrime(17));
	System.out.println(pnums.isPrime(21));

## Phase One: Basic Interface

1. Just use an array to hold a fixed number of primes at the start,
   and make a `get` method that just returns a value from that array.

        private static int[] primes = {2,3,5,7,11,13,17,19,23,27};
		
2. Review the discussion from in class and write an efficient
   `isPrime` method that checks only prime numbers up to the square
   root of the number being tested.

3. Test your `isPrime` method using [JUnit testing]({{% relref
   "ap-cs/testing" %}}).
   
## Phase Two: Improvements

We will see the benefit of "information hiding" when we change our
code to compute more prime numbers when they are needed.
We are going to change the fixed-length list of primes into an 
ArrayList that grows automatically, and then change the get method to
automatically find new primes as needed.

* Make an `ArrayList<Integer>` instance variable to hold the prime
  numbers. Put `2` in it initially. (What part of the class should do this?)

* Write a `public int nextPrime()` method that finds the next prime number after
  the last one in the list, and adds it to the list. (Why should this
  method actually be private?) 

* Test the `nextPrime()` method using JUnit. 

* Modify the `get(int index)` method so that it will generate more primes
  automatically if asked for a prime number index greater than or
  equal to the size of the list.

  
## Phase 3: Use It

1. Find the 10,001st prime number.
2. Find the largest prime factor of 88,762,035,289L.
3. How about 4,395,275,946,425,798,569L?
