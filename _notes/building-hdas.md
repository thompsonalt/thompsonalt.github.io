---
title: Building HDAs
date: 18-11-16
category: houdini
---

To get the current node use `hou.node('.')` or `hou.pwd()`

To press a button deeper in the HDA use the following:
```python
hou.parm("./deadline_submit1/submit").pressButton()
```
[Nick Pfeiffer explains this well.](http://nicholaspfeiffer.com/blog/2016/2/20/houdini-tip-of-the-day-python-pressbutton-and-set-commands)

If you have a function in the asset's python module you'd like to access, use the following:
```python
hou.node(".").hdaModule().random_function()
# or...
hou.pwd().hm().random_function()
```
To get current node in a callback:
```python
kwargs.get("node")
```

[Link to Side Effects help](http://www.sidefx.com/docs/houdini/hom/hou/HDAModule.html)

### [Add Parameter to Existing Folder](https://www.sidefx.com/forum/topic/20361/?page=1#post-95571)

```python
n = hou.node('/out/renderNode3')
parm_group = n.parmTemplateGroup()
target_folder = parm_group.findFolder((“Passes”,))
hou_parm_template2 = …
hou_parm_template3 = …
target_folder.addParmTemplate(hou_parm_template2)
target_folder.addParmTemplate(hou_parm_template3)
n.setParmTemplateGroup(parm_group)
```

### Add Vexpression To HDA

```c
{
`ifs(ch('../use_vex', chs('./preproc_vex')))
}
```

### Reference embedded 'extra files

You can embed files into an HDA through type properties > Extra Files. 

For [referencing those files](https://www.sidefx.com/docs/houdini/assets/opdef.html) from within the HDA, use the following syntax:

```
opdef:..?default_texture.jpg
```

**Note:** The `..` is a relative path to the HDA root. If this parameter is on the HDA itself and not inside it, it would just be `opdef:.?default_texture.jpg`

This syntax is often used for [HDA Icons](https://www.sidefx.com/docs/houdini/ref/windows/optype#basic)