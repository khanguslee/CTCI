import pytest
import one_one


@pytest.mark.parametrize("string", [
    "test",
    "hello",
    "foo"
])
def test_non_unique(string):
    assert one_one.isUnique(string) == False
    assert one_one.isUniqueNoDataStructure(string) == False


@pytest.mark.parametrize("string", [
    "world",
    "bar",
    "coding"
])
def test_unique(string):
    assert one_one.isUnique(string) == True
    assert one_one.isUniqueNoDataStructure(string) == True
