---
title: Building HDAs
published: true
categories: houdini
date: 2018-11-16
---

To get the current node use `hou.node('.')`

To press a button deeper in the HDA use the following:
```javascript
hou.parm("./deadline_submit1/submit").pressButton()
```
[Nick Pfeiffer explains this well.](http://nicholaspfeiffer.com/blog/2016/2/20/houdini-tip-of-the-day-python-pressbutton-and-set-commands)