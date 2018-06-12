---
title: "Final Problem"
date: 2018-06-12T09:15:41-05:00
#weight: 
draft: false
#type: slide
#theme: white
description: "Splash game."
---

{{% alert theme="info" %}}
{{% attachments title="Helper Classes" pattern=".*\.java$" /%}}
{{% /alert %}}

The Whitney Young Dolphins have come up with a new game to play: "Splash".

{{< use-mathjax >}}

The game of splash is played on an $N \times N$ grid. A dolphin claims
a square by splashing their fin and writing their id number in the
square.

The game ends when all of the squares have numbers in them.

An individual dolphin wins if they have connected the largest
contiguous region. Two squares belong to the same region if the have
the same id number and there is a path from one to the other going up,
down, left, right (but no diagonals) all on squares with the same id
number as the start and end.

Dolphins are team players, so they prefer to play the game with a
partner. When two dolphins play on a team together, either one of
their id numbers can be used at any step of the connecting path to
form a region. In fact, for a team to count a region, 
the id numbers of both players _must_ be used in the region.

## Input Format

The first line of the file with be the number N.

Each of the N lines following will contain N positive integers
separated by spaces.

## Output Format

Output two lines, each containing one number.

* The first number is the largest sized region for any single dolphin.
* The second number is the largest sized region for any two-dolphin team.

## Constraints

The board will be at most 250x250. The id numbers will all be
nonnegative integers less than one million.

{{% alert theme="info" %}}
{{% attachments title="Test Data" pattern=".*\.txt$" /%}}
{{% /alert %}}

