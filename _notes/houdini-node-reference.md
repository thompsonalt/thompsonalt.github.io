---
title: Node Reference
date: 22/05/10
category: houdini
---

### To get curveu without resample
Use a `uvtexture` node set to "Arc Length Spline" and the attribute class set to "Point"

### Change attribute persision
`attribcast` node will let you modify attribute types.

### Curves
Useful nodes for curves
- `resample`
- `fit`
- `cardinal_ql`

### Spirals
- `sweep` will let you roll around a curve
- `labs::spiral` 
- `qLib::spiral_ql`

### Groups
- `groupfromattributeboundary` Makes edge groups from transitions between attributes


### COPs

To disable premultiplication in a COP file node, there is a drop down next to the file name.