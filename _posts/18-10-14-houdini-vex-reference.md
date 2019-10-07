---
title: Houdini Vex Reference
layout: note
date: 18-10-14
categories: houdini
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

This is another way to define them. A drawback to this method is there can be no evaluation on the right side of the equation.
```javascript
float @mass = 1;
vector @up = {0, 1, 0};
```

The typical way to grab an attribute from the second input of a wrangle would be to use the `point` function. Another way is to use `@opinput1_` followed by the attribute name.
```javascript
v@cord_offset = point(1, "P", 0); 
v@cord_offset = @opinput1_P;
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

### Create Groups from Attributes
This is of limited usefulness. `detailintrinsic` is a handy way to get a list of all the primitive attributes. See more on that [here](https://www.sidefx.com/forum/topic/31699/).

```javascript
string primattribs[] = detailintrinsic(0,"primitiveattributes");

for (int i = 0; i < len(primattribs); i++) {
    setprimgroup(0, primattribs[i], @primnum, prim(0, primattribs[i], @primnum), "set");
}
```

### Easy positive or negative integer
```javascript
i@rand_mag =  rand(@ptnum)< 0.5 ? -1 : 1;
```
Or even easier:
```javascript
sign(rand(@ptnum)-0.5);
```

### Extract transform from Alembic
From this help page on [`packedtransform()`](https://www.sidefx.com/docs/houdini/vex/functions/packedtransform.html).
[Hip download.](/assets/projects/houdini/19-10-07-alembic-transform.zip)

Negate and store transform:
```javascript
// get transform from alembic
matrix full_transform = primintrinsic(0, "packedfulltransform", 0);
4@disabled_transform = full_transform;

// invert that transform
matrix invert_full_transform = invert(full_transform);
matrix transform = invert_full_transform;

// get current packed transform
matrix3 primtf = primintrinsic(0, "transform", @primnum);
setprimintrinsic(0, "transform", @primnum, primtf * (matrix3)transform);

// set position
int primpoint = primpoint(0, @primnum, 0);
vector pos = point(0, "P", @ptnum);
setpointattrib(0, "P", @ptnum, pos * transform);
```

Apply transform to arbitrary geo:
```javascript
matrix transform = prim(1, "disabled_transform", 0);

// get current packed transform
setprimintrinsic(0, "transform", @primnum, (matrix3)transform);

// set position
int primpoints[] = primpoints(0, @primnum);
for (int i = 0; i < len(primpoints); i ++){
    int point_num = primpoints[i];
    vector pos = point(0, "P", point_num);
    setpointattrib(0, "P", point_num, pos * transform);
}
```


## Links
[VFXbrain has some great vex snippets](https://vfxbrain.wordpress.com/2016/10/02/vex-snippets/)

