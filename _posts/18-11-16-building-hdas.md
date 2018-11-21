---
title: Building HDAs
published: true
categories: houdini
date: 2018-11-16
---

To get the current node use `hou.node('.')` or `hou.pwd()`

To press a button deeper in the HDA use the following:
```javascript
hou.parm("./deadline_submit1/submit").pressButton()
```
[Nick Pfeiffer explains this well.](http://nicholaspfeiffer.com/blog/2016/2/20/houdini-tip-of-the-day-python-pressbutton-and-set-commands)

If you have a function in the asset's python module you'd like to access, use the following:
```javascript
hou.node(".").hdaModule().random_function()
# or...
hou.pwd().hm().random_function()
```
To get current node in a callback:
```javascript
kwargs.get("node")
```

[Link to Side Effects help](http://www.sidefx.com/docs/houdini/hom/hou/HDAModule.html)