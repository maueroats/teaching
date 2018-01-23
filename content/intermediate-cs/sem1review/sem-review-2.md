---
title: "I.2 Semester I Review 2"
date: 2018-01-09T15:08:52-06:00
draft: false
weight: 20
#type: slide
#theme: white
description: "Random dots located on a circle, purify color, Benz symbol."
---

1. Random dots on a circle. Create an animation of a dot moving to one of six random locations on a circle. Ideally the locations will be equally spaced. 

    Advanced: use the x coordinate of the location to control the amount of red, and the y coordinate to control the amount of green.
    
    [Solution to basic](circle-6dots.rkt).

2. **Purify color**. Given a color name, decide which component has the greatest color value and return it. In the case of a tie you can choose any of the tied values.
```text
purify-color: string(color-name) -> string("red" "green" or "blue")
```

3. **Cheap Benz symbol**. Write a function to create the image below. Then make an animation that lets you control the size of the image (e.g., right and left arrow keys).

{{% figure src="benz.png" %}}


## Extra

* **Dotted Pentagon**. The `dotted-pentagon` function puts a colored
   dot on one of the five vertices of a regular pentagon. Challenge: the color of the dot is red, but fades...
   
   
   
