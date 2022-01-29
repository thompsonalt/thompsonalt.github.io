---
title: Camera Space Transform
date: 22-01-28
category: houdini
---

Drop this in a wrangle to transform geo in screen space.


```
string cam = chs("cam");
vector2 cam_res = chu("camera_resolution");

vector ndc = toNDC(cam, @P);

// Make a vector that will be used to normalize the offset
vector norm_cam = (vector)cam_res;
norm_cam[2] = 1;

vector offset = chv("offset") / norm_cam;
ndc += offset;

@P = fromNDC(cam, ndc);
```

TODO: Add pivot, rotation, and viewport handles