# type: ignore[attr-defined]
'''
:created: 18-07-2019
:author: Leandro (Cerberus1746) Benedet Garcia
'''
from dataclasses import field, InitVar
from typing import MutableMapping, Dict, Any, Optional, List

import pytest

from dataclass_dict import DataclassDict, delete_field, add_field


TESTING_VALUES: Dict[str, Any] = {
    "name": "testing",
    "cur_value": 10
}

TEST_VALUES: List[Any] = list(TESTING_VALUES.values())
SECOND_VALUE: str = "Another Test"
THIRD_VALUE: int = 5
FOURTH_VALUE: int = 10

NEW_TEST_VALUES: List[Any] = TEST_VALUES + [SECOND_VALUE, THIRD_VALUE]

def test_mappings_with_post_init():
    to_set_value: int = 9
    sum_result: int = TESTING_VALUES["cur_value"] + TESTING_VALUES["cur_value"]

    class BaseDictWithPost(DataclassDict, dataclass_order=False):
        name: str
        cur_value: int
        auto_value: Optional[int] = field(init=False)
        to_set: InitVar[int]

        def __post_init__(self, to_set):
            self.auto_value = self.cur_value + self.cur_value
            self.to_set = to_set

    instanced: BaseDictWithPost = BaseDictWithPost(**TESTING_VALUES, to_set=to_set_value)

    assert instanced.pop("auto_value") == sum_result
    assert instanced.pop("to_set") == to_set_value

    mapping_test(instanced)

    instanced: BaseDictWithPost = BaseDictWithPost(*TEST_VALUES, to_set_value)
    assert instanced.pop("auto_value") == sum_result
    assert instanced.pop("to_set") == to_set_value

    instanced: BaseDictWithPost = BaseDictWithPost(*TEST_VALUES, to_set=to_set_value)
    assert instanced.pop("auto_value") == sum_result
    assert instanced.pop("to_set") == to_set_value


def test_mappings_with_inherit():
    class BaseDict(DataclassDict):
        name: str
        cur_value: int

    mapping_test(BaseDict(**TESTING_VALUES))

def test_mappings_without_inherit():
    mapping_test(DataclassDict(**TESTING_VALUES))

def mapping_test(instanced):
    assert isinstance(instanced, MutableMapping)

    test_keys: List[str] = list(TESTING_VALUES.keys())

    for key_name in instanced:
        assert key_name in test_keys

    for value in instanced.values():
        assert value in TEST_VALUES

    for key_name, value in instanced.items():
        assert key_name in test_keys
        assert value in TEST_VALUES

    assert instanced[:1] == TEST_VALUES[:1]
    assert instanced[0:1] == TEST_VALUES[0:1]
    assert instanced[0:2] == TEST_VALUES[0:2]

    instanced["name"] = SECOND_VALUE
    instanced[1] = THIRD_VALUE
    instanced.fourth = FOURTH_VALUE

    for key_name in instanced:
        assert key_name in test_keys + ["fourth"]

    for value in instanced.values():
        assert value in NEW_TEST_VALUES

    for key_name, value in instanced.items():
        assert key_name in test_keys + ["fourth"]
        assert value in NEW_TEST_VALUES + [FOURTH_VALUE]

    #pylint: disable=no-member
    assert instanced.name == SECOND_VALUE
    assert instanced[0] == SECOND_VALUE

    assert instanced.pop("name") == SECOND_VALUE
    instanced["new_field"] = "test"

    assert "new_field" in instanced
    assert instanced["new_field"] == "test"
    assert len(instanced) == 3

    instanced.clear()

    #pylint: disable=len-as-condition
    assert len(instanced) == 0

    add_field(instanced, "first", int, 10)
    assert instanced["first"] == 10


def test_mapping_exceptions():
    instanced: DataclassDict = DataclassDict(*TESTING_VALUES)

    with pytest.raises(IndexError):
        #pylint: disable=pointless-statement
        instanced[9]

    with pytest.raises(KeyError):
        #pylint: disable=pointless-statement
        instanced["invalid"]

    with pytest.raises(AttributeError):
        delete_field(instanced, "invalid")
