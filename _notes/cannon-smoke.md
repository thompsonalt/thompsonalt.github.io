---
title: Cannon Smoke
date: 18-10-15
category: houdini
---
This is the code to produce the velocity field for the smoke. Making the smoke travel a long distance without pluming is crux of the challenge. Having a large velocity field solves this problem to some extent.

```c
float dist = length(set(@P.x, @P.y, 0));
float norm_dist = fit(dist, 0.0, chf("max_dist"), 0.0, 1.0);
float remap_dist = chramp("remap_dist", norm_dist);
float z_max = chf("z_max");
float norm_z = fit(@P.z, z_max, 0, 0, 1);
float z_falloff = chramp("z_remap", norm_z);
float noise_falloff = chramp("noise_falloff", norm_z);

vector noise = curlnoise(@P*chf("noise_scale"))*chf("noise_amp");
vector noise_scaled = noise*noise_falloff;

vector towards_center = normalize(set(@P.x, @P.y, 0));
float diverge = chramp("diverge", norm_z);
@vel = lerp(@vel, towards_center, diverge);

@vel = @vel*remap_dist*z_falloff+noise_scaled;
```
Here is a screenshot of the setup:

![Cannon Vel Screenshot](/assets/images/18-10-15-cannon-source-vel.PNG)

### [Hip file download](/assets/projects/houdini/18-10-16-cannon-smoke.hip)

### Links
[Jeff Wagner's tips on preventing mushrooming](https://forums.odforce.net/topic/18397-get-rid-of-mushroom-effect-in-explosion-and-add-details-in-the-opening/)
