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
        """Prepare the thread to be executed

        :param url: The url to be loaded."""
        self.url = url

        self.started = False
        self.already_run = False
        type(self).registered_threads.append(self)
        super().__init__(**kwargs)

    @classmethod
    def start_loop(cls):
        'Load all urls and register them on their data attributes'
        for cur_thread in cls.registered_threads:
            if not cur_thread.already_run:
                cur_thread.start()

        while any(cls.open_threads):
            pass

        cls.registered_threads = []

    def run(self):
        cur_type = type(self)

        self.started = True
        self.already_run = True

        cur_type.open_threads.append(self)

        self.data = urlopen(self.url)

        self.started = False
        cur_type.open_threads.remove(self)

    def from_json(self, **kwargs):
        'Transform json data into a :class:`~dataclass_dict.DataclassDict`'
        return json.load(self.data, **kwargs)


def load_url(*urls: str) -> List[ThreadedGetData]:
    '''Load one or more urls executing them from threads

    :param urls: one or more urls to be loaded'''
    all_threads = []
    for cur_url in urls:
        all_threads.append(ThreadedGetData(cur_url))

    ThreadedGetData.start_loop()
    return all_threads


def load_json_from_url(*urls: str, **kwargs: Any) -> Union[JsonType, List[JsonType]]:
    '''Load one or more json from the urls

    :param urls: one or more urls to be loaded'''
    output_list = []
    for current_thread in load_url(*urls):
        output_list.append(current_thread.from_json(**kwargs))
    return output_list[0] if len(output_list) == 1 else output_list


__all__ = ("load_url", "load_json_from_url")
