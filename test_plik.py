import plik


def test_add():
    assert plik.add(3, 4) == 7
    assert plik.add(3.5, 4) == 7
    assert plik.add(3.9, 4) == 7
    assert plik.add(3.9, 4.1) == 8


def test_to_sentence():
    assert plik.to_sentence('apple') == 'Apple.'
    assert plik.to_sentence('Apple trees') == 'Apple trees.'
    assert plik.to_sentence('Apple trees.') == 'Apple trees.'
