---
title: SSH
date: 21-12-29
category: command-line
---

## ssh-keygen

Setting up ssh starts with ssh-keygen. You run this script on the client computer to generate public `id_rsa.pub` and private `id_rsa` keys and put them in your ssh directory `~/.ssh`. This works the same on Windows and Linux.

## ssh-copy-id

The next step is appending that public key to the host computer's `authorized_keys` file. On linux there's a convenient sccript called `ssh-copy-id` for this. 

```
ssh-copy-id -i ~/.ssh/id_rsa.pub user@host
```

Windows doesn't have a script for this, so we have to do it [manually](https://serverfault.com/questions/224810/is-there-an-equivalent-to-ssh-copy-id-for-windows):

```
cat ~/.ssh/id_rsa.pub | ssh user@host "cat >> ~/.ssh/authorized_keys"
```

Or if the `.ssh` directory doesn't yet exist on the host:

```
cat ~/.ssh/id_rsa.pub | ssh user@host "mkdir ~/.ssh; cat >> ~/.ssh/authorized_keys"
```