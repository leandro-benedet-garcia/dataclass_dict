import http
import json
from threading import Thread
from typing import Any, Dict, List, Union
from urllib.request import urlopen


JsonObj = Dict[str, Any]
JsonType = Union[List[Union[JsonObj, Any]], JsonObj]


class ThreadedGetData(Thread):
    output_data: List["ThreadedGetData"] = []
    open_threads: List["ThreadedGetData"] = []
    registered_threads: List["ThreadedGetData"] = []

    data: http.client.HTTPResponse
    started: bool

    def __init__(self, url: str, **kwargs):
        self.url = url

        self.started = False
        self.already_run = False
        ThreadedGetData.registered_threads.append(self)
        super().__init__(**kwargs)

    @classmethod
    def start_loop(cls):
        for cur_thread in cls.registered_threads:
            if not cur_thread.already_run:
                cur_thread.start()

        while any(cls.open_threads):
            pass

        cls.registered_threads = []

    def run(self):
        self.started = True
        self.already_run = True
        ThreadedGetData.open_threads.append(self)

        self.data = urlopen(self.url)

        self.started = False
        ThreadedGetData.open_threads.remove(self)

    def from_json(self, **kwargs):
        return json.load(self.data, **kwargs)


def load_url(*args: str) -> List[ThreadedGetData]:
    all_threads = []
    for cur_url in args:
        all_threads.append(ThreadedGetData(cur_url))

    ThreadedGetData.start_loop()
    return all_threads


def load_json_from_url(*args: str, **kwargs: Any) -> Union[JsonType, List[JsonType]]:
    output_list = []
    for current_thread in load_url(*args):
        output_list.append(current_thread.from_json(**kwargs))
    return output_list[0] if len(output_list) == 1 else output_list


__all__ = ("load_url", "load_json_from_url")
