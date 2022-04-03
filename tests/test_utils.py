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
    result = {
        "alpha": [
            {"target1": "test"},
            {"target2": "test"},
            {"target3": "test"},
        ]
    }
    assert reference == result


def test_subset():
    list1 = ["a", "a" "c", "d"]
    list2 = ["a", "e"]
    result = ["a"]
    assert subset(list1, list2) == result


def test_ancestors():
    path1 = Path("./conf/schema/a/a.txt")
    path2 = Path("./conf/schema/b/b.txt")
    result = ["conf", "schema"]
    assert ancestors(path2, path1) == result

    path1 = Path("./conf/schema/a/a.txt")
    path2 = Path("./conf/b.txt")
    result = ["conf"]
    assert ancestors(path2, path1) == result
