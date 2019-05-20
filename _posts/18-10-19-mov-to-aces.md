---
title: Mov Gamma 1.8 to Aces Workflow
layout: note
categories: nuke
date: 18-10-19
---
Aces doesn't have a built in way to convert gamma 1.8, so we have to use a work around in Nuke. This is helpful for bringing Mov elements into a Aces comp.

{% raw %}
```
set cut_paste_input [stack 0]
version 11.1 v4
Read {
inputs 0
file V:/Jobs/182344_Army/Design/Production/Path/Shots/Common/Elements/Footage/FX/ActionEssentials/18_Shells/8mm_03.mov
format "2048 1152 0 0 2048 1152 1 "
last 91
frame_mode "start at"
frame 1001
origlast 91
origset true
version 13
colorspace Gamma1.8
raw true
mov32_codec {{0} "Apple PNG (appl - png )"}
mov32_pixel_format {{0} "default (RGBA  8-bit)" "RGBA  8-bit"}
name Read14
selected true
xpos -94
ypos 2996
}
Colorspace {
colorspace_in 1.80
name Colorspace1
selected true
xpos -94
ypos 3094
}
OCIOColorSpace {
in_colorspace "Utility - Linear - Rec.709"
out_colorspace "ACES - ACEScg"
name OCIOColorSpace1
selected true
xpos -94
ypos 3120
}
```
{% endraw %}

- Read in the Mov as raw
- Convert from Gamma1.8 to Linear with a colorspace node
- Convert from Utility - Linear - Rec.709 to ACES - ACEScg with a OCIOColorSpace node
- Profit

Courtesy of [Ryan Quinlan](https://rjqfx.com)