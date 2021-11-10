---
title: Raspberry Pi Headless Setup
layout: note
categories: electronics
---

1. Install [Raspberry Pi Imager](https://www.raspberrypi.com/software/), and follow the simple steps to install the OS.

2. Add `wpa_supplicant.conf` to the root of the SD card to automatically connect to wifi.

    ```
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
    scan_ssid=1
    ssid="wifi-name"
    psk="password"
    }
    ```

3. Add an empty file called `ssh` to the root to enable SSH.

4. After booting Raspberry Pi, connect via SSH.

    `ssh pi@raspberrypi.local`

    **Default settings**

    - hostname :    raspberrypi
    - user:         pi
    - pass:         raspberrypi

5. Run `raspi-config` to change hostname and password. Also consider expanding the file system under 'Advanced'.

6. Update

    ```
    sudo apt update -y
    sudo apt upgrade -y
    ```

## Troubleshooting

* Restart the router
* Connect via USB to computer