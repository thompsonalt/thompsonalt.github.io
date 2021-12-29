---
title: Mantra Notes
category: houdini
date: 21-11-12
---

## Rendering Lines

This [Odforce post](https://forums.odforce.net/topic/27668-mantra-glowing-points-and-fake-dof-fake-light-emitting/), particulary the file provided by MENOZ, describes how to render additive lines in Houdini with a falloff on the edges.

An important note, when you set Surface Opacity (`Of`) to 0 in the shader, you have to disable stochastic transparency in the Mantra node. If you need to keep that enabled, you can set `Of` to a very low constant and get a similar result. 

Also, the modern `uvcoords` node uses *u* and *v* instead of *s* and *t* like the example file. *u* is the component you want for falloff on the edges. 

**TODO:** Add example Houdini file


## Render State VOP

Sometimes you need to access render time attributes within a shader. The main usecase for this is accessing *primitive* attributes on packed primitives. Lay down a renderstate node, and add `packed:your_attribute` to the value name. The dropdown has a bunch of useful options as well.

## Cryptomatte Pieces

Lewis Saunders has a great [overview](https://lewisinthelandofmachines.tumblr.com/post/176559578118/houdini-per-piece-cryptomatte-mantra-support-for) of how to apply cryptomatte to pieces inside a geo node in Mantra.

In short: 
- Add `vm_gifile` render property to your material
- Where you assign your material add a local override. Enable `Overrides use local variables` and select `vm_gifile` from the `Choose Parameter` dropdown. Put `$NAME` or another unique primitive attribute as the string.
- Add a Cryptomatte layer to the Mantra ROP and set the property to `gifile`