---
title: Houdini Cameras
layout: note
date: 19-11-22
categories: houdini
---

To calculate the horizontal and verticle FOV for Houdini's cameras:
Horizontal:
```
2*atan(ch("aperture")/(2*ch("focal")))
```
Vertical:
```
2*atan(ch("aperture")*(ch("resy")/ch("resx"))/(2*ch("focal")))
```

To calculate how many pixels wide a given particle is (assumes square pixels):
``` javascript
float horizontal_fov = chf("horizontal_fov");
float vertical_fov = chf("vertical_fov");
int horizontal_res = chi("horizontal_res");
int vertical_res = chi("vertical_res");
int iteration = detail(-1, "iteration", 0);
vector cam_pos = point(1, "P", 0);

float distance = distance(cam_pos, @P);
f@distance = distance;
float width_of_frame =  2*distance*tan(radians(horizontal_fov)/2);
f@width_of_frame = width_of_frame;
f@pixel_width = width_of_frame/horizontal_res;
f@pixels = @pscale/f@pixel_width;
```