---
title: "SI Walkthrough"
date: 2017-12-14T13:56:16-06:00
draft: false
#type: slide
#theme: white
---

## Drawing

1. Draw alien at a given posn on a background
    
    ```text
draw-alien: posn image(bg) -> image
```
2. Draw turret at a given posn on a background

    ```text
draw-turret: posn image(bg) -> image
```
3. Draw bullet at a given posn on a background

    ```text
draw-bullet: posn image(bg) -> image
```
4. Draw win screen.

5. Draw lose screen.

## Action

0. Bullet activating function. This does not fit into our model so far.

    ```text
activate-bullet: posn(turret-posn) -> posn(bullet-posn)
```
1. Right arrow moves right, left arrow moves left

    ```text
turret-key-h: model(turret-posn) -> model(turret-posn)
```


## Tick handler

1. Bullet moves up at a constant rate.

    ```text
update-bullet: posn -> posn
```
Details: where should the bullet be when you start?

2. Alien advances (harder). 

     How can you tell when to go right and when to move left? Discuss choices: y-coordinate or an extra direction parameter.

## Logic

For each of these, first write (or type) the information you will take
as parameters in order to create the function. Do not include
constants in your parameter list.

1. `enemy-right-edge?`: posn (enemy-posn) number(direction) -> boolean
2. `enemy-left-edge?`: posn (enemy-posn) number(direction) -> boolean
3. `bullet-hit-enemy?`: posn (bullet-posn) posn (enemy-posn) -> boolean 
4. `enemy-hit-turret?`: posn (enemy-posn) posn (turret-posn) -> boolean
5. `game-over?`: posn(bullet-posn) posn (enemy-posn) posn (turret-posn) -> boolean
6. `bullet-on-screen?`: posn (bullet-posn) -> boolean
7. `can-fire?`: posn (bullet-posn) -> boolean

## Combining

Now we need a model that will combine everything, and write handlers that combine the
other handlers. They are going to look like basically like this:

```racket
(define (real-tick-handler model)
    (alien-tick-handler (bullet-tick-handler model)))
``` 

There are some technical details and I will end up providing functions that glue
everything together.

