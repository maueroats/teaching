---
title: "Essentials"
date: 2017-10-16T11:19:58-05:00
draft: false
description: "Links to the repository and documentation for the Karel the Robot unit."
weight: 5
---
## Book

The book is [_Karel J Robot: A Gentle Introduction to the Art of
Object-Oriented Programming in Java_](https://www.amazon.com/Karel-Robot-Introduction-Object-Oriented-Programming/dp/0970579519), by Joseph Bergin, Mark Stehlik,
Jim Roberts, and Rich Pattis. We have the January 2008 printing, but
all versions are very similar. Happily, the book is available for under $10 used.

## Documentation

* [Karel the Robot](https://csis.pace.edu/~bergin/KarelJava2ed/KJRdocs/index.html) documentation online.

* [JUnit](http://junit.org/junit4/javadoc/latest/) documentation online.

* [Hamcrest matcher libary](http://hamcrest.org/JavaHamcrest/javadoc/1.3/) documentation online.

## Downloading the files

You should get them all by `git clone` [the central repository](https://github.com/2017-2018-wy-ap-cs/apcs-karel).
```git
git clone https://github.com/2017-2018-wy-ap-cs/apcs-karel.git
```

## Getting started 

* Make your own repository to hold your version of this code. (note link for use below)
* Clone this repository
* Change the name to "upstream":
     git remote rename origin upstream
* Add your own repository as a remote:
     git remote add origin [link from starting step]

## Saving your work

You can use the `save-it` script or type the following commands:

```git
git add -A
git commit -a -m 'Save'
git push -u origin master
```

