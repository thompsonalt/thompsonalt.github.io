---
title: Node Reference
date: 22/05/10
category: houdini
---

## SOPs

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

### Attribute Create

Attributecreate offers a clean way to construct strings from existing attributes. Unlike parameters on wrangles, you can access local varaibles and attributes. Adding your own attributes works as well.

![attribute create screenshot](/assets/images/23-03-02-attribcreate-string-screenshot.png)


### VDBs
#### Infuse density vdb with velocity vectors.
I often find myself with a density volume or VDB that I'd like to add velocity to. If it's coming from geometry, you could use the `vdbfrompolygons` node to read the velocity surface attribute. Otherwise, there are a couple approaches.

One simple method would be to use a `convertvdb` node with "Convert To" set to VDB and "VDB Type" set to "Vector Float". After that you just need to rename your primitive to "vel" and merge it with your original density VDB.

Another, and perhaps more "correct" way is to use `vdb` and `vdbactivate` nodes. Your `vdb` node gets plugged into your density VDB. You can name it `vel` and select the "Vector Float" type. Also set the "vector type" to velocity. Below that, plug the output into the first input of a vdb activate. This node will be set to the "Reference" tab with "Activate Using VDBs" optionally checked. The second input goes into your original density VDB. This has the effect of creating an empty VDB, and activating the same VDB grids as your density VDB. Then you can merge them together just like the previous technique.

![VDB Screenshot](/assets/images/22-10-04-vdb-techniques.png)

## COPs

To disable premultiplication in a COP file node, there is a drop down next to the file name.

## Kinefx

[Matt's video on IK Chains](https://youtu.be/ZEFYdbhsVi0)