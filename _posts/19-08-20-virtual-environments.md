---
title: Virtual Environments
layout: note
date: 19-08-20
categories: python
---

A virtual environment is an set of modules and dependencies isolated from the system as a whole. In this way you can set up different virtual environments for different tasks. Say one python project requires python 3.4 while another requires 2.7. You could configure an environment for each of them and run each project in its respective environment. 

For python, I've had good luck using the Anaconda environment manager. For the most part it just works, though not without some hiccups. 

## Configuring Anaconda Environments in Visual Studio Code
There are a couple things we have to do to make Anaconda work seamlessly inside VS Code. When installing Anaconda or miniconda I recommend adding it to the path, even though that's disabled by default in the latest versions of Anaconda. Then...

### Define Python version when creating environment
First of all, when you create an Anaconda environment you plan to use in vscode, be sure to define the python interpreter explicitly:

```
conda create -n myenv python=2.7
```

`-n myenv` defines the name of the environment.

Without explicitly defining the python version, visual studio code won't be able to find it when searching for python interpreters. 

### Select the python interpreter from VS Code
Use `Ctrl + Shift + P` and type "Python: Select Interpreter". You should see a list of environments to choose from if you did the previous step correctly.

### Enable Anaconda for Powershell
By default, Anaconda is missing some functionality in powershell (which is vscode's default console on Windows). You'll know you have a problem when it has DLL Load errors:

```
Exception has occurred: ImportError
DLL load failed: The specified module could not be found.
```

What's happening is VS Code may technically be activating your anaconda environment before running your script, but it's not defining some extra paths it needs. You can verify this by printing the path in the anaconda prompt, and in the VS code terminal. You'll notice some discrepancies. To fix this I had to enable anaconda in powershell.

```
conda init powershell
```

See [here](https://stackoverflow.com/questions/47800794/how-to-activate-different-anaconda-environment-from-powershell).


The first time you run your scripts you'll always still get that error. VS code then does `conda activate myenv` and fixes it for the next time you run it.

Another useful link for setting up vscode with anaconda: [How to Activate Conda Environment in VS Code](https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d)


## Pip Reference

To install a python package to a specific location use ```--target```. ([Source](https://stackoverflow.com/questions/2915471/install-a-python-package-into-a-different-directory-using-pip))

```
pip install --target=d:\somewhere\other\than\the\default package_name
```

To force upgrade a package use ```--upgrade```
```
pip install Django --upgrade
```