---
title: Centos Notes
layout: note
date: 19-06-23
categories: linux
---

# Changing Grub's Default
This took me a while to figure out. Probably because I was using the instructions for BIOS-based instead of UEFI-based machines. Here's a link to the info ([CUSTOMIZING THE GRUB 2 CONFIGURATION FILE](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sec-customizing_the_grub_2_configuration_file)), but I'll lay out the key points below.

First, find the grub config file here: `/etc/default/grub`. This stores settings for grub. We need to change `GRUBDEFAULT`. By default the setting is "saved" which means it will use the last kernel installed. If you would like to default to a specific system, list the systems with this command: 
```
awk -F\' '$1=="menuentry " {print $2}' /etc/grub2.cfg
```
Copy the output of that command to the `GRUBDEFAULT` setting. Now we need to rebuild grub.cfg.

grub.cfg lives in a different place depending on if you're on a bios system or a uefi system. Here are the commands for rebuilding grub.cfg:

- On BIOS-based machines, issue the following command as root:
    ```
    grub2-mkconfig -o /boot/grub2/grub.cfg
    ```
- On UEFI-based machines, issue the following command as root:
    ```
    grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg
    ```
> **NOTE**: Notice how 'centos' is defined instead of 'redhat'