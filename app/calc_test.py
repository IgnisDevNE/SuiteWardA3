from app.calc import add


def test_add_zero():
    assert add(0, 2) == 2
