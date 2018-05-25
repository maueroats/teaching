---
title: "P4. Model Message"
date: 2018-05-25T11:20:54-05:00
weight: 32
draft: false
#type: slide
#theme: white
description: "A lecture on models and messages, based on misconceptions that surfaced during a quiz."
---

## Model

The **model** carries all of the information. The mouse-handler can only change the model, the tick-handler can only change the model. The draw-handler can only look at the model to decide what to draw. 

Once you relly understand that everything you want to do has to be done through the model, you begin to ask questions like "How will I know in the model that my animation is paused?" instead of "How will I pause my animation?" This makes a huge difference - it makes writing programs much easier, because the way you are thinking is the way the program actually works.

## Message

The **message** is the only way to communicate information between worlds. If you need to know anything about the model from another world, you communicate that information in a message.

* The model should only know one world's information.
* You cannot change the world by changing its "id". That would be like saying you are going to Doc Mo's class by changing your name to "Doc Mo". Never change the world id.
* Advice: only remember what you need from a message. This means change the model in the receive-handler, but do not place the whole message in the model. When someone gives you a donut, you eat the donut (that's changing your model). You don't usually walk around with a note saying "I got a donut from Carol." (That would be saving the message.)

## Model vs Message

Every handler needs to decide whether to return a model or a package containing the model and a message. 

* Model: only affects one world
* Message: affects all worlds

