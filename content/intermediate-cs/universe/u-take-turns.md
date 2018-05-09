---
title: "Universe Taking Turns"
date: 2018-05-02T21:18:09-05:00
weight: 35
draft: false
#type: slide
#theme: white
description: "An introduction to taking turns when the universe broadcasts all messages to every client."
---

1. **Labeled worlds**. Give each world a unique identity (a string name or a number). Show the world's identity in the upper left corner. When you hit a key in a world, every world also shows the identity of the world you clicked in.

2. **Colored worlds**. The world you hit a key in turns green. All other worlds turn yellow. Still show each world's identity.

3. **Active stamping**. Add on to your _colored worlds_ program. Hit a key to activate a world. Only one world is active at a time. When you click in the active world, it shows a solid circle. Inactive worlds show an outline circle. (Basic: only one circle at a time, no control over where it appears, disappears when de-/activating. Challenge: show all circles, centered at the location of the click.

4. **Spinning**. Each world has a separate image. Only one image spins at a time. When you hit a key in a window, that world's image starts spinning and the other window(s) stop.

5. Chase. Each world has one image that it controls with the mouse. Hitting a key makes the mouse inactive for about one second. (Use a tick handler to reactivate.) I used a colored bar to indicate whether the window is active or not.

    {{% figure src="chase-drawn-frozen.png"  %}}
    {{% figure src="chase-drawn-running.png"  %}}

{{% alert warning %}}
You cannot send a `posn` as a message for technical reasons. Reasonable replacements: `(define-struct msg (x y))` or use `(list x y)` for the message.
{{% /alert %}}

