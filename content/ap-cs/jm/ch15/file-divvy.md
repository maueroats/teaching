---
title: "15. File Divvy"
date: 2018-04-26T09:34:20-05:00
weight: 40
draft: false
#type: slide
#theme: white
description: "Questions about the Divvy trip database."
---

Get a subset of [Divvy bike trip data](smalltrips.csv). Later you may want the [Divvy station data](stations.csv) as well.

1. Find the trip of longest duration.
2. Find the oldest female rider in this dataset.

## Tips

You do not have to store the data in an `ArrayList`, but if you want to do that, you should make a class `BikeInfo` that has all of the information contained on one line in the database. Making 12 separate ArrayLists is lots harder to work with.

The `Scanner` class has a `useDelimiter` method that can be used to split on things that are not whitespace.

The `String` class has a `split` method that can be used in a similar way.
