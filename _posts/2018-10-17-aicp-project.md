---
title: Aicp Project
published: true
categories: houdini
date: 2018-10-17
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

### Links
[Copying and Instancing Point Attributes](http://www.sidefx.com/docs/houdini/copy/instanceattrs.html)

[RBD deintersect](http://www.tokeru.com/cgwiki/index.php?title=HoudiniDops)

[Object packing](https://vimeo.com/190660612)

[Tokuru Orient Vex](http://www.tokeru.com/cgwiki/index.php?title=JoyOfVex17)

[Richard Lord Dops Work](http://richardlord.tumblr.com/page/2)
