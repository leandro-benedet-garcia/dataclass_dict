Change Logs
============

0.0.6
######
Added
^^^^^^
- `sphinx_autodoc_typehints` is now a dependency fr the docs

Changed
^^^^^^^^
- All functions and methods now have type annotations and the documentation
  uses them to determine the type

0.0.5
######
Changed
^^^^^^^^
- Everytime a :class:`~panda_core_data.data_type.DataType` is instanced, it
  will be added to the attatched :class:`~panda_core_data.DataCore`. The
  behaviour was that the instance would be added only by calling
  :meth:`~panda_core_data.data_core_bases.data_model.DataModel.instance_model`
  and :meth:`~panda_core_data.data_core_bases.data_template.DataTemplate.instance_template`.
  Also tests were changed to make sure it happens.
- All exceptions now inherit
  :class:`~panda_core_data.custom_exceptions.PCDException`.
- :meth:`~object.__init__` methods are not overwritten anymore.

0.0.4
######
Added
^^^^^^
- Support for tox

Changed
^^^^^^^^
- Fixed the installer to behave better, which could derp while reading some
  files.

0.0.3
######

Changed
^^^^^^^^
- Improved compatibility with Python.Net

Fixed
^^^^^^
- Fixed a bug with the `_get_core()` method

0.0.2
######

Added
^^^^^^
- Support for Json was added
- Now, it's possible to save :class:`~panda_core_data.model.Model` or
  :class:`~panda_core_data.model.Template` to the raw with the
  :meth:`~panda_core_data.data_type.DataType.save_to_file` method
- :meth:`~panda_core_data.data_core_bases.data_model.DataModel.instance_model`
  and
  :meth:`~panda_core_data.data_core_bases.data_template.DataTemplate.instance_template`
  and `older_contents` were added.
- `panda_core_data_commands` has a new option `-re` which you can choose
  between `json` or `yaml`
- :class:`~panda_core_data.custom_exceptions.PCDInvalidRaw` and
  :class:`~panda_core_data.custom_exceptions.PCDDuplicatedModuleName`
  exceptions was created
- Package `Storage` was created

Changed
^^^^^^^^
- :func:`~panda_core_data.storages.auto_convert_to_pathlib` do not need the
  `is_file` parameter anymore
- :class:`panda_core_data.DataCore` has a new parameter `excluded_extensions`
- Both exceptions `PCDFolderNotFound` and `PCDFileNotFound` was merged into
  :class:`~panda_core_data.custom_exceptions.PCDInvalidPath`

0.0.1
######

Added
^^^^^^
- Package released
- Basic yaml reading which their contents is loaded to a python `dataclass`
