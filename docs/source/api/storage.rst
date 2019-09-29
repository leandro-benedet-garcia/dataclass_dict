Storages
===========

Storages are classes based on TinyDB that handles file management, raw parsing
and other things like that, if you'd like to create support for more file
types, all you have to do is to inherit the
:class:`~panda_core_data.storages.base_db.BaseDB` and follow the instructions
in the API of that class.

Directory Utils
-------------------

.. automodule:: panda_core_data.storages
    :members:
    :private-members:
    :special-members:
    :exclude-members: __weakref__

YamlDB
-------------------

.. autoclass:: panda_core_data.storages.yaml_db.YamlDB
    :members:
    :private-members:
    :special-members:
    :exclude-members: __weakref__

JsonDB
-------------------

.. autoclass:: panda_core_data.storages.json_db.JsonDB
    :members:
    :private-members:
    :special-members:
    :exclude-members: __weakref__

BaseDB
-------------------

.. autoclass:: panda_core_data.storages.base_db.BaseDB
    :members:
    :private-members:
    :special-members:
    :exclude-members: __weakref__
