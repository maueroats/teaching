---
title: "Button"
date: 2019-06-11T11:31:12-05:00
weight: 50
draft: false
#type: slide
#theme: white
description: "Adding a push button to your circuit."
---

A button is a digital device, it reads either pressed or not pressed.
The Arduino is set up to consider a reading of 5V as "true", so with
the circuit below,
<scratch class="inline">digital reading () :: #468cfc reporter</scratch>
 gives true when the button is _not_ pressed.

{{% figure src="button-1.png" %}}

I will use 
<scratch class="inline">button pressed? :: variables reporter</scratch> 
for the variable that holds the reading from 
the button.

{{< scratch >}}
when green flag clicked
forever
  set [button pressed? v] to < not < digital reading (10) :: #468cfc> >
  if (button pressed?) then
    say [Pressed] for (0.5) seconds
  else
    say [Not Pressed] for (0.5) seconds
{{< /scratch >}}

