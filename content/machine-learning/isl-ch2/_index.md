---
title: "ISL Chapter 2"
date: 2018-09-29T09:08:21-05:00
weight: 91
draft: false
#type: slide
#theme: white
description: "Basic working with data frames. Selection and counting without loops. Graphs, especially scatterplot and bar graph."
---

Required work for Chapter 2:

* Conceptual questions 1,2,3,5,6,7
* Practical exercises: 9, 10.
* Question 10: don't get stuck in part c - all of the other parts
  are more accessible.

Common confusions:

* Question 10: [how do I get the data?]({{% relref "Boston-Starter.html" %}})
* Question 10 refers to "suburbs" of Boston, but it is not clear that
  the data points refer to suburbs. Redefine "suburb" to be "data
  point". Answer questions such as "which suburb" by "row 50 in the
  dataset", or like this:
  
    ```
    boston.iloc[50,:]

    crim         0.08873
    zn          21.00000
    indus        5.64000
    chas         0.00000
    [...]
    ```

## Getting the data

Most of the data is on the [ISL web
site](http://www-bcf.usc.edu/~gareth/ISL/data.html). Here are direct
links:

* [Auto.csv](http://www-bcf.usc.edu/~gareth/ISL/Auto.csv)
* [College.csv](http://www-bcf.usc.edu/~gareth/ISL/College.csv)
* [Boston data starter notebook]({{% relref "Boston-Starter.html" %}}):
  a simple way to get the Boston data loaded and described.

Example of how to load the data:

```
df = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Auto.csv', 
                 na_values = '?', sep=",")
```

Common parameters: 

* `na_values` contains a string used to represent missing
  data. Only needed if data is not in a usual format (sorry, that's
  the Auto dataset).
* `sep` could be `"\t"` if the columns are separated
by tabs instead of spaces. 

{{% alert theme="warning" %}}
## Links for Lab 2.3a

* HTML [Lab 2.3]({{% relref "ISL2LabQuestions.html" %}}) (recommended)
* [Lab 2.3 Solutions]({{% relref
  "ISL2LabSolutions.html" %}}) should not be needed - typing helps you remember.
{{% /alert %}}



## Directly Downloadable Content
These links do not go to GitHub display pages, they go straight to the
raw source code. They are also automatically generated so they will
always be up to date.

{{% attachments-github title="Downloadable Jupyter Notebooks" pattern=".*\.ipynb" /%}}

{{% attachments-github title="Datasets" pattern=".*\.(csv|data|tsv)" /%}}


### Changelog
2018-09-19 Directly downloadable links fixed.
2018-09-29 Cleanup with a focus on getting loaded and running.

