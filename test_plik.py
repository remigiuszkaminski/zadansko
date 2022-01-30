import plik


def test_add():
    assert plik.add(3, 4) == 7
    assert plik.add(3.5, 4) == 7
    assert plik.add(3.9, 4) == 7
    assert plik.add(3.9, 4.1) == 8

