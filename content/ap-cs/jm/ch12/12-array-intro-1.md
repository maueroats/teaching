---
title: "12. Array Basic Facts"
date: 2018-12-07T09:11:27-06:00
weight: 10
draft: false
#type: slide
#theme: white
description: "The basics of one dimensional arrays."
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
    
* Printing out an array.

    + At start of program: 

        ```java
        import java.util.*;
        ```

    + When you want to print an array, use `Arrays.toString`:
    
        ```java
        int[] e = {1,2,3};
        String ee = Arrays.toString(e);
        System.out.println(ee);
        ```


* Miscellaneous
    + Arrays are handled like Java Objects in memory. The name of the array is a reference to a block of memory where the array data is stored.
    + You cannot use the `{10,30,90}` form of the initializer anywhere except the declaration of the object.

        ```java
        int[] nums = {10,30,90}; // OK
        int[] bad;
        bad = {10,30,90}; // ERROR
        ```
    + In that case, you need to make a new (unnamed) array before you assign it:

        ```java
        int[] decent;
        decent = new int[]{10,30,90};
        ```
