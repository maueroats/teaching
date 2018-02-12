---
title: "14. Comparable"
date: 2018-02-12T11:49:54-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

Comparable means that two items in a class can be compared (less than,
equal to, greater than). It is similar to the `Ord` typeclass in Haskell.

Comparable is an interface. You implement it.  It is a template, so
you put the class you are able to compare to in angle brackets
afterwards. I expect this to be the same class as the one that is
implementing the `Comparable` interface.

    public class Whatever implements Comparable<Thing> { 
        public int compareTo (Thing other) {
            // ...
        }
    }

The `compareTo` function gives an integer that indicates whether
`this` is greater than `other`. 

* negative means `this < other`. This could be read "this comes before other".
* zero means `this = other`
* positive means `this > other`

| a | b | a.compareTo(b) | meaning | inquality |
|---|---|----------------|---------|-----------|
|10 | 20|      -10       | a is before b | < |
|30 | 17|       13       | a is after b  | > |
|20 | 20|        0       | a is the same as b   | = |
|"can" | "ask"  | 2       | a is after b   | > |
|"dang"| "ghost"| -3      | a is before b  | < |
|"bo" | "boat"  | -1      | a is before b  | < |
|"same"| "same" | 0       | a is the same as b   | = |

{{% notice note %}}
The `Comparable` interface does not require any particular number be returned from the `compareTo` function. Any positive result indicates that the left (`this`) argument is greater than the right (`other`) argument.
{{% /notice %}}


## Exercises

1. The `Drow` class holds a `String`, but when you compare two `Drow`
   instances you get the opposite answer from comparing two strings. Example: 

        Drow a = new Drow("cat");
        Drow b = new Drow("dog");
        int cmp = a.compareTo(b);
        // cmp is positive, but would be negative for Strings
    
    Write the `Drow` class, including any instance variables,
    constructor, and `compareTo` method.
     

2. **EBO**. The class `EBO` is like `Integer` except all evens appear
   before any odd number in the ordering created by `compareTo`.
   
     Examples:
     
    | a | b | a.compareTo(b) | a _interpretation_ b |
    |---|---|--------------|----------------------|
    |2|4| -2           | is before |
    |9|3| 6            | is after |
    |2|9| -7           | is before |
    |2|-3| -1 (any neg)| is before |
    |3|8| +1 (any pos) | is after |
    |5|10| +1 (any pos) | is after |

      The constructor is of the form `new EBO(7)`.


3. The class `Pt` contains an `(x,y)` coordinate pair. The ordering of `Pt` is given by first comparing the x's and then, if they are equal, comparing the y's.

    Examples:

    | a | b | a.compareTo(b) | a _interpretation_ b |
    |---|---|--------------|----------------------|
    |(20,50)|(20,80)| -30              | is before |
    |(10,5)|(10,2)| 3 |is after |
    (10,30)|(31,19)| -21 | is before
    
    Write a class header, instance variables, constructor, and `compareTo` method.
        
