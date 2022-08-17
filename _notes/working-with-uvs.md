---
title: UV Workflows
date: 19-01-23
category: houdini
---

### Preserving UVs After Remeshing
There are a couple ways to acomplish this. One is to use the `splitpoints` node to break each point along a uv seam into two points. Then you can feed that into a remesh and fuse after the fact. A more direct method is to group the uv edges with `groupfromattributeboundary` and use that new edge group as the hard edge group in the remesh node. In either case, I usually disable recomputing normals. 

### Preserving UVs After VDB Conversion
The [Labs](https://www.sidefx.com/products/sidefx-labs/) toolkit has a great node for this called `uv_transfer`. You can transfer most of the attributes by plugging the original geometry into the second input of `convertvdb`, and then fix the UVs with `uv_transfer`. By default this node is very slow though. If you open up the node and compile the inner loop, it gets much faster.

[Side Effects Forum Post](https://www.sidefx.com/forum/topic/18890/)
[Another relevant post](https://www.sidefx.com/forum/topic/61928/?page=1#post-331565)
### [Hip Download](/assets/projects/houdini/19-01-23-remesh-preserve-uvs-v002.hiplc)

![Preserve UVs](/assets/images/19-01-23-preserve-uvs.gif)