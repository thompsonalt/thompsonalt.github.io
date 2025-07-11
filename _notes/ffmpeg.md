---
title: FFMpeg
date: 21-10-21
category: command-line
---

## Video to image sequence

```
ffmpeg -i .\input.mp4 -start_number 1001 output_v01/output_v01_%04d.png
```
Note that this won't autuomatically make folders.

## Rotating video

```
ffmpeg -i .\input.mp4 -vf "transpose=1" output.mp4
```

* 0 - Rotate by 90 degrees counter-clockwise and flip vertically. This is the default.
* 1 - Rotate by 90 degrees clockwise.
* 2 - Rotate by 90 degrees counter-clockwise.
* 3 - Rotate by 90 degrees clockwise and flip vertically.

[Source](https://ostechnix.com/how-to-rotate-videos-using-ffmpeg-from-commandline/)

## Converting videos

Converting audio and video is as smiple as choosing a filename with a new extension.

```
ffmpeg -i input.mp4 output.webm
```