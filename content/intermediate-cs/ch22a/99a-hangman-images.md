---
title: "22a. Hangman Images"
date: 2018-03-15T13:20:05-05:00
weight: 991
draft: false
#type: slide
#theme: white
description: "How to load a sequence of images into DrRacket."
---

Goal for the day: produce a sequence of images to use for "hangman" and load it into Racket. 


## Image sequence

Draw a sequence of images `hang-0.png`, `hang-1.png`, etc., with the appropriate number of parts of the person filled in. Use "File -> Export as..." to save each file with a different name. 

Tools:

* Microsoft Paint on Windows
* [Paintbrush](https://paintbrush.sourceforge.io/) ([download](https://sourceforge.net/projects/paintbrush/files/latest/download?source=files)) on Macintosh.
* [Gimp](https://www.gimp.org/) on Linux. 

## Load into Racket

The best way to load an image from a file is to use `bitmap/file`. 

Examples:

* `(bitmap/file "hang-0.png")`
* `(bitmap "pics/hang-1.png")`

## Why?

The only cases of file corruption I have seen involve large images
being pasted into DrRacket files. Keeping the images in separate files
prevents that problem.

