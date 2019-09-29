PandaCoreData [![Build Status](https://travis-ci.org/Cerberus1746/PandaCoreData.svg?branch=master)](https://travis-ci.org/Cerberus1746/PandaCoreData) [![Documentation Status](https://readthedocs.org/projects/pandacoredata/badge/?version=stable)](https://pandacoredata.readthedocs.io/en/latest/?badge=stable) [![Coverage Status](https://coveralls.io/repos/github/Cerberus1746/PandaCoreData/badge.svg?branch=master)](https://coveralls.io/github/Cerberus1746/PandaCoreData?branch=master) [![PyPI version](https://badge.fury.io/py/panda-core-data.svg)](https://pypi.org/project/panda-core-data/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/panda-core-data)](https://www.python.org/downloads/)
=========

So, if you already played games like Factorio, Rimworld or Dwarf Fortress and tried to mod them,
you will find that it’s absurdly easy to mod those games for simple things like changing the
balancing, adding items, changing descriptions and etc. Because the data files of the games are
simple raws and not binaries. This library pretty much makes the task of using raws as simple as
possible. Raws in our case is plain text files like xml, json, yaml and etc that
is commonly used to hold data, for now the library supports `yaml` and `json`.

The library might have modding in mind, however it pretty much be used for any sort of software or
game engine that uses python.

Internally the library use [dataclasses](https://docs.python.org/3/library/dataclasses.html>) to
handle the data and [TinyDB](https://tinydb.readthedocs.io/en/latest/) to load them from raws.

Thanks for your interest in our package! But for now our things are still a bit of a todo. But, you
can check a basic api documentation here: https://pandacoredata.readthedocs.io/

# Install

This package only works with python 3.7 and above because it uses dataclasses.

The package is now available with pip, so to install all you need is to run this command:
```
pip install panda-core-data
```

# Quick Start

Once installed, you can run this command:
```
panda_core_data_commands.py -o directory-name
```
It will automatically generate the basic directory structure, plus a basic main file.

# How to Collaborate

If you want to help with the development of this library, I would say that I love you but my
fiancee would get jealous, so I will just say thank you :D

## By throwing money at the screen
- **Tidelif**: We are on Tidelift! So you can get some technical support from them, and they help us. It's a win win! If you are interested, [click here](https://tidelift.com/subscription/pkg/pypi-panda-core-data?utm_source=pypi-panda-core-data&utm_medium=referral&utm_campaign=readme) (we get some help if you use this referal link too~)
- **Patreon**: If you want to help us every month, you can help us by checking our patreon page [here](https://www.patreon.com/project_chrysalis)
- **Ko-fi**: Do you like Coffee, I love coffee, if you want to send a tip for a coffee, you can do that [here](https://ko-fi.com/project_chrysalis)

## By providing help with coding

First, make sure you have **at least Python 3.7**, git and pip up and running:
```
python -V
pip -V
git --version
```
download this repository with the following command using git:
```
git clone https://github.com/Cerberus1746/PandaCoreData.git
```

And then cd into the directory with:
```
cd PandaCoreData
```

Now, if you want to just run the tests to test your changes, you can run:
```
pip install tox
tox
```
If you want to generate docs, you can install all dependencies with:
```
pip install panda-core-data[docs]
```

And then generate the docs with the command:
```
python setup.py build_sphinx
```
The docs will be located by default inside the directory `docs/build/html`

Security contact information
=============================
To report a security vulnerability, please use the
[Tidelift security contact](https://tidelift.com/security). Tidelift
will coordinate the fix and disclosure.
