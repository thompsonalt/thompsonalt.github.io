---
layout: note
title: Crowd Simulations
date: 2019-01-03
categories: 
    houdini
---

### Important note on importing animations from Mixamo
This is an annoying one... It turns out, if you download an FBX from [Mixamo](https://www.mixamo.com/) and import it into Houdini using the FBX importing tool it leaves off frame zero of the animation. This is unfortunate because houdini expects the first and last frames of a looping agent animation to be identical. To work around this, I ended up importing the FBX out of Mixamo into Maya, offseting all the animation one frame forward, and re-exporting the FBX. 

**To offset all the animation in an FBX forward in Maya:**
- Import FBX and select it in the Outliner
- `[Select > Hierarchy]` to select all the keyframes
- Shift, left click and hold the first frame of the animation on the timeline and drag to the end.
- Grab the arrows in the center of the red selection area and drag one frame to the right.
- Re-export the FBX with `[File > Export All]`

[Example Hip Download](/assets/projects/houdini/19-01-23-crowds-example.hip)

## Links

[Short and Sweet 3D video on foot locking and basics](https://www.youtube.com/watch?v=CIgTqZBtMwY)

[Tokoru, as usual, has invaluable information](http://www.tokeru.com/cgwiki/index.php?title=HoudiniCrowd)

[Masterclass on 15.5 crowds](https://vimeo.com/178031369)

[Masterclass on 15 crowds](https://vimeo.com/150917240)

[Masterclass on stylsheets](https://vimeo.com/155876134)