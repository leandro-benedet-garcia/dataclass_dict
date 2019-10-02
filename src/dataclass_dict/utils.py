# type: ignore[attr-defined]
'''
:created: 2019-07-29
:author: Leandro (Cerberus1746) Benedet Garcia'''
from dataclasses import _get_field
from typing import Optional, Any, Type


def add_field(dataclass_inst: object, field_name: str, field_type: Type[Any],
              field_value: Optional[Any] = None):
    '''Create a new dataclass field

    :param dataclass_inst: The input dataclass
    :param field_name: The name of the field
    :param field_type: The field type
    :param field_value: The value of the field'''
    setattr(dataclass_inst, field_name, field_value)
    dataclass_inst.__dataclass_fields__[field_name] = _get_field(dataclass_inst, field_name,
                                                                 field_type)
    dataclass_inst.__annotations__[field_name] = field_type


def check_field(dataclass_inst: object, field_name: str) -> bool:
    '''Return true if the field exist inside the input dataclass

    :param dataclass_inst: The dataclass to check
    :param field_name: The name of the field to check'''
    return field_name in dataclass_inst.__dataclass_fields__


def delete_field(dataclass_inst: object, field_name: str, default: Optional[Any] = None) -> Any:
    '''Remove the field from the dataclass

    :param dataclass_inst: The datclass field
    :param field_name: The field name to delete
    :param default: the value to be returned if the field doesn't exist
    :raises KeyError: If default is `None` and the field doesn't exist'''
    dataclass_inst.__dataclass_fields__.pop(field_name, None)
    dataclass_inst.__annotations__.pop(field_name, None)

    if hasattr(dataclass_inst, field_name):
        cur_value = getattr(dataclass_inst, field_name)
        delattr(dataclass_inst, field_name)
        return cur_value

    if default is not None:
        return default
    raise KeyError(field_name)


__all__ = ("add_field", "check_field", "delete_field",)
