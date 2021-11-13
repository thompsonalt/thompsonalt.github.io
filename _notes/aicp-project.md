---
title: Aicp Project
category: houdini
date: 18-10-17
---

Finds the closest position to the surface of the geometry:
```javascript
@P = minpos(1, @P);
```

### [Quaternion to Euler](https://forums.odforce.net/topic/3440-quaternion-to-euler/)
```javascript
vector  qToE(vector4 q_value){
    float   q_0 = q_value.w ; 
    float   q_1 = q_value.x ; 
    float   q_2 = q_value.y ; 
    float   q_3 = q_value.z ; 
    vector  out = {0,0,0} ; 
            out.x = atan2(2*(q_0*q_1+q_2*q_3), (1-2*(q_1*q_1+q_2*q_2))) ; 
            out.y = asin(2*(q_0*q_2-q_3*q_1)) ;
            out.z = atan2(2*(q_0*q_3+q_1*q_2), (1-2*(q_2*q_2+q_3*q_3))) ;
    return out ; 
}
```

### Houdini's orient from vel equation
```javascript
@orient = quaternion(dihedral({0,0,1},@v));
```

### [Custom Slerp Formula](https://keithmaggio.wordpress.com/2011/02/15/math-magician-lerp-slerp-and-nlerp/)
```javascript
vector custom_slerp(vector start; vector end; float percent) {
     // Dot product - the cosine of the angle between 2 vectors.
     float dot = dot(start, end);     
     // Clamp it to be in the range of Acos()
     // This may be unnecessary, but floating point
     // precision can be a fickle mistress.
     //clamp(dot, -1.0f, 1.0f);
     // Acos(dot) returns the angle between start and end,
     // And multiplying that by percent returns the angle between
     // start and the final result.
     float theta = acos(dot)*percent;
     vector RelativeVec = end - start*dot;
     RelativeVec = normalize(RelativeVec);     // Orthonormal basis
     // The final result.
     return ((start*cos(theta)) + (RelativeVec*sin(theta)));
}

vector vec1 = {0,1,0};
vector vec2 = {0,0,1};

@N = custom_slerp(vec1, vec2, chf("bias"));
```
### Working @w Based POP Wrangle (needs refining)
I finally have something working. There's still some wiggly values going on, but I think it will just take some refining.
```javascript
vector4 first_orient = @orient;
vector4 second_orient = {0,0,0,1};

// Calculate orient from @up and @v
matrix3 transform = lookat(@v, 0, {0,1,0});
second_orient = quaternion(transform);

// Get the difference between the two quaternions
// https://stackoverflow.com/questions/1755631/difference-between-two-quaternions
vector4 transition = qmultiply(second_orient, qinvert(first_orient));

// Convert to Angle-Axis
// http://www.tokeru.com/cgwiki/index.php?title=JoyOfVex17#Convert_back_to_matrix
vector angle_axis = qconvert(transition);

@w = angle_axis*chf("strength");
```

### Easily Rotate a Vector Around an Axis
```javascript
matrix3 rot = qconvert(quaternion(chf("angle"), {0,1,0}));
@N = @N*rot;
```

### [This sounds very similar to the problem I'm having](https://stackoverflow.com/questions/2886606/flipping-issue-when-interpolating-rotations-using-quaternions)
>Remember, each rotation can actually be represented by two quaternions, q and -q. But the Slerp path from q to w will be different from the path from (-q) to w: one will go the long away around, the other the short away around. It sounds like you're getting the long way when you want the short way.
>
>Try taking the dot product of your two quaternions (i.e., the 4-D dot product), and if the dot product is negative, replace your quaterions q1 and q2 with -q1 and q2 before performing Slerp.

### [Great guide on using xyzdist and primuv together](http://www.toadstorm.com/blog/?p=465)
```javascript
int posprim;
vector param_uv;
float maxdist = 10;
float dist = xyzdist(0,@P,posprim,param_uv,maxdist);
vector goal_pos = primuv(0,"P",posprim,param_uv);
```

### Instancing from Houdini to Maya
The most challenging aspect of this project was finding a way to instance Maya objects using the Houdini Engine, but remove Houdini Engine from the files sent to the farm. This was in order to save money on Houdini licenses.

#### Steps:
- Create low resolution geometry for Houdini and make sure the object is centered in world space in Houdini and Maya.
- Sim that geometry in Houdini. Make sure to disable `Compute Center of Mass` in the rigid body packed object. Also, when fetching out of the DOP network, make sure to `Fetch Geometry from DOP Network` instead of fetching packed geometry. Also, preserve an attribute that describes which object that point refers to for Maya.
- Write those points to disk as bgeo files
- Create an HDA that converts the orient attribute on those points to euler rotation values for Maya.
- After importing that HDA into Maya, use `nCache>Create New Cache` to cache those points.
- In Maya, create an nParticleSystem and geoInstancer with the Maya objects layed down in the same order as the attribute out of Houdini.
    - Add the rotation, scale and object id attributes using `Modify>Add Attribute`
    - Choose the correct data type and "Per particle" as the Attribute type.
- Attach that newly created cache to the nParticle system you created.
- Remove the Houdini Engine object from the scene before rendering.

Confusing and many gotchas, but in the end it was pretty stable. Here are some files for reference:
- [Example Maya File](/assets/projects/maya/18-11-16-example-maya-instancer.ma)
- [Example HDA](/assets/projects/houdini/18-11-16-example-hda.hda)

### Links
[Copying and Instancing Point Attributes](http://www.sidefx.com/docs/houdini/copy/instanceattrs.html)

[RBD deintersect](http://www.tokeru.com/cgwiki/index.php?title=HoudiniDops)

[Object packing](https://vimeo.com/190660612)

[Tokuru Orient Vex](http://www.tokeru.com/cgwiki/index.php?title=JoyOfVex17)

[Richard Lord Dops Work](http://richardlord.tumblr.com/page/2)

[Good stuff about orient](https://www.sidefx.com/forum/topic/53253/)

[Centering the Pivot](https://forums.odforce.net/topic/29350-custom-pivot-location-on-packed-primitives/)

[Tokuru Grain Ropes](http://www.tokeru.com/cgwiki/index.php?title=HoudiniDops#Grain_solver_for_hair)


### [Download Sample Hip](/assets/projects/houdini/18-11-16-AICP-project.hip)