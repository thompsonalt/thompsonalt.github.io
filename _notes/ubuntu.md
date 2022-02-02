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