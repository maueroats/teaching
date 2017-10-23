---
title: "Essentials"
date: 2017-10-17T10:17:44-05:00
draft: false
description: "Links to the repository and documentation for the Karel the Robot unit."
weight: 5
---

## Getting started 

1. GitHub Classroom 
```url
https://classroom.github.com/a/bOX4Z5jT
```
You should end up with a new repository which has all of the Karel starter files and also lets you save your files. 

    Note the link in the green box!

2. Git clone

    In this step you download your new repository to the computer you are working on. 
    Start "Git Bash" or type the following in "Terminal" on your computer.
```git
git clone paste-link-to-your-repository-here
```

3. One time settings

    In this step you run my one-time setup code that links you to the original repository. You need to actually be inside the directory/folder that you just cloned for this command to work. 
```ssh
    cd karel-*
     ./one-time
```
    This command currently:

    * Sets the editor to "nano", a reasonable beginner's editor.
    * Adds a remote repository containing the AP CS "master" code so you can get updates.

    Alternative:
```git
    cd karel-*
    git remote add upstream https://github.com/2017-2018-wy-ap-cs/apcs-karel.git
    git config core.editor nano
```

## Saving your work

I have a `save-it` script that makes it easy for you to save and push your changes in one step:
```ssh
     cd karel-*
     ./save-it 'Optional message'
```
You can use the `save-it` script or type the following commands:

```git
git add -A
git commit -a -m 'Save'
git push -u origin master
```

The meaning of these commands is:

* git add
     * -A: I intend to save every new file.
* git commit: Save every change to a special place on the current computer.
     * -a: Save all files that are known (changed, deleted, or new and already added).
     * -m 'Save': The required message for the save is just the word "Save". Pros are more descriptive.
* git push: Send the changes to GitHub so they are stored online and I can get them from other computers.

## DrJava

### Getting DrJava

On the lab computers, DrJava is on the Desktop in the Computer Science
folder. Unfortunately it is not in the windows menu at this time.

At home you will need to download [DrJava](http://drjava.org/). 

* Mac OS X: read the instructions carefully; do not download the disk image (".dmg") file.
* Windows 10: install [Oracle Java 8 JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) and DrJava should work fine. You may need to uninstall other versions of Java.


### Running DrJava

Open `karelBasic.drjava`.

**In the Projects menu**, there is an option to open a project. **This is not the same as ther other "Open" options you see!** Use that instead of the more obvious "open a file" command so that you don't have to re-teach DrJava about the Karel the Robot files.


## Documentation

* [Karel the Robot](https://csis.pace.edu/~bergin/KarelJava2ed/KJRdocs/index.html) documentation online.

* [JUnit](http://junit.org/junit4/javadoc/latest/) documentation online.

* [Hamcrest matcher libary](http://hamcrest.org/JavaHamcrest/javadoc/1.3/) documentation online.


