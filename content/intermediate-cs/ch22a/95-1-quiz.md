---
title: "22a. Mini-Quiz"
date: 2019-02-27T16:50:50-06:00
weight: 95
draft: false
type: slide
theme: white
---
# `ex-it`

`ex-it: string -> string`

Change every "x" to a "y".

    (check-expect (ex-it "tresxxx") "tres")
    (check-expect (ex-it "zyzzyva") "zyzzyva") ; no change
