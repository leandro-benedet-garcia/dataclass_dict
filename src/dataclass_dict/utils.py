# type: ignore[attr-defined]
'''
:created: 2019-07-29
:author: Leandro (Cerberus1746) Benedet Garcia'''
from dataclasses import _get_field
from typing import Optional, Any, Type


def add_field(dataclass_inst: object, field_name: str, field_type: Type[Any],
              field_value: Optional[Any] = None):
    setattr(dataclass_inst, field_name, field_value)
    dataclass_inst.__dataclass_fields__[field_name] = _get_field(dataclass_inst, field_name,
                                                                 field_type)
    dataclass_inst.__annotations__[field_name] = field_type

def check_field(dataclass_inst: object, key: str) -> bool:
    return key in dataclass_inst.__dataclass_fields__

def delete_field(dataclass_inst: object, key: str) -> Any:
    dataclass_inst.__dataclass_fields__.pop(key, None)
    dataclass_inst.__annotations__.pop(key, None)

    if hasattr(dataclass_inst, key):
        cur_value = getattr(dataclass_inst, key)
        delattr(dataclass_inst, key)
        return cur_value
    raise AttributeError(key)

__all__ = ("add_field", "check_field", "delete_field")
