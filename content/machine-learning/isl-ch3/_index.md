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
  (October 10-11, 2018) Solutions to A discussed in class. Remainder became worksheet BC.
* [Chapter 3 Section 1 Worksheet
  BC](https://colab.research.google.com/drive/1sByruzoLR3D14if-x3YppUbsJsgVroYU). Assigned:
  Friday, October 12. Due: Monday, October 15.

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

## Downloadable Content (from Github)

{{% attachments-github title="Python Code" pattern=".*\.py" /%}}
