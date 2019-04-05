import pytest

from core.stack import FifthStack


@pytest.fixture
def stack():
    yield FifthStack()
