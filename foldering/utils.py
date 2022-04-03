import logging
from typing import List

logger = logging.getLogger(__name__)


def ancestors(reference: List, target: List) -> list:
    return subset(reference.parts, target.parts)


def subset(reference: List, target: List) -> list:
    return [part for part in target if part in reference]


def aggregate(reference, target, value):
    if not isinstance(value, (dict, list)):
        raise ValueError(
            f"the input value can only be of \
                type {type(list)} and {type(dict)}"
        )
    default = type(value)()
    reference.setdefault(target, default)
    if not reference[target]:
        reference[target] = value
        return reference
    if isinstance(reference[target], dict):
        reference[target] = [reference[target]]
    if isinstance(default, dict):
        reference[target] = reference[target] + [value]
    if isinstance(default, list):
        reference[target] = reference[target] + value
    return reference
