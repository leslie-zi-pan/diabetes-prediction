import pytest


@pytest.fixture(scope='module')
def test_fixture():
    return {
        "0": 'two',
        "1": 'one'
    }
