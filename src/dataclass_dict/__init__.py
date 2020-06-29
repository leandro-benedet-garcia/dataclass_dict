# type: ignore[attr-defined]
'''
:created: 2019-09-28
:author: Leandro (Cerberus1746) Benedet Garcia'''
from collections.abc import MutableMapping, KeysView
from dataclasses import _FIELDS, _POST_INIT_NAME, _process_class, field, InitVar, dataclass
from inspect import signature
from json import loads
from typing import Optional, Any, Dict, Union, Type, List, Callable, Mapping

from .threaded_request import load_json_from_url
from .utils import *


class DataclassDict(MutableMapping, KeysView):
    'The dataclass dict. It automatically transforms any class that inherits it into a dataclass.'

    def __new__(cls, *_, **kwargs: Dict[str, Any]) -> "DataclassDict":
        if not hasattr(cls, "dataclass_args"):
            raise TypeError("You can't instance the class directly, you must inherit it first or "
                            "use the function 'create_dataclass_dict', 'dataclass_from_dict' or"
                            "'dataclass_from_json'")

        if not hasattr(cls, "__annotations__"):
            cls.__annotations__ = {}
        for cur_key, cur_value in kwargs.items():
            assert valid_variable(cur_key), "the variable has a invalid name"
            cur_type = type(cur_value)

            if cur_key not in  cls.__annotations__:
                cls.__annotations__[cur_key] = cur_type

            if cur_type in (dict, list, set):
                created_field = field(default_factory=cur_type)
                setattr(cls, cur_key, created_field)

        # Even if the class has an annotated attribute, It should not appear in the dataclass at all
        # if it starts with `_`
        # Hence why we are saving a copy of the annotations and filtering out any variable starting
        # with underline and then putting the annotation back
        original_annotations = cls.__annotations__
        cls.__annotations__ = dict(filter(lambda x: x[0][0] != "_", original_annotations.items()))

        # pylint: disable=self-cls-assignment,no-member
        cls = _process_class(cls, **cls.dataclass_args)

        cls.__annotations__ = original_annotations

        for cur_key, cur_value in kwargs.items():
            setattr(cls, cur_key, cur_value)

        return super().__new__(cls)

    def __init_subclass__(cls, **kwargs: Dict[str, Any]):
        cls.dataclass_args = {}
        for param_name, param in signature(dataclass).parameters.items():
            # both cls and _cls are to avoid bugs with nightly version of python.
            if param_name not in ["_cls", "cls"]:
                dt_param_name = "dataclass_" + param_name

                if dt_param_name in kwargs:
                    cls.dataclass_args[param_name] = kwargs.pop(dt_param_name, param.default)
                else:
                    cls.dataclass_args[param_name] = kwargs.pop(param_name, param.default)
        super().__init_subclass__(**kwargs)

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
                generated_range = range(key.start,
                                        key.stop if key.stop is not None else 0,
                                        key.step if key.step is not None else 1)

            for curr_key in generated_range:
                return_list.append(self.__getitem__(curr_key))

            return return_list

        raise KeyError(key)

    def __setitem__(self, key: Union[str, int], value: Any):
        if isinstance(key, int):
            key_name = self._mapping[key]
            self.__setitem__(key_name, value)
        else:
            setattr(self, key, value)

    def __setattr__(self, key: Union[str, int], value: Any):
        if key[0] != "_" and key not in self:
            field_type = type(value)
            # pylint: disable=no-member
            if key not in getattr(self, _FIELDS):
                created_field = field()
                created_field.name = key

                if field_type in (dict, str, set):
                    created_field.default_factory = field_type

                created_field.type = field_type

                # pylint: disable=no-member
                getattr(self, _FIELDS)[key] = created_field

            if key not in self.__annotations__:
                self.__annotations__[key] = field_type

        super().__setattr__(key, value)

    __contains__ = check_field
    __delitem__ = pop = delete_field

    @property
    def _mapping(self):
        # pylint: disable=no-member
        return list(getattr(self, _FIELDS))

    @staticmethod
    def create_new(*args, **kwargs):
        return create_dataclass_dict(*args, **kwargs)

    @staticmethod
    def from_json(json_input: str):
        return dataclass_from_json(json_input)

    def update_from_json(self, json_input: str):
        '''
        Exactly like :meth:`~dict.update` but it loads data from a json string.

        :param json_input: The input json string.'''
        created_data = dataclass_from_json(json_input)
        created_data.update(self)
        return created_data


def create_dataclass_dict(input_dict: Mapping = None, **kwargs):
    if not input_dict:
        input_dict = dict(**kwargs)

    tmp_class = type("GeneratedDataclassDict", (DataclassDict,), input_dict)
    return tmp_class(**input_dict)


def dataclass_from_json(*args, **kwargs):
    dumped_json = loads(*args, **kwargs)
    return create_dataclass_dict(dumped_json)


def dataclass_from_url(*args, **kwargs):
    returned_json = load_json_from_url(*args, **kwargs)

    if isinstance(returned_json, list):
        returned_dict_data = []
        for opened_json in returned_json:
            returned_dict_data.append(create_dataclass_dict(opened_json))
        return returned_dict_data

    return create_dataclass_dict(returned_json)


__all__ = ("DataclassDict", "add_field", "check_field", "delete_field", "create_dataclass_dict",
           "dataclass_from_json", "load_json_from_url")
