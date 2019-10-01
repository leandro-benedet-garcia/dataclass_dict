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

Keep in mind that all parameters from the function :func:`json.dumps` works with the
:func:`dataclass_from_json` so you can write special parsers.

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
0.0.1
------
Added
^^^^^^
- Package released
