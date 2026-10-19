from app.calc import add


def test_add_negative():
    assert add(-1, 1) == 0
