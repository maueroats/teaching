---
title: "Avoid Aardvark"
date: 2018-02-06T10:31:58-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

[Google Presentation with all of the ArrayList in-class problems](https://docs.google.com/presentation/d/1gLoI2KTCvALpSvW26gLePK7NVkqIe84Aq9lgYkWqL24/edit?usp=sharing)

* ArrayList 5, page 12
```java
public static void avoidAardvarks (ArrayList<String> data)
```

## Testing

+ Include the [boilerplate]({{% relref "testing-intro.md" %}}).

        import org.junit.*;
        import org.junit.runner.*;
        import static org.junit.Assert.*;

+ See code at the end of the presentation (linked above) if you prefer not to just "add" to  results.
+ Recall: `@Before` and `@Test` must appear before _functions_, not statements.
+ Testing `ArrayList` is simplest if you use the `toArray()` method and `assertArrayEquals`.

```java
@Test
public void simple_1() {
    ArrayList<String> correct = new ArrayList<>();
    correct.add("yes");
    
    ArrayList<String> data = new ArrayList<>();
    data.add("not");
    data.add("yet");

    change(data);
    
    assertArrayEquals(correct.toArray(), data.toArray());
}
```

