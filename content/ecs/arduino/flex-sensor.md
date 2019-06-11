---
title: "Flex Sensor"
date: 2019-06-11T11:22:38-05:00
weight: 40
draft: false
#type: slide
#theme: white
description: "The basics of connecting a flex sensor."
---

Connect the flex sensor and a 10,000 ohm resistor. One end of the
assembly should be 5V (+), the other end GND (-). In the middle, run
the wire to an analog voltage sensor.

{{% figure src="flex-sensor.png" %}}


{{< scratch >}}
when green flag clicked
forever
  set [flex reading v] to (analog reading (2) :: #468cfc) 
  say (flex reading) for (0.5) seconds
  set pin (9 v) to value ((flex reading) / (4)) :: #468cfc
{{< /scratch >}}

