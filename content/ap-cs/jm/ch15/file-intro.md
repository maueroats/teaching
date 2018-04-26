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


## Common Problems and Advice

* Read error messages closely. 

    - Know what the error is. For example, this is a `FileNotFound` error caused by trying to read `myfolder` with `Scanner`, like a file.

            java.io.FileNotFoundException: myfolder (Is a directory)
                at java.io.FileInputStream.open0(Native Method)
                at java.io.FileInputStream.open(FileInputStream.java:195)
                at java.io.FileInputStream.<init>(FileInputStream.java:138)
                at java.util.Scanner.<init>(Scanner.java:611)


    - from a File? Know what File causes it.
    - from a Scanner? Know exactly what input causes the problem. Print lots! For example, this error comes from trying to get the `next()` item when there is nothing more available.

            java.util.NoSuchElementException
                at java.util.Scanner.throwFor(Scanner.java:862)
                at java.util.Scanner.next(Scanner.java:1371)

* Make sure you only call `listFiles` on a `File` that is a directory.
* Reading a directory like a file will give you a `FileNotFound` or permissions error.
* Listing the files in a file that is not a directory will return `null` but not give an error. This is dangerous because you cannot loop through the returned array (since nothing is created).
* You can get very unusual error messages if you start recursively examining a folder that contains your system files. Make folders especially for testing.
