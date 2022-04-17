---
title: Raspberry Pi Headless Setup
category: electronics
date: 21-11-10
---

1. Install [Raspberry Pi Imager](https://www.raspberrypi.com/software/), and follow the simple steps to install the OS. You can skip the next two steps if you use the gear icon in the bottom right corner (or `Ctrl + Shift + X`) to configure the Pi. In fact, if you're installing the "Lite" version, you **must** configure it this way.

### [Raspberry Pi Imager](https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager)

>If you are installing Raspberry Pi OS Lite and intend to run it headless, you will still need to create a new user account. Since you will not be able to create the user account on first boot, you MUST configure the operating system using the Advanced Menu.

2. Add `wpa_supplicant.conf` to the root of the SD card to automatically connect to wifi. For the Zero 2W, this must be **2.4 gigahertz**.

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
    - pass:         raspberry

5. Run `raspi-config` to change hostname and password. Also consider expanding the file system under 'Advanced'.

6. Update

    ```
    sudo apt update -y
    sudo apt upgrade -y
    ```

## Troubleshooting

* **Restart the router**
* Connect via USB to computer