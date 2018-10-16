---
layout: note
title: First Houdini Post
date: 2018-10-14 12:29:12 -0700
categories: 
    houdini
---

## This is my first attempt at a Houdini post

```javascript
float maxdist = ch('maxdist');
int numlegs = chi('legs');
int pts[];
int prim;
int i;
 
if (@group_soot==1) {
  pts = nearpoints(0,@P,maxdist,numlegs);
  for (i=1; i<len(pts); i++) {
     prim = addprim(0,'polyline');
     addvertex(0,prim,@ptnum);
     addvertex(0,prim,pts[i]);
  }
}
```
