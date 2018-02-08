---
title: "13. Shopping List"
date: 2018-02-07T09:13:59-06:00
weight: 20
draft: false
#type: slide
#theme: white
---

See the [ArrayList presentation](https://docs.google.com/presentation/d/1gLoI2KTCvALpSvW26gLePK7NVkqIe84Aq9lgYkWqL24/edit#slide=id.g7b177d99b_00), pages 9-11, exercise ArrayList 4/4a/4b.

The [setup code](ShoppingSetup.java) is to provide you with a sample shopping list to use in your tests.

Testing suggestion:

```java
@Test
public void test_example() {
  ArrayList<Integer> n = new ArrayList<>();
  n.add(5); n.add(25); n.add(100);

  List<Integer> correct = Arrays.asList(5,25,100);
   
  assertEquals(correct, n);
} 
```
