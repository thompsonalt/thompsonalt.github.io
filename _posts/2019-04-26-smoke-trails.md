---
layout: note
title: Smoke Trails
date: 2019-04-26
categories: 
    houdini
---

### Distributed Simulation
For my first attempt at smoke trails I used a pyro simulation. For shots that get close to camera I think this is the way to go. The difficulty becomes the sheer size of the simulation volumes. This is where distributed simulations come in handy. This way, a source volume can pass smoothly from one volume box to another without creating seams. In fact, a method of distribution called **clustering** allows all the parts of the simulation to run at the same time since they do not affect each other. 

Vimeo user [Tighe Rzankowski](https://vimeo.com/trzanko) has a great tutorial on clustering, though my approach ended up being significantly different.

### Procedural
The system I ultimately ended up using was completely procedural. A useful technique used in this approach was assigning a frame number to the points on the curve corresponding to where the object was on that frame. This can be used to calculate how much time has passed since the object was in that position. Also, clustering the smoke and isolating the smoke to just what the camera could see significantly reduced computation time.


### [Hip Download](/assets/projects/houdini/19-04-04-distributed-smoke.hip)

![Preserve UVs](/assets/images/19-04-26-distributed_smoke.png)