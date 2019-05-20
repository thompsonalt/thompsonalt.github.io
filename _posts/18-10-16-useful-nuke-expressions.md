---
title: Useful Nuke Expressions
layout: note
date: 18-10-16
categories: nuke
---

### Set a write node based on the read node at the top of the pipe
```
[file dirname [knob [topnode].file]]/jpg/[file rootname [file tail [knob [topnode].file]]].jpg
```
The `[topnode]` is the key word. I use `[file rootname]` in this case just to strip the extension. More complex operations would require a `[split]`.

### Links:
[Heavyimage Nuke python / tcl snippits](http://kb.heavyimage.com/notes/nuke/python/snippits/software/tutorial/vfx/nuke)

[Lookin Nuke TCL Snippets](http://www.lookinvfx.com/nuke-tcl-snippets/)

[Adam Teale's Nuke Snippets](http://adamteale.com/some-nuke-python-snippets/)

[Cameron Carson's Wave Expressions](https://www.cameroncarson.com/nuke-wave-expressions/)
