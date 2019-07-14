import pytest
import one


@pytest.mark.parametrize("string", [
    "test",
    "hello",
    "foo"
])
def test_non_unique(string):
    assert one.isUnique(string) == False
    assert one.isUniqueNoDataStructure(string) == False


@pytest.mark.parametrize("string", [
    "world",
    "bar",
    "coding"
])
def test_unique(string):
    assert one.isUnique(string) == True
    assert one.isUniqueNoDataStructure(string) == True
