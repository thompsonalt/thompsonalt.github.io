---
title: Rendering Lines
layout: note
categories: houdini
---

This [Odforce post](https://forums.odforce.net/topic/27668-mantra-glowing-points-and-fake-dof-fake-light-emitting/), particulary the file provided by MENOZ, describes how to render additive lines in Houdini with a falloff on the edges.

An important note, when you set Surface Opacity (`Of`) to 0 in the shader, you have to disable stochastic transparency in the Mantra node. If you need to keep that enabled, you can set `Of` to a very low constant and get a similar result. 

Also, the modern `uvcoords` node uses *u* and *v* instead of *s* and *t* like the example file. *u* is the component you want for falloff on the edges. 

**TODO:** Add example Houdini file