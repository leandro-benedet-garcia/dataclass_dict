dataclass_dict [![Build Status](https://travis-ci.org/Cerberus1746/dataclass_dict.svg?branch=master)](https://travis-ci.org/Cerberus1746/dataclass_dict) [![Documentation Status](https://readthedocs.org/projects/dataclass-dict/badge/?version=latest)](https://dataclass-dict.readthedocs.io/en/latest/?badge=latest) [![Maintainability](https://api.codeclimate.com/v1/badges/6373c7712a3a29353842/maintainability)](https://codeclimate.com/github/Cerberus1746/dataclass_dict/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/6373c7712a3a29353842/test_coverage)](https://codeclimate.com/github/Cerberus1746/dataclass_dict/test_coverage)
===============
With this package you are able to create a dataclass that works exactly like a dictionary.

# Install
This package **only works with python 3.6 or above** because it uses **dataclasses**. In python 3.6
it will uses the dataclass package from pypi.

To use this package you may run the following command:
```
pip install dataclass-dict
```

# How to Collaborate
If you want to help with the development of this library, I would say that I love you but my
fiancee would get jealous, so I will just say thank you :D

## By throwing money at the screen
- **Tidelif**: We are on Tidelift! So you can get some technical support from them, and they help us.
  It's a win win! If you are interested,
  [click here](https://tidelift.com/subscription/pkg/pypi-dataclass-dict?utm_source=pypi-dataclass-dict&utm_medium=referral&utm_campaign=readme)
  (we get some help if you use this referal link too~)
- **Patreon**: If you want to help us every month, you can help us by checking our patreon page
  [here](https://www.patreon.com/project_chrysalis)
- **Ko-fi**: Do you like Coffee, I love coffee, if you want to send a tip for a coffee, you can do
  that [here](https://ko-fi.com/project_chrysalis)

## By providing help with coding
First, make sure you have **at least Python 3.6**, git and pip up and running:
```
python -V
pip -V
git --version
```
download this repository with the following command using git:
```
git clone https://github.com/Cerberus1746/dataclass_dict.git
```

And then cd into the directory with:
```
cd dataclass_dict
```

Now, if you want to just run the tests to test your changes, you can run:
```
pip install tox
tox
```
If you want to generate docs, you can install all dependencies with:
```
pip install .[docs]
```

And then generate the docs with the command:
```
python setup.py build_sphinx
```
The docs will be located by default inside the directory `docs/build/html`

# Security contact information
To report a security vulnerability, please use the
[Tidelift security contact](https://tidelift.com/security). Tidelift will coordinate the fix and
disclosure.
