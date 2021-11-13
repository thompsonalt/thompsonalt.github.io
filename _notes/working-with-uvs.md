---
title: Working With UVs
date: 19-01-23
category: houdini
---

### Preserving UVs After Remeshing
This has been bothering me for a while. Fixing the pesky seams that come up when using vertex UVs can be a pain. A great tool to fix this is the `vertex split` node. This creates new points at vertex where an attribute differs by more than a specified amount. If you choose the uv attribute, it'll create new points at the uv seams and promote it to a point attribute. When you remesh at this point the UV seams won't be aparent and you can promote the UVs to a vertex attribute and fuse the points to get it back to vertex uvs.

[Side Effects Forum Post](https://www.sidefx.com/forum/topic/18890/)
### [Hip Download](/assets/projects/houdini/19-01-23-remesh-preserve-uvs.hip)

![Preserve UVs](/assets/images/19-01-23-preserve-uvs.gif)