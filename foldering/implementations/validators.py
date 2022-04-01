import logging
import foldering.abstractions.validator as abstract
from jsonschema import validate, Validator

logger = logging.getLogger(__name__)


class JsonValidator(abstract.Validator):
    def __init__(self, schema=None):
        self._schema = schema

    def validate(self, value):
        validate(value, self.schema)

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, schema):
        Validator.check_schema(schema)
        self._schema = schema
