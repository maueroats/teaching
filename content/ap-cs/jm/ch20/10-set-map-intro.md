---
title: "20. Set Map Intro"
date: 2018-05-22T08:53:38-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "Introduction to set and map."
---

See the [Java Methods Chapter 20 Powerpoint](http://www.skylit.com/javamethods2/ppt/Ch20.ppt) for a discussion. 

## Hashing vs Trees

When dealing with Sets and Maps one needs to find a value quickly. There are two main ways storing the data: hashing and using a tree. 

### Hashing

Hashing gives you a "random-ish" number to associate with the thing you are storing. The number is always the same, so you can store the object at the location given by the number and look in that location (with no searching) later when you want to find the object. The drawback is that hashing does not keep the objects in any kind of order.

**Advantage of hashing**: constant time access.

**Requirements to use a hash**: none; all Java objects have a built-in hash function. (If your object changes the default notion of equality, like you define your own `compareTo` method, you should learn how to change the hash function or avoid hashes.)

One simplified example is to take integers and use the remainder after dividing by a medium-sized prime (like 173). This lets someone use an array of length 173 to store numbers that may be much larger:

{{< highlight java >}}
{
  int [] data = new int[173];
  for (int k=0; k<30; k++) {
    int num = (int)(Math.random()*100000);
    data[num%173] = num
  }
}
{{< /highlight >}}

With that code it is very fast to find if a number is in the array. (Just check to see if `data[newnum%173] == newnum`.)

Dividing by a prime means smaller numbers will not be able to have short cycles - as a non-example, think what happens with the multiples of 16 when you divide by 128 (which is not prime). The "hashes" of the multiples of 16 would be 16, 32, 64, 80, 96, 112, 0, and then repeat.

### Tree

A binary tree records "smaller", "bigger", or "equal to" by offering a number and two choices at each step of the tree. Searching a tree for your object takes about log(N) steps, where N is the number of objects stored in the tree so far. This is slower than a hash function, and requires the objects to be ordered, but it keeps them in order - which can be very useful.

**Advantage of tree**: items are kept in order. 

**Requirements to use a tree**: items have to be `Comparable` to use a `Tree`.

## Set

The interface `Set` represents a mathematical set. Implementing classes include `HashSet` and `TreeSet`. Sets can answer the question "is this item in the set?" using the `contains` method. That's really all a set can do.

## Map

The interface `Map` represents a mathematical function. The inputs to the function are called "keys" and the outputs of the function are called "values". Implementing classes include `HashMap` and `TreeMap`. 
A map can answer the question "when I put this item in, what value comes out?" by using the `get` method. There is no `set` method, but you can change the output value by using `put(key, newValue)`.

