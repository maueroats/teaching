---
title: "15. File Intro"
date: 2018-04-18T10:28:09-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "API for File, Scanner, PrintWriter."
---

Sample code: [class github](https://github.com/2017-2018-wy-ap-cs/java-rotary-phone/tree/master/ch15).

You should be familiar with the basic methods listed in the [JavaMethods Chapter 15 PowerPoint](http://www.skylit.com/javamethods2/ppt/index.html).

## File

The [official File documentation](https://docs.oracle.com/javase/8/docs/api/java/io/File.html) has all of the details. This is a brief summary of methods you are likely to use.

* `new File("filename")`. I recommend you only files in the same directory as your Java program, until you become very comfortable with Files.
* `String getName()`
* `long lastModified()`: Return modification time, in unusual units.
* `boolean isDirectory()`
* `File[] listFiles()`

## Scanner

Consult the [Chapter 15 PowerPoint](http://www.skylit.com/javamethods2/ppt/Ch15.ppt) for common functions or [the official documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html) for full information.

| Inquire (all return `boolean`) | Get    | Notes |
|---------------------------------|--------|-------|
| `hasNextLine()` | `String nextLine()` | Rest of the line, starting at the current location. |
| `hasNext()`     | `String next()`      | One token (group of letters and numbers) until next whitespace.   |
| `hasNextInt()`  | `int nextInt()`      | One integer. |
| `hasNextDouble()` | `double nextDouble()` | One decimal. |

Miscellaneous:

* `NoSuchElementException` is returned when a Scanner is asked for something that it cannot provide - for example, `nextInt()` when the next item is not an integer.

## PrintWriter

* `PrintWriter out = PrintWriter (file)`: Construct based on a `File` object.
* `out.println()`: Print, like usual.
* `out.close()`: Write all of the data to the disk.

