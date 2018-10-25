---
title: "ISL Chapter 3: Linear Regression"
date: 2018-10-08T15:10:33-05:00
weight: 92
draft: false
#type: slide
#theme: white
description: "Graphs of results. Quality of fit (statistical tests). When do you have enough variables included?"
---

* [Chapter 3 Section 1]({{% relref "Chapter3-Section1" %}})
* [Chapter 3 Section 2]({{% relref "Chapter3-Section2-MultipleRegression" %}})
* [Chapter 3 Section 6]({{% relref "Chapter3-Section6-Linear-Regression-Lab" %}})

## Homework

* [Chapter 3 Section 1 Worksheet
  A](https://colab.research.google.com/drive/11SjQKhsL9oX3bM5pHvGAl2yHhQN4M9-v).
  (October 10-11, 2018) [Solutions to A]({{% relref
  "Chapter3-Section1-Worksheet-A-Solutions.html" %}}) discussed in class. Remainder became worksheet BC.
* [Chapter 3 Section 1 Worksheet
  BC](https://colab.research.google.com/drive/1sByruzoLR3D14if-x3YppUbsJsgVroYU). Assigned:
  Friday, October 12. Due: Monday, October 15. [Lecture]({{% relref "Chapter3-Section1-Worksheet-C-Demo.html" %}}).

* [Reading Questions for 3.1.2]({{% relref "reading-q-312" %}}). Due:
  Oct 17.

* [Chapter 3 Section 1 Worksheet
  D](https://colab.research.google.com/drive/1un0iS9v6hjc_WrzpVqj1BWSouG-fnHw2). Assigned:
  October 16. Due: October 17.

* [Chapter 3 Exercise 8 Demo](https://colab.research.google.com/drive/1kup4F6XKYZ4Sqcxuj8ClE1K14sCCDT1o).

## Notes of Interest

I was just curious about the logistic distribution, so I dug up a few
points of interest. These are not critical. Especially do not confuse
this with other uses of logistic that come up later in the course.

1. From Wikipedia, the [logistic distribution is used to calculate
   chess ratings](https://en.wikipedia.org/wiki/Sech-square_distribution#Chess_ratings):

     > Τhe United States Chess Federation and FIDE have switched its formula for calculating chess ratings from the normal distribution to the logistic distribution; see the article on Elo rating system (itself based on the normal distribution). 

2. The logistic distribution is easier to work with than the normal
   distribution. There is a formula for its cumulative density
   function that does not require approximation on a computer.


## Graphical Summary of Linear Model
Download the `linearmodelplot.py` file from the attachments at the
bottom of the page.

Make sure you have the standard includes for Chapter 3. A quick
starter code is below. See the [full sample making a summary plot for
a linear model]({{% relref "Using plot_lm_summary" %}}) for a working notebook.

How to [upload python files to
Collaboratory](https://stackoverflow.com/questions/48905127/importing-py-files-in-google-colab).

```python
from linearmodelplot import plot_lm_summary
fitted_lm = sm.ols(...).fit()
plot_lm_summary(fitted_lm);
```

{{% notice tip %}}
Download the `linearmodelplot.py` and then use the 
[starter notebook including file-uploading
code](https://colab.research.google.com/drive/1LhNP4uEkqAlzYByjGh3FPYt7iP-pnyOo)
to get going more easily.
{{% /notice %}}


## Downloadable Content (from Github)

{{% attachments-github title="Python Code" pattern=".*\.py" /%}}
