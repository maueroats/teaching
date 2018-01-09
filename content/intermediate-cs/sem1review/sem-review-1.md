---
title: "Semester I Review 1"
date: 2018-01-08T08:49:18-06:00
draft: false
description: "Random shape. Drift to a new position. Reduce the amount of green." 
---

## Day 1 

1. **Random shape**. Write a function that returns a square, circle, or triangle. All should be equally likely.
```text
random-shape: ignore -> image
```

2. **Drift**. A smiley face starts at some position on the screen. It randomly drifts 5 pixels in some direction (up, down, left, or right) every 0.2 seconds. Write the function that gives its new position.
```text
drift-to-new: posn(old) -> posn(new)
```

3. **Reduce green**. Write a function `less-green` that reduces the amount of green in a color by 25%.
```text
less-green: color -> color
```

## Day 2

1. Random dots on a circle. Create an animation of a dot moving to one of six random locations on a circle. Ideally the locations will be equally spaced. 

    Advanced: use the x coordinate of the location to control the amount of red, and the y coordinate to control the amount of green.

2. **Purify color**. Given a color name, decide which component has the greatest color value and return it. In the case of a tie you can choose any of the tied values.
```text
purify-color: string(color-name) -> string("red" "green" or "blue")
```

3. **Peace symbol**. Write a function to create the image below. Then make an animation that lets you control the size of the image (e.g., right and left arrow keys).

{{% figure src="peace.png" %}}


## Extra

* **Dotted Pentagon**. The `dotted-pentagon` function puts a colored
   dot on one of the five vertices of a regular pentagon. Challenge: the color of the dot is red, but fades...
   
   
   
