# type: ignore[attr-defined]
'''
:created: 2019-07-29
:author: Leandro (Cerberus1746) Benedet Garcia'''
from dataclasses import _FIELDS, _get_field
from typing import Optional, Any, Type


def add_field(dataclass_instance: object, field_name: str, field_type: Type[Any],
              field_value: Optional[Any] = None):
    '''Create a new dataclass field

    :param dataclass_instance: The input dataclass
    :param field_name: The name of the field
    :param field_type: The field type
    :param field_value: The value of the field'''
    setattr(dataclass_instance, field_name, field_value)
    getattr(dataclass_instance, _FIELDS)[field_name] = _get_field(dataclass_instance, field_name,
                                                                  field_type)
    dataclass_instance.__annotations__[field_name] = field_type


def check_field(dataclass_instance: object, field_name: str) -> bool:
    '''Return true if the field exist inside the input dataclass

    :param dataclass_instance: The dataclass to check
    :param field_name: The name of the field to check'''
    return field_name in getattr(dataclass_instance, _FIELDS)


def delete_field(dataclass_instance: object, field_name: str, default: Optional[Any] = None) -> Any:
    '''Remove the field from the dataclass

    :param dataclass_instance: The dataclass to delete the field from
    :param field_name: The field name to delete
    :param default: the value to be returned if the field doesn't exist
    :raises KeyError: If default is `None` and the field doesn't exist'''
    getattr(dataclass_instance, _FIELDS).pop(field_name, None)
    dataclass_instance.__annotations__.pop(field_name, None)

    if hasattr(dataclass_instance, field_name):
        cur_value = getattr(dataclass_instance, field_name)
        delattr(dataclass_instance, field_name)
        return cur_value

    if default is not None:
        return default
    raise KeyError(field_name)

def item_zip(*dicts_input):
    '''Function to iterate across multiple dictionaries

    An example in how to use this function is:

    .. code:: python

        first_dict = {"first": 1}
        second_dict = {"second": 2}

        for first_key, first_var, second_key, second_var in item_zip(first_dict , second_dict):
            #prints first, 1
            print(first_key, first_var)
            #prints second, 2
            print(second_key, second_var)'''
    zipped = zip(*[cur_dict.items() for cur_dict in dicts_input])
    return map(lambda x: (x[0][0], x[0][1], x[1][0], x[1][1]), zipped)

__all__ = ("add_field", "check_field", "delete_field", "item_zip",)
