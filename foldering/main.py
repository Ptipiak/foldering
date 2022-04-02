import foldering.utils as utils
import logging
from pathlib import Path
from foldering.reader import Reader
from foldering.implementations.validators import JsonValidator
from foldering.implementations.configuration import Configuration

logger = logging.getLogger(__name__)
files = ["schemas", "parameters", "a"]


def main():
    reader = Reader()
    schema_path = Path("./conf/schemas")
    iterator_schemas = reader.open(schema_path)
    param_path = Path("./conf/parameters")
    iterator_params = reader.open(param_path)
    settings = Configuration()
    validator = JsonValidator()
    for schema, _ in map(reader.read, iterator_schemas):
        validator.schema = schema
    for param, path in map(reader.read, iterator_params):
        validator.validate(param)
        ancestors = utils.subset(files, path.parts)
        logger.debug(f"ancestors: {ancestors}")
        settings[tuple(ancestors)] = param
    logger.info(settings)
