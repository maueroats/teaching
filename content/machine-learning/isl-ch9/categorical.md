---
title: "Python Notes"
date: 2019-03-02T20:34:20-06:00
weight: 10
draft: false
#type: slide
#theme: white
---

Categorical data. 
<!--more-->

## Categorical Data

Categorical data has only a few values, so is encoded efficiently.

 [Pandas
documentation on categorical
data](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html):
to make data categorical, you should make a new categorical column: `df["B"] =
df["A"].astype('category')`. 

The `legend="brief"` option to `sns.scatterplot` does not work when
the coloring of the points is done with a numerical categorical
variable. Use `legend="full"` instead.


