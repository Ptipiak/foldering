from pathlib import Path


class Path(Path):
    def __new__(cls, *args, **kwargs):
        super().__new__(*args, **kwargs)

    def __init__(self, path):
        super().__init__(path)

    def compare(self):
        print(self.parts)
