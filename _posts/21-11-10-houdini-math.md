---
title: math.h
layout: note
categories: houdini
---

## Snippets from math.h

`$HFS/houdini/vex/include/math.h`

```
// Defines for the maketransform() VEX function.  The function takes two
// integer arguments which determine the order that the transform gets made.
#define XFORM_SRT	0	// Scale, Rotate, Translate
#define XFORM_STR	1	// Scale, Translate, Rotate
#define XFORM_RST	2	// Rotate, Scale, Translate
#define XFORM_RTS	3	// Rotate, Translate, Scale
#define XFORM_TSR	4	// Translate, Scale, Rotate
#define XFORM_TRS	5	// Translate, Rotate, Scale

#define XFORM_XYZ	0	// Rotate order X, Y, Z
#define XFORM_XZY	1	// Rotate order X, Z, Y
#define XFORM_YXZ	2	// Rotate order Y, X, Z
#define XFORM_YZX	3	// Rotate order Y, Z, X
#define	XFORM_ZXY	4	// Rotate order Z, X, Y
#define XFORM_ZYX	5	// Rotate order Z, Y, X

// Defaults TRS and XYZ orders for bones
#define BONE_TRS_ORDER 0
#define BONE_XYZ_ORDER 5

// Defines for rotate() prerotate() that take an axis argument.
#define XAXIS	1
#define YAXIS	2
#define ZAXIS	4

// Defines for cracktransform() component argument
#define CRACK_T	0
#define CRACK_R	1
#define CRACK_S	2
#define CRACK_SHEARS 3
#define CRACK_R_DEGREES	1
#define CRACK_R_RADIANS	4
```

## Math constants

**Note**: This has been modifed from the original file for brevity

```
#define M_E		2.7182818
#define LN10		2.3025850
#define LN2		0.6931471
#define LOG10E		0.4342944
#define LOG2E		1.4426950
#define PI		3.1415926
#define M_TWO_PI	6.2831852
#define PI_2		1.5707963
#define PI_4		0.7853981
#define SQRT1_2		0.7071067
#define SQRT2		1.4142135
#define TOLERANCE	0.0001

#define M_2SQRT6_3	1.6329931618554518	// 2 * sqrt(6) / 3
#define M_SQRT3		1.7320508075688772	// sqrt(3)
#define M_1_SQRT3	0.5773502691896257	// 1 / sqrt(3)
#define M_SQRT_2_3	0.816496580927726	// sqrt(2 / 3)
```