from utils import arrs
import pytest


@pytest.fixture
def coll():         # имя фикстуры любое
    return [1, 2, 3, 4]


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get([], 6, "test") == "test"


def test_slice(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3, 4]
    assert arrs.my_slice(coll, None, -1) == [1, 2, 3]
    assert arrs.my_slice([], 3, 4) == []
    assert arrs.my_slice(coll, -4, 0) == []
