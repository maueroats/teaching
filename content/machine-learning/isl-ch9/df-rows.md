---
title: "Dataframe Rows"
date: 2019-03-12T16:57:42-05:00
#weight: 
draft: false
#type: slide
#theme: white
description: "How to speed up accessing the information for the Perceptron."
---

My perceptron was very slow until I read a [Stack Overflow comment](https://stackoverflow.com/questions/7837722/what-is-the-most-efficient-way-to-loop-through-dataframes-with-pandas) that
led me to a post [comparing the speeds of different ways of accessing
a dataframe by rows](https://towardsdatascience.com/different-ways-to-iterate-over-rows-in-a-pandas-dataframe-performance-comparison-dc0d5dcef8fe?gi=6aa22445ae23).

If you are using `df.iloc[rownum]`, your code is slow. The fast way to
get rows is to zip the columns together and get the info from that
list/array. It's not just a little fast, it's like 100x faster.

Code snippet:

    #outside of beta updating function
    xyc = list(zip(df.x, df.y, df.c))

    #inside beta updating function
    for (x1,x2,c) in xyc: 
       ...
       
