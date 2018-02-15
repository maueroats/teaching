---
title: "14. Binary Search"
date: 2018-02-15T10:35:29-06:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Binary search to find an item or an insertion point."
---

1. Binary search: the traditional function returning an index where the wanted item is found, or `-1` if the item is not found.

        public static int binarySearch(ArrayList<String> data,
                                       String wanted);
                                       


2. Binary insert: this function finds the index (`idx`) at which a new item fits in the ordering, so that `data.add(idx, newItem)` results in `data` still being sorted. 

        public static int binaryInsert(ArrayList<String> data,
                                       String newItem);
                                       
