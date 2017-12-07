---
title: "3. Objects and Classes"
date: 2017-12-04T09:00:52-06:00
draft: false
#type: slide
#theme: white
weight: 30
---

* Day 1: read 3.1, skim 3.2 - read boldface, 3.3.
* Day 2: read 3.5-end.
* Day 3: [Writing Simple Classes II](https://docs.google.com/document/d/1Uj4zGqRIpJBNXfSBTPbO2vZC70mog_gD_tS3U-KJmSc/edit?usp=sharing).
* Day 4: [Writing Simple Classes III](https://docs.google.com/document/d/1Uj4zGqRIpJBNXfSBTPbO2vZC70mog_gD_tS3U-KJmSc/edit?usp=sharing).
* Statements and solution in the [new github repository](https://github.com/2017-2018-wy-ap-cs/java-rotary-phone).

```shell
git clone https://github.com/2017-2018-wy-ap-cs/java-rotary-phone
```

## Reading Questions

1. What does CRC stand for in the phrase "I wrote a CRC card for SuperBot"? 

### Classes (3.3)

2. What is a **class**, according to Java Methods?

3. What is the difference between a class and an object? Give two examples not from the text.

4. Are there any rules in Java governing the name of a file containing `DinosaurBot`? If so, what?
 
5. Does Java force you to name your classes beginning with capital letters?
Explain the context of this question.

6. What is an instance variable? How does it compare to a field?

7. What vocabulary word is used for behaviors of a class?

8. Give an example of an "implicit" field, constructor, or method. (Appears later in the chapter.)

9. If you refuse to use import statements, does that mean you cannot access information from other files, like the Color class? Explain.

10. Does Java care what order methods and fields appear in a class?

11. What conventions do Java programmers use when ordering the things that 
they put in a class?

12. Is it considered good design to put the `main` method inside your `WorkerBot` class? What do the Java Methods authors say? Why do you think they say that?

### Gridworld (3.4)

### Fields, Constructors, Methods (3.5)

13. Is it an error to have two constructors: `public Bug()` and `public Bug(Color c)`? If not, how do you determine which one is used?

13. What is a "reference" (intuitively)?

14. What is garbage collection?

15. Is it possible for a class to have no constructors? How? Or why not?
 
16. What does it mean to "send a message" to an object in Java (metaphorically speaking)?

17. Does a method belong to an object or a class? Explain briefly.

18. How do you indicate that a method gives no result?

19. There is a technique mentioned called either _encapsulation_ or _information hiding_. What is one way to implement encapsulation?

20. What is one advantage of encapsulation? (One of the three mentioned in the book is more important than the other two - try to pick that one.)

### Inheritance (3.6)

21. Why might adding methods to an existing class not be "feasible or desirable"? (Three reasons.)
     - Reason 1:
     - Reason 2:
     - Reason 3:

22. What is inherited from a superclass? What is not?

23. Is it possible to make a class that does not inherit from any other class? Explain. 

24. `Bug` is on page 52, `UTurnBug` is on page 65. Why can't `UTurnBug` just have `turnAround()` function that is `direction += 180`?

25. What are accessor methods? 


