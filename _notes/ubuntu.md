---
title: Ubuntu
date: 22-02-02
category: linux
---

## Single application session

```
cd /usr/share/xsessions
sudo nano appname.desktop
```

.desktop contents:
```
[Desktop Entry]
Type=Application
Exec=executable-name
Name=Application Name
Comment=Launch just this application
```

Then restart. You'll see it as an option in the lower right after selecting your user.

## Where to install software

An excerpt from a [stack exchange](https://askubuntu.com/questions/130186/what-is-the-rationale-for-the-usr-directory) post:

> The above list is already half the answer of you Oracle JDK question, at least it gives several clues. The checklist to "Where should I install software X?" goes by:
>
> - Is it a completely self-contained, single directory software, like Eclipse IDE and other downloaded java apps, and you want it to be available to all users? Then install in `/opt`
>
> - Same as above, but you don't care about other users and I want to install for your user alone? Then install in `~/.local/opt`
>
> - Its files split over multiple dirs, like bin and share, like traditional software compiled and installed with `./configure && make && sudo make install`, and should be available to all users? Then install in `/usr/local`
>
>- Same as above, but for your user only? Then install in `~/.local`
>
> - Software installed by the OS, or via package managers (like Software Center), and, most importantly, which any local modification might be overwritten when update manager upgrades it to a new version? It goes to `/usr`