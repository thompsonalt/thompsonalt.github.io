---
layout: note
title: Houdini Vex Reference
date: 2018-10-14 12:29:12 -0700
categories: 
    houdini
---

## [Declaring attributes](http://www.sidefx.com/docs/houdini/vex/snippets.html#declare)
```javascript
f@name //float
u@name //vector2 (2 floats)
v@name //vector3 (3 floats)
p@name //vector4 (4 floats)
i@name //int
2@name //matrix2(2x2 floats)
3@name //matrix 3 (3x3 floats)
4@name //matrix (4x4 floats)
s@name //string
```

You can also define them like this:
```javascript
float @mass = 1;
vector @up = {0, 1, 0};
```

### Arrays
```javascript
int nbors[] = neighbours(0, @ptnum);
i[]@connected_pts = neighbours(0, @ptnum);
```

### [Set Attribute as a Vector that Houdini Should Transform](https://www.sidefx.com/forum/topic/41722/?page=1#post-187303)
By default, when you declare a vector attribute in Houdini it doesn't know if it should transform it with the rest of the geo or not. Some attributes, like `@orient`, `@v`, and `@N`, Houdini automatically knows to transform. If you create your own attribute, you'll have to set the type info explicitly. I'm curious if that attribute type info is visible somewhere.
```javascript
v@attribute1 = 1;
setattribtypeinfo(0, “point”, “attribute1”, “vector”);
addvariablename(0, “attribute1”, “ATTRIBUTE1”);
```