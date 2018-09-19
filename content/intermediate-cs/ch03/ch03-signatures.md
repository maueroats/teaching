---
title: "Ch03 Signatures"
date: 2018-09-19T15:47:54-05:00
#weight: 
draft: false
# type: slide
# theme: white
---

* Practice writing signatures.
* Write examples as you go.
* We did these one at a time.

Write signatures for:

1. `overlay/align`
2. `text`
3. `ellipse`
4. Write a possible signature for `mystery`:

     {{% figure src="mystery-inputs.png" %}}
5. Write a signature for `magic` described below.

    ```racket 
    (magic (circle 40 "solid" "blue") 
           100)
    ```
     Produces two semi-transparent blue circles of radius 40:
     {{% figure src="semi-transparent-circles.png" %}}
     Aside: if they were solid blue, they would look like this:
     {{% figure src="solid-circles.png" %}}  
6. Write a signature for `overtext`.
    ```racket
    (overtext "Banned" (scale 5 pic:stick-figure))
    ```
    {{% figure src="banned-result.png" %}}
7. Write a signature for `dimsum`, which returns the sum of the length
    and width of each of its dimensions.
    ```racket
    (dimsum (rectangle 400 100 "solid" "blue")
            (cirlce 45 "outline" "green"))
    ==> 680
    ```
