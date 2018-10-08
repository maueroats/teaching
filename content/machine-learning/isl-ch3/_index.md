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

## Graphical Summary of Linear Model
Download the `linearmodelplot.py` file from the attachments at the
bottom of the page.

Make sure you have the standard includes for Chapter 3. A quick
starter code is below. See the [full sample making a summary plot for
a linear model]({{% relref "Using plot_lm_summary" %}}) for a working notebook.

```python
from linearmodelplot import plot_lm_summary
...
fitted_lm = sm.ols(...).fit()
plot_lm_summary(fitted_lm);
```

## Downloadable Content

{{% attachments title="Python Code" pattern=".*\.py" /%}}

