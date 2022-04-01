import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class Reader:
    def __init__(self):
        super().__init__()

    def __new__(cls, *args, **kargs):
        return super().__new__(cls, *args, **kargs)

    def _jsonParser(func):
        def inner(self, *args, **kargs):
            with func(self, *args, **kargs) as fileDescriptor:
                content = json.load(fileDescriptor)
            return content

        return inner

    @_jsonParser
    def openFile(self, path, mode="r"):
        return path.open(mode)

    @staticmethod
    def open(path: Path):
        return Reader.openFile(Reader(), path), path

    def read(self, path, depth=-1):
        iterator = path.iterdir()
        # If the depth is reached, close the iterator before any actions
        if depth == 0:
            iterator.close()
        for path in iterator:
            depth -= 1
            if path.is_dir():
                yield from self.read(path, depth)
            if path.is_file():
                yield path
