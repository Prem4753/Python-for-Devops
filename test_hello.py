from hello import more_hello
from hello import more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


def test_more_googbye():
    assert "bye" == more_goodbye()
