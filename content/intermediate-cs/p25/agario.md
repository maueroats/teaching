---
title: "Agar.io"
date: 2018-05-16T22:21:14-05:00
weight: 20
draft: false
#type: slide
#theme: white
description: "A clone of the agar.io web game."
---

Do not play the [agar.io](http://agar.io/) game more than necessary to learn the rules. We don't plan to make a full clone of the game, just allow an unlimited number of individual circles to move about the screen.

Warning: your clone will lag more than the original web site. Don't expect lightning fast responses.

## Model

* A single player has: unique identity (id), color, position, and radius.
* One big-bang is a player that is being controlled and a list of other players.

## Message 

The mouse-handler will send a message indicating how the player being controlled has moved. 

## Receiving the message

When a big-bang receives a message, it will:

- update the current player being controlled, if the message comes from the same world; or
- go through the list of players and replace the player with the newly received player info

## Helper functions

* `replace-player: player(new) listof-player(players) -> listof-player`. Replace the player with the same identity as `new` by the actual player `new`. All other players in the list are returned unchanged.

