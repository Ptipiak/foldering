from foldering.utils import aggregate, subset, ancestors
from pathlib import Path


def test_aggregate():
    reference = {}
    target1 = {"target1": "test"}
    target2 = {"target2": "test"}
    target3 = {"target3": "test"}
    reference = aggregate(reference, "alpha", target1)
    reference = aggregate(reference, "alpha", target2)
    reference = aggregate(reference, "alpha", target3)
    alpha = {
        "alpha": [
            {"target1": "test"},
            {"target2": "test"},
            {"target3": "test"},
        ]
    }
    assert reference == alpha
