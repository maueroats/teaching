---
title: "12. Two Dimensional Arrays"
date: 2018-01-16T10:11:37-06:00
draft: false
#type: slide
#theme: white
description: "Two dimensional arrays can represent temperatures across the states, locations of buildings, or hospital X-rays."
---

## Fundamentals

```java
int[][] data = new int[30][60];
int rows = data.length;
int cols = data[0].length;

import java.util.Arrays;
int[][] given = {{1,2},{3,4},{5,6}};
System.out.println(Arrays.deepToString(given));
```

## Exercises

1. Write the `makeBoard` function that creates a matrix of ones surrounded by a moat of zeros. 

        public static int[][] makeBoard(int rows, int cols);

        int[][] result = makeBoard(5,7);
        System.out.println(Arrays.deepToString(result); 
        /*
        0 0 0 0 0 0 0
        0 1 1 1 1 1 0
        0 1 1 1 1 1 0
        0 1 1 1 1 1 0
        0 0 0 0 0 0 0
        */

2. Make `boxSplit`, which takes in a 1D array of integers 
of even length and splits it into two rows (in "row major order").
     
        public static int[][] boxSplit(int[] data);
         
        int[] data = {10,20,40,80,120,160};
        int[][] result = boxSplit(data); 
        /* result == {{10,20,40},
                      {80,120,160}} */

3. Make the `boxSplitV`, which takes in a one dimensional array of integers of even length and splits it into two rows, but distributes the values in "column major order".

        public static int[][] boxSplitV(int[] data);

        int[] data = {10,20,40,80,120,160};
        int[][] result = boxSplitV(data); 
        /* result == {{10,40,120},
                      {20,80,160}} */


4. The `colMax` function takes in a (nonempty, rectangular) 2D array of data and returns a 1D array containing the maximum value from each column of the array.

        public static int[] colMax(int[][] data);

        int[][] data = {{-50, 100, 40},
                        {-30,   0, 90},
                        {-40,  95, 30}};
        int[] result = colMax(data);
        System.out.println(Arrays.toString(result));
        // {-50,100,90}

## More Links

* [Array 2D intro and Practice slides](https://docs.google.com/presentation/d/1QEp4FGMU1ShqXnAAwZ2gDNfMQqL6rmHUkAVeGWsszeU/edit?usp=sharing)

