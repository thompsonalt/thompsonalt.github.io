---
title: Weighted Random Attributes
date: 18-10-23
category: houdini
---

I wanted a way to scatter random objects to points in Houdini. This is simple enough if you want to have them randomly distributed, but what if you want more of some objects than others?

To solve this takes a two step process. First assign weights to each of the objects and make an array of those weights. Then use those weights to assign a random object to each point.

[Here](https://stackoverflow.com/questions/1761626/weighted-random-numbers) is the code I based my implementation on.

This asset is also a good demonstration of using the Multiparm Block folder.

### Set Weights
```c
f[]@choice_weights;

for(int i=1; i<=11; i++){
    @choice_weights[i] = chf(concat("element", itoa(i)));
}
```
### Create Weighted Attribute
```c
float choice_weights[] = detail(0, "choice_weights");
//printf("choice weights: %E", choice_weights);

float sum_of_weight = 0;
for(int i=1; i<len(choice_weights); i++) {
    sum_of_weight += choice_weights[i];
}
float rnd = rand(@ptnum*chf("seed"))*sum_of_weight;

int screen_num = 1;

//printf("sum of weight: %f", sum_of_weight);

for(int i=1; i<len(choice_weights); i++) {
//    printf("%s,%i", "iteration: ", i);
    if(rnd < choice_weights[i]){
        i@weighted_rand = i;
        return;
    }
    rnd -= choice_weights[i];
}
```

### [DOWNLOAD HDA](/assets/projects/houdini/com_carbonvfx__weighted_rand.hda.zip)