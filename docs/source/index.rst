Welcome to dataclass_dict's documentation!
===========================================

All this package does is create a dataclass so you can straight up use it as if it was a dictionary.
Here's a basic example:

.. code:: python

    from dataclass_dict import DataclassDict

    # Generate a instance
    instance = DataclassDict(name="Test", value=10)

    # prints "Test"
    print(instance.name)

    # also prints "Test"
    print(instance["name"])

    # prints "Test" and deletes the field "name"
    print(instance.pop("name")

Changelogs
==========
0.0.1
######

Added
^^^^^^
- Package released
