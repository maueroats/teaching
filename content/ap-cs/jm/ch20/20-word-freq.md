---
title: "20. Frequency Analysis"
date: 2018-05-22T09:31:46-05:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Find the most frequent words in a text document."
---

In this assignment, we will find the most frequent words in Jane Austen's [Sense and Sensibility](https://www.gutenberg.org/ebooks/21839). 

Your goal is to print the top 100 most frequent words and their frequency count. Your method should be fast and flexible so that you can handle longer documents and more or less than the top 100.

1. Read the information in the file using `File` and `Scanner`.
2. Clean up the information by removing non-word characters. Make everything lowercase for consistency. This step is surprisingly tricky to get perfect. I recommend `replaceAll` using the [regular expression](http://www.vogella.com/tutorials/JavaRegularExpressions/article.html) `"\\W+"` to match at least one non-word character. See a handy [cheat sheet](https://zeroturnaround.com/rebellabs/java-regular-expressions-cheat-sheet/) ([pdf](http://files.zeroturnaround.com/pdf/zt_regular-expressions-cheat-sheet.pdf)) for more information. 
3. Create a `Map` to count each word and their frequency. 
4. Create your own custom `WordCount` class that will hold one word and its frequency together.
    1. Constructor
    2. Write a `toString` method.
    3. Write a `compareTo` method and implement the `Comparable` interface. This should be written so that the highest frequency comes first.
5. Make a `TreeSet` with the `WordCount` class using the data from the file.
6. Print the top 100 most frequent words in your `TreeSet`.
