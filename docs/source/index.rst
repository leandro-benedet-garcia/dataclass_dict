Welcome to dataclass_dict's documentation!
===========================================

All this package does is create a dataclass so you can straight up use it as if it was a dictionary.
Here's a basic example:

.. code:: python

    from dataclass_dict import create_dataclass_dict

    # Generate a instance
    instance = create_dataclass_dict({"name": "Test", "value": 10})

    # prints "Test"
    print(instance.name)

    # also prints "Test"
    print(instance["name"])

    # prints "Test" and deletes the field "name"
    print(instance.pop("name")

Also, you can automatically generate a dataclass with a json like this:

.. code:: python

    from dataclass_dict import dataclass_from_json

    json_code = """{
        "name": "Test",
        "value": 10
    }"""

    instance = dataclass_from_json(json_code)


If you'd like, you can load a json file straight from a url like this:

.. code:: python

    from dataclass_dict import dataclass_from_url

    dataclass_from_url("json_url")

Plus, if you pass multiple parameters this way:

.. code:: python

    from dataclass_dict import dataclass_from_url

    dataclass_from_url("json_url_1", "json_url_2")

They will be downloaded at the same time using threads.

Keep in mind that all parameters from the function :func:`json.dumps` works with the
:func:`dataclass_from_json` and :func:`dataclass_from_url` so you can write special parsers.

API Reference
==============
Dataclass Dict
---------------
.. automodule:: dataclass_dict
    :members:
    :private-members:
    :special-members:
    :show-inheritance:
    :exclude-members: __weakref__

Threading
----------
.. automodule:: dataclass_dict.threaded_request
    :members:
    :private-members:
    :special-members:
    :show-inheritance:
    :exclude-members: __weakref__

Utils
------
.. automodule:: dataclass_dict.utils
    :members:
    :private-members:
    :special-members:
    :show-inheritance:
    :exclude-members: __weakref__


Changelogs
===========
0.0.5
------
Added
^^^^^^
- If the creation dictionary have a string that is not a valid variable name, it will raise an 
  :class:`~AssertionError`
- :func:`~dataclass_dict.utils.item_zip` was added

0.0.4
------
Fixed
^^^^^^
- Now, the package should be able to be installed normally. The package name was being identified as
  src

0.0.3
------
Added
^^^^^^
- Any attribute, including parent ones, that starts with underscore will be ignored.
- :func:`~dataclass_dict.utils.item_zip` was added. It iterates between more than one
  :class:`~dict`.

Fixed
^^^^^^
- Now, indeed, anything started with underscore will be ignored.

0.0.2
------
Changed
^^^^^^
- Any attribute starting with a `_` will not be added to the dataclass, but will be available
  normally
Fixed
^^^^^^
- :meth:`~dataclass_dict.DataclassDict.__new__` and
  :meth:`~dataclass_dict.DataclassDict.__init_subclass__` now calls their
  parents with :func:`super`
- If a class inherited :class:`~dataclass_dict.DataclassDict` and it didn't have a field with
  annotations, it would raise an error. That's fixed now.

0.0.1.1
------
Added
^^^^^^
- Added Tidelif information in the readme
Fixed
^^^^^^
- Fixed informations in the `setup.py` file such as descriptions and repository link.

0.0.1
------
Added
^^^^^^
- Package released
