---
title: Digital Lines
date: 19-06-26
category: houdini
---

There are probably better ways to do this, but these are the two ways I came up with under a time crunch. Possibly useful to look at in the future. Would take further development to make them more useful.

### Pop Solution
![Digital Lines Pop](/assets/images/19-06-26-digital-lines-pop.png)

### Shortest Path Solution
![Digital Lines Short](/assets/images/19-06-26-digital-lines-short.png)

These create straight lines with many points along them. In order to reduce the number of points to just the corners you can use a `facet` sop and check `Remove Inline Points`.

### [Hip file download](/assets/projects/houdini/19-06-26-digital-lines.hip)
