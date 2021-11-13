---
title: Houdini Constraints
date: 19-12-17
category: houdini
---

## Gyroscope Example

<video width="700" loop autoplay>
  <source src="/assets/images/19-12-17-gyroscope.mp4" type="video/mp4">
</video>

This is a project I did in order to learn the basics of constraints in Houdini. I learned a lot from the creations of Richard Lord [here](https://richardlord.tumblr.com/) and [here](https://forums.odforce.net/topic/25124-learning-dops-motors-constraints-etc/).

One place I got tripped up on was figuring out how to do an angular motor on the Y axis. As soon as I changed axis 1 to `[0,1,0]` the geo connected to it would disappear. It turns out that by default Axis 2 is set to `[0,1,0]`. Even though it's grayed out, the solver still uses that value somehow. To fix this, temporarily change the number of motors to 2, change the vector to a different direction, and drop the motors back down to one again.

![Digital Lines Short](/assets/images/19-12-17-angular-motor.png)

### [Hip Download](/assets/projects/houdini/19-12-17-gyroscope.hip)