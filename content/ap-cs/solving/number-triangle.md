---
title: "Number Triangle"
date: 2019-03-18T15:32:57-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "The the maximum possible sum of a path in a number triangle, from the top row to the bottom row."
---

1. Create a function to read a file full of numbers into an array
   (`int [][]nums`), one row of numbers from the file becomes one row
   of numbers in the array. It is OK to just have an input be how many rows are
   in the triangle. Signature: 
       
        public static int[][] readNums(int rows, Scanner s)

2. Create a function to write a triangle of numbers into a
   file.

        public static void triwrite (int rows, PrintWriter p)
   

3. Find the maximum possible sum along any path that goes down or down
   and right from the top to the bottom row of your triangle. 
   
            1
            1 20
            1 2  30
            1 3  4  50
        10000 5  6  7  8
        
    One possible path is 1, 20, 3, 4, 5, 7, for a total of 40. Another
    possible path is 1,1,1,1,10000 for a total of 10004. 


## References

* Project Euler [Problem 18](https://projecteuler.net/problem=18)
* [PrintWriter](https://docs.oracle.com/javase/8/docs/api/java/io/PrintWriter.html)
* [Scanner](https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html)
* [File](https://docs.oracle.com/javase/7/docs/api/java/io/File.html)


