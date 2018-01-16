---
title: "12. Arrays"
date: 2018-01-10T10:44:21-06:00
draft: false
#type: slide
#theme: white
---

The fundamentals:

* Create (make space for) an array:

```java
int[] data = new int[50];
String[] names = { "Justyn", "Connor", "Leo", "Ellie" };
```
* Arrays in Java do not grow or shrink. There is no `+=` for arrays.
* The length of the `data` array is `data.length`. 
* Arrays without `new` have no space created for them.

```java
int[] nums;
int len = nums.length; // error, array is not made at all!!
nums[0] = -1; // error, certainly no item 0
```
* Getting values from an array:

```java
int first = data[0];
int last = data[data.length - 1];
```
* Setting values in an array:

```java
data[0] = 10;
data[1] = 50;
```
* Miscellaneous
    + Arrays are handled like Java Objects in memory. The name of the array is a reference to a block of memory where the array data is stored.
    + You cannot use the `{10,30,90}` form of the initializer anywhere except the declaration of the object.

      ```java
int[] nums = {10,30,90}; // OK
int[] bad;
bad = {10,30,90}; // ERROR
```



## Resources

If you missed class, you will want to read Chapter 12 and/or the [Java Arrays Tutorial](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html).

## Homework

* 2018-01-10: CodingBat [Array-1](http://codingbat.com/java/Array-1) exercises in class. Complete 5 or more; enough so you are comfortable with the basics - getting items from the start and end of an array, changing values, making new arrays.

* 2018-01-12: CodingBat [Array-2](http://codingbat.com/java/Array-2) exercises all day. You should have completed 8 already. Do 12 more before class Tuesday 2018-01-16.

* 2018-01-16: [Class JavaMethods GitHub](https://github.com/2017-2018-wy-ap-cs/java-rotary-phone.git) - Chomp is Chapter 12.
