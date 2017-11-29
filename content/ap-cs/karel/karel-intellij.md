---
title: "Karel Intellij"
date: 2017-11-28T21:30:53-06:00
draft: false
#type: slide
#theme: white
description: "How to use IntelliJ IDEA to work with our Karel the Robot configuration."
---

This documents using [IntelliJ IDEA](https://www.jetbrains.com/idea/) development environment. Way overkill unless [DrJava](http://drjava.org) is giving you trouble.

## Easy method
* Clone the [apcs-karel-intellij](https://github.com/2017-2018-wy-ap-cs/apcs-karel-intellij) repository. 

    This is just a snapshot to get you started at home. I just copied all of the java files from the karel repository to a new directory in the correct place. 

```sh
git clone https://github.com/2017-2018-wy-ap-cs/apcs-karel-intellij
```

* IDEA has: File -> New -> Project from existing sources... that will let you import my files. If you are lucky you can even just use my whole folder.
    
    
## Step by step

1. New project in IDEA: File -> New -> Project...
2. Make lib and src subfolders.
3. `KarelJRobot.jar` goes into lib.
4. All java files go into src.
5. IDEA: 
    * File -> Project Structure... -> Modules (under Project Settings on left) 
    * Select "Dependencies" tab.
    * Use "+" and choose the KarelJRobot.jar file in the lib folder.
    * I checked the box "Export"; not sure if that matters.
6. Build -> Build Project. I had to delete the "HackBot.java" since I did not include the hacked KarelHRobot library.
7. Run -> Run...

