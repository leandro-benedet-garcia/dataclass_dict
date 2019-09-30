# type: ignore[attr-defined]
'''

:created: 2019-09-28
:author: Leandro (Cerberus1746) Benedet Garcia'''
from collections.abc import MutableMapping, KeysView
from dataclasses import _FIELDS, _POST_INIT_NAME, _process_class, field, InitVar, dataclass
from inspect import signature
from typing import Optional, Any, Dict, Union, Type, List, Callable

from .utils import delete_field, add_field, check_field


class DataclassDict(MutableMapping, KeysView):
    def __new__(cls: Type["DataclassDict"], *_: List[Any], **kwargs: Dict[str, Any]
                ) -> "DataclassDict":
        cls.__init_subclass__(**kwargs)
        return object.__new__(cls)

    def __init_subclass__(cls: Type["DataclassDict"], **kwargs: Dict[str, Any]):
        if not hasattr(cls, "dataclass_args"):
            cls.dataclass_args = {}
            for param_name, param in signature(dataclass).parameters.items():
                # both cls and _cls are to avoid bugs with nightly version of python.
                if param_name not in ["_cls", "cls"]:
                    dt_param_name = "dataclass_" + param_name

                    if dt_param_name in kwargs:
                        cls.dataclass_args[param_name] = kwargs.pop(dt_param_name, param.default)
                    else:
                        cls.dataclass_args[param_name] = kwargs.pop(param_name, param.default)

            for cur_key, cur_value in kwargs.items():
                if not hasattr(cls, cur_key):
                    setattr(cls, cur_key, cur_value)
                    if not hasattr(cls, "__annotations__"):
                        cls.__annotations__ = {}
                    cls.__annotations__[cur_key] = type(cur_value)

            #pylint: disable=self-cls-assignment
            cls = _process_class(cls, **cls.dataclass_args)

    def __getitem__(self, key: Union[int, str, slice]) -> Union[List[Any], Any]:
        if isinstance(key, int):
            key_name = self._mapping[key]
            return self.__getitem__(key_name)

        if isinstance(key, str) and key in self:
            return getattr(self, key)

        if isinstance(key, slice):
            return_list = []
            if key.start is None:
                generated_range = range(key.stop)
            else:
                generated_range = range(key.start, key.stop if key.stop is not None else 0,
                                        key.step if key.step is not None else 1)

            for curr_key in generated_range:
                return_list.append(self.__getitem__(curr_key))

            return return_list

        raise KeyError(key)

    def __setitem__(self, key: Union[str, int], value: Any):
        if isinstance(key, int):
            key_name = self._mapping[key]
            self.__setitem__(key_name, value)
        elif isinstance(key, str) and key in self:
            setattr(self, key, value)
        else:
            add_field(self, key, type(value), value)

    __contains__ = check_field

    pop = __delitem__ = delete_field

    @property
    def _mapping(self):
        return list(self.__annotations__)

__all__ = ("DataclassDict", "delete_field", "add_field", "check_field")
