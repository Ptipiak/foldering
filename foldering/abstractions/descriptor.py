import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class Validator(ABC):
    def __init__(self, name=""):
        logger.debug(f"name: {name}")
        self.name = name

    def __set_name__(self, owner, name):
        self.private_name = name

    def __get__(self, obj):
        logger.debug(f"getting {self.name}")
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass
