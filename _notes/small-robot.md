---
title: Small Robot Notes
category: electronics
date: 21-11-07
---

## Motors

### Small Motor Sizes/Types:

[**N20**](https://www.adafruit.com/product/4638)

[Pololu Micro Metal Gearmotors](https://www.pololu.com/category/60/micro-metal-gearmotors) |
[Bringsmart N20 Micro motor](https://www.aliexpress.com/item/32910935772.html) | 
[DC N20 Mini Micro Metal Gear Motor](https://www.aliexpress.com/item/32991622456.html) | 
[uxcell DC 3V 0.2A 100RPM Gear Box Geared Motor](https://www.amazon.com/uxcell-100RPM-Geared-Motor-Project/dp/B0080DNBPK/) |
[uxcell 300RPM 6V 0.45A](https://www.amazon.com/gp/product/B0080DOEQU/) 

![](/assets/images/21-11-07-n20-motor.png)

[**130 Size**](https://www.adafruit.com/product/711)

![](/assets/images/21-11-07-130size-motor.png)

[**TT motors**](https://www.adafruit.com/product/3777)

![](/assets/images/21-11-07-tt-motor.png)

[**NEMA-8 (Stepper motor)**](https://www.adafruit.com/product/4411)

![](/assets/images/21-11-07-nema8-motor.png)


### Universal Mounting Hubs

[Pololu Universal Mounting Hubs](https://www.pololu.com/category/137/pololu-universal-mounting-hubs)

To attach something to the shaft of a motor, you can use a universal mounting hub of the correct diameter. 

![](/assets/images/21-11-07-universal-mounting-hub.png)


### Acceptable RPM

With 2" diameter wheels, a 60 rpm motor could drive the robot at 6.2" per second. That seems like a reasonable speed. But 2" wheels might be just slightly large on the size of robot I'd like to build, and it wouldn't give much headroom for speed bursts. I think I'll be looking for around 80-150 rpm motors after gear ratio.

## Circuits

### Possible Microcontrollers

[Adafruit ItsyBitsy nRF52840 Express - Bluetooth LE](https://www.adafruit.com/product/4481)

This one has bluetooth built in, supports CircuitPython and Arduino IDE, and is extremely small (1.4" x .7"). I was worried about the LE version of bluetooth, but from some breif research it looks like it can have latency as low as 7ms, so that shouldn't be an issue.

[Adafruit Guide](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/)

Another bonus for this board is that Adafruit makes a [backpack](https://www.adafruit.com/product/2124) for it that allows for charging LiPoly batteries through the already built in USB port on the board. This board charges at 100mA by default, but can be adjusted to 500mA by soldering a jumper. Note, it also covers the reset button on the board.

### Motor Controllers / Motor Drivers

[DRV8833 Dual Motor Driver Carrier](https://www.pololu.com/product/2130)

## Batteries

Adafruit has a great [overview](https://learn.adafruit.com/li-ion-and-lipoly-batteries/overview) on lipo batteries that's a great reference. They have another entire guide about [charging](https://learn.adafruit.com/multi-cell-lipo-charging) multi-cell LiPos.

I haven't yet done calculations for how much battery capacity I'll need. I'm considering betweein [500mAh](https://www.adafruit.com/product/1578) and [1200mAh](https://www.adafruit.com/product/258). Or even higher at  [2500mAh](https://www.adafruit.com/product/328). All of these are tiny and will easily fit in the robot. I'm afraid the small ones will die far too quickly, but the large ones will take some time to charge. Will have to do some more research. 

For something more power hungry than a microcontroller like the Raspbery Pi Zero 2W, it might be necessary to go even larger: [Lithium Ion Battery Pack - 3.7V 4400mAh](https://www.adafruit.com/product/354)

### Chargers:

Hopefully charging can be integrated into the design of the robot. It will be helpful to have an external charger for testing purposes. Here are a couple:

[Adafruit Micro Lipo - USB LiIon/LiPoly charger - v1](https://www.adafruit.com/product/1304)

[USB LiIon/LiPoly charger - v1.2](https://www.adafruit.com/product/259)

[iMAX B6AC V2 Balance Charger and Discharger](https://www.pololu.com/product/2588)


### Wire Connectors 

A common type of connector used for batteries and often disconnected wires is "jst". 

![](/assets/images/21-11-07-jst-connector.png)

"Raw jumper wires" have exposed crimped ends like this:

![](/assets/images/21-11-07-jumperwire-female.png)
![](/assets/images/21-11-07-jumperwire-male.png)

You can buy them premade or buy a crimping tool to make your own. For organization, you clip them into single or dual row housings. I've also heard these called "Dupont connectors"

![](/assets/images/21-11-07-jumper-housing.png)

