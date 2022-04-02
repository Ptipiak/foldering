from collections import UserDict
import logging

logger = logging.getLogger(__name__)


class Configuration(UserDict):
    def __getattr__(self, attr):
        return self.__getitem__(attr)

    def __getitem__(self, key):
        if isinstance(key, str):
            return super().__getitem__(key)
        if isinstance(key, tuple):
            return self.__reach_get(list(key)[::-1], self.data)

    def __setitem__(self, key, value):
        if isinstance(key, str):
            return super().__setitem__(key, value)
        if isinstance(key, tuple):
            return self.__reach_set(list(key)[::-1], value, self.data)

    def __reach_get(self, items, data={}):
        item = items.pop()
        if len(items) <= 0:
            return data[item]
        data = data[item]
        return self.__reach_get(items, data)

    def __reach_set(self, items, value, data={}):
        item = items.pop()
        data.setdefault(item, {})
        if len(items) <= 0:
            data[item] = {**data[item], **value}
            return data
        data = {**data[item], **self.__reach_set(items, value, data[item])}
        return data
