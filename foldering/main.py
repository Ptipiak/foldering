import foldering.utils as utils
import logging
from pathlib import Path
from foldering.reader import Reader
from foldering.implementations.validators import JsonValidator

logger = logging.getLogger(__name__)
files = ["schemas", "parameters", "a"]


def main():
    reader = Reader()
    schema_path = Path("./conf/schemas")
    iterator_schemas = reader.open(schema_path)
    param_path = Path("./conf/parameters")
    iterator_params = reader.open(param_path)
    settings = {}
    validator = JsonValidator()
    for schema, _ in map(reader.read, iterator_schemas):
        validator.schema = schema
    for param, path in map(reader.read, iterator_params):
        validator.validate(param)
        ancestor = ".".join(utils.ancestors(path, param_path))
        settings = utils.aggregate(settings, ancestor, param)
    logger.info(settings)
