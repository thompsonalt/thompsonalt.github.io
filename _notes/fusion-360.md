---
title: Fusion 360
date: 22-05-15
category: fusion360
---

## Shortcuts

| Shortcut          | Description 
| -                 | -
| s                 | Design Shortcuts
| l                 | Line
| i                 | Measure
| q                 | Press Pull
| f                 | Fillet
| lmb (long press)  | Selection list
| hold Shift        | Lock midpoint
| hold Ctrl         | [Lock face selection](https://youtu.be/zonnR575Xkc?t=1177)

---

<!-- TODO: Fix table formating -->

> TIP: Using design shortcuts you can search for "Change Parameters" to bring up the parameter menu

### Dimmensions
Select the lines, points, or arcs holding Ctrl and hit 'd'

### Dimmension from Circle Tangent
Normally when setting a dimmension between a circle and anything else, it will default to the center of the circle. To define from the edge of the circle, right click and select "Pick Circle/Arc Tangent".


### 3D Printing Clearance [Table](https://youtu.be/zonnR575Xkc?t=1290)

- **Press fit:**    .05mm - .15mm
- **Snug fit:**     .25mm
- **Slip fit:**     .35mm

The best tool for the job is the [Press Pull](https://youtu.be/FzCm1iTf8PA?t=1275) tool.

### Mirroring

A handy way to mirror features is to not click on the features in the viewport, but instead click on the relevant extrudes in the timeline.

### Import STLs

 - Solid > Insert > Insert Mesh
    - Pick correct [units](https://knowledge.autodesk.com/support/fusion-360/troubleshooting/caas/sfdcarticles/sfdcarticles/Imported-STL-file-into-Fusion-360-is-10x-larger-than-original.html)
- [Disable design history](https://youtu.be/pgWWVcM5YJY?t=397) to enable BRep conversion
- [Convert to BRep](https://youtu.be/zonnR575Xkc?t=1979)
- Delete mesh body
- One way to fix triangular mesh is to [click and delete](https://youtu.be/pgWWVcM5YJY?t=579) faces
- Another option:
    - Move to Surface tab
    - Select faces and [use merge command](https://youtu.be/zonnR575Xkc?t=2003)
    - This fixes many faces at once
- Two options for fixing curves:
    - [Product Design Online's method](https://youtu.be/pgWWVcM5YJY?t=638)
    - [Team Small Robot's method](https://youtu.be/zonnR575Xkc?t=2087)

### Joints

Always make sure you have your main component 'grounded'. Right click in the browser and select 'Ground'.