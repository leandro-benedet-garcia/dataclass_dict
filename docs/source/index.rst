Welcome to PandaCoreData's documentation!
=========================================

So, if you already played games like Factorio, Rimworld or Dwarf Fortress and
tried to mod them, you will find that it’s absurdly easy to mod those games for
simple things like changing the balancing, adding items, changing descriptions
and etc. Because the data files of the games are simple raws and not binaries.
This library pretty much makes the task of using raws as simple as possible.
Raws in our case is plain text files like xml, json, yaml and etc that
is commonly used to hold data, for now the library supports `yaml` and `json`.

The library might have modding in mind, however it pretty much be used for any
sort of software or game engine that uses python.

Internally the library use
`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ to handle
the data and `TinyDB <https://tinydb.readthedocs.io/en/latest/>`_ to load them
from raws.

.. toctree::
    :maxdepth: 4
    :glob:
    :caption: Tutorial

    tutorial/getting_started
    tutorial/unity

.. toctree::
    :maxdepth: 4
    :glob:
    :caption: API

    api/*
    changelogs


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
