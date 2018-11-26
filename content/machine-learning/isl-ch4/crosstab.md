---
title: "Crosstabulation"
date: 2018-11-21T09:00:19-06:00
#weight: 
draft: true
#type: slide
#theme: white
description: "Cross-tabulation gets results for a bunch of groupings at once."
---

## Pandas

* `df.groupby('age')`
* `df.groupby(['age', 'income'])`
* `df.crosstab(df.age, df.gender, values=df.income, aggfunc=np.mean)`

## Methods

* `mean()`
