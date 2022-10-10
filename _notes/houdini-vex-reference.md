---
title: Houdini Vex Reference
date: 18-10-14
category: houdini
---

## [Declaring attributes](http://www.sidefx.com/docs/houdini/vex/snippets.html#declare)
```c
f@name //float
u@name //vector2 (2 floats)
v@name //vector3 (3 floats)
p@name //vector4 (4 floats)
i@name //int
2@name //matrix2(2x2 floats)
3@name //matrix 3 (3x3 floats)
4@name //matrix (4x4 floats)
s@name //string
d@name //dict
s[]@name //array of strings
f[]@name //array of floats
```

This is another way to define them. A drawback to this method is there can be no evaluation on the right side of the equation.
```c
float @mass = 1;
vector @up = {0, 1, 0};
```

The typical way to grab an attribute from the second input of a wrangle would be to use the `point` function. Another way is to use `@opinput1_` followed by the attribute name. This will grab the element with the same index as the first input. There is also a “attribute to match” parameter that will let you use arbitrary attributes such as `id`.
```c
v@cord_offset = point(1, "P", 0); 
v@cord_offset = @opinput1_P;
```

### [Reference Parameters in Vex](https://mrkunz.com/blog/08_22_2018_VEX_Wrangle_Cheat_Sheet.html)

```c
ch('flt1');             // Float
chf('flt2');            // Float
chi('int');             // Integer
chu('vector2')          // Vector 2
chv('vecparm');         // Vector 3
chp('quat');            // Vector 4 / Quaternion
ch3('m3');              // 3x3 Matrix
ch4('m4');              // 4x4 Matrix
chs('str');             // String
chramp('r', x);         // Spline Ramp
vector(chramp('c', x)); // RGB Ramp 
```

### Global Variables

```c
@Time //Float time ($T)
@Frame //Float frame ($FF)
@SimTime //Float simulation time ($ST), only present in DOP contexts.
@SimFrame //Float simulation frame ($SF), only present in DOP contexts.
@TimeInc //Float time step (1/$FPS)
```


### [Attribute Wrangle Variables](https://mrkunz.com/blog/08_22_2018_VEX_Wrangle_Cheat_Sheet.html)
```c
v@P         //The position of the current element.
i@ptnum     //The point number attached to the currently processed element.
i@numpt     //The total number of points in the geometry.
i@vtxnum    //The linear number of the currently processed vertex.
i@numvtx    //Vertices in the primitive of the currently processed element.
i@primnum   //The primitive number attached to the currently processed element.
i@numprim   //The total number of primitives in the geometry.
i@elemnum   //The index number of the currently processed element.
i@numelem   //The total number of elements being processed.
```


### Arrays
```c
int nbors[] = neighbours(0, @ptnum);
i[]@connected_pts = neighbours(0, @ptnum);
```

### [Set Attribute as a Vector that Houdini Should Transform](https://www.sidefx.com/forum/topic/41722/?page=1#post-187303)
By default, when you declare a vector attribute in Houdini it doesn't know if it should transform it with the rest of the geo or not. Some attributes, like `@orient`, `@v`, and `@N`, Houdini automatically knows to transform. If you create your own attribute, you'll have to set the type info explicitly. I'm curious if that attribute type info is visible somewhere.
```c
v@attribute1 = 1;
setattribtypeinfo(0, “point”, “attribute1”, “vector”);
addvariablename(0, “attribute1”, “ATTRIBUTE1”);
```

You can also specify the type with the `attributeadjustvector` node.

### Create Groups from Attributes
This is of limited usefulness. `detailintrinsic` is a handy way to get a list of all the primitive attributes. See more on that [here](https://www.sidefx.com/forum/topic/31699/).

```c
string primattribs[] = detailintrinsic(0,"primitiveattributes");

for (int i = 0; i < len(primattribs); i++) {
    setprimgroup(0, primattribs[i], @primnum, prim(0, primattribs[i], @primnum), "set");
}
```

### Easy positive or negative integer
```c
i@rand_mag =  rand(@ptnum)< 0.5 ? -1 : 1;
```
Or even easier:
```c
sign(rand(@ptnum)-0.5);
```

### Extract transform from Alembic
From this help page on [`packedtransform()`](https://www.sidefx.com/docs/houdini/vex/functions/packedtransform.html).
[Hip download.](/assets/projects/houdini/19-10-07-alembic-transform.zip)

Negate and store transform:
```c
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
```c
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

## Find Weighted Average of Near Points Attribute

```c
// Compute color of voxel based on distance weighted
// average Cd of particles within radius of .05

int near_points[] = nearpoints(1, @P, .05);

// Find distances to all near points
float dists[];
foreach(int i; int pt; near_points) {
    dists[i] = distance(@P, point(1, "P", pt));
}

// Normalize by maximum distance
float max = max(dists);
float norm_dists[];
foreach (int i; float dist; dists) {
    norm_dists[i] = max/dist;
}

// Find weighted average Cd (value)
float total_normalized = sum(norm_dists);
vector value = set(0,0,0);
foreach (int i; float norm_dist; norm_dists) {
    float ratio = norm_dist / total_normalized;
    value += point(1, "Cd", near_points[i]);
}
value = value / total_normalized;

v@Cd = value;
```

## Modify cracked transform

This stumped me for a while. In order to crack the transform and feed those transform values back into a maketransform, you need to use `XFORM_SRT` instead of `XFORM_TRS` for the order of the transform.

```c
matrix3 xform = primintrinsic(0, "transform", @primnum);

vector translate, rotate, scale;

cracktransform(XFORM_SRT, XFORM_XYZ, @P, xform, translate, rotate, scale);

matrix3 new_xform = (matrix3)maketransform(XFORM_SRT, XFORM_XYZ, translate, rotate, scale);

3@old_xform = xform;
3@new_xform = new_xform;
```

## Integer to padded string

```c
sprintf('%04d',@Frame)
```

## Simulation Attributes

John Kunz has a great [list](https://mrkunz.com/blog/08_22_2018_VEX_Wrangle_Cheat_Sheet.html) of attributes used in simulations


## Attribute fade along curve
```c
float falloff = chf("falloff");
float offset = chf("offset");

float min = offset * (falloff + 1) - falloff;
float max = min + falloff;

f@value = fit(f@curveu, min, max, 0, 1);
v@Cd = f@value;
```

## Get number from node name
This isn't vex, but I always forget it.
```c
opdigits('.')
```


## Unique Values

Useful function for finding all the unique values a string or integer attribute has.

```c
int [] uniquevals(<geometry>geometry, string attribclass, string attribute_name)

string [] uniquevals(<geometry>geometry, string attribclass, string attribute_name)

```


## Ternary Conditional
```c
f@density = (f@density>0.01) ? 1.0 : 0.0; 
```

## Sample weighted 

[`sample_discrete()`](https://www.sidefx.com/docs/houdini/vex/functions/sample_discrete.html)

## Modulo Reference
To get a value from 0-1 that loops every 12 frames:
```c
f@cool = (f@Frame / 12) % 1
```

## Normalize attribute sweep between 0 and 1

I find it annoying to have to animate a parameter beyond 1 or below 0, so this lets you have a nice normalized parameter to animate.

```
    0                  1
    |__________________|
[   ]  ->  [    ]  ->  [    ]

```

Where `@mask` goes from 0-1:
```c
float radius = chf("radius");
float offset = chf("offset");

offset = fit(offset, 0, 1, 0, offset + radius);
f@mask = fit(f@mask, offset - radius, offset, 0, 1);
```
And a version with noise:
```c
float radius = chf("radius");
float offset = chf("offset");

float norm_y = relbbox(0, @P).y;
float noise = (noise(@P*chf("noise_scale")*chv("noise_scale_vector"))-.5)*1;
offset = fit(offset, 0, 1, 0, offset + radius);
float mask = fit(fit(norm_y + noise, 0, 1.75, 0, 1), offset - radius, offset, 0, 1);
```

## Animate point attribute sequentially

When you want only one point or a few points to animate at a time.

<!-- TODO: I think there's an off by 1 error here -->
```c
float overlap = chf("overlap");
float anim = chf("anim");

float range = (1-overlap) * (npoints(0) + 1)
float pt_range_start = ((1-overlap) * (npoints(0) - 1 - @ptnum));
f@amount = fit(anim, pt_range_start / range, (pt_range_start + 1) / range, 0, 1);

```

## PID POP Controller
```c
vector pid = chv("pid");

v@goal = point(1, "P", idtopoint(1, @ptnum%npoints(1)));

v@error = v@goal - v@P;

v@prev_error = (v@goal - v@pprevious) * @has_pprevious;
v@derivative = (v@error - v@prev_error)/@TimeInc;
v@integral = v@prev_integral + v@error * @TimeInc;

v@force = pid[0] * v@error + pid[1] * v@integral + pid[2] * v@derivative;

v@prev_integral = v@integral;
```
Links:
 - [PID without a PHD](http://www.wescottdesign.com/articles/pid/pidWithoutAPhd.pdf)
 - [PID control](https://www.robotsforroboticists.com/pid-control/)


## Find primitives in a bounding box

```c
int [] primfind(<geometry>geometry, vector min, vector max)
```

## Links
[VFXbrain has some great vex snippets](https://vfxbrain.wordpress.com/2016/10/02/vex-snippets/)

[Lots of great vex tricks](https://github.com/jtomori/vex_tutorial)