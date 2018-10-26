---
title: "Linear Model Summary Plot"
date: 2018-10-26T13:16:40-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Summary plot of a linear regression, exactly like R provides."
---

## Graphical Summary of Linear Model

Download the `linearmodelplot.py` file from the attachments at the
bottom of the page. Make sure you save the file as "All Files..." an
not "Text file".

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
