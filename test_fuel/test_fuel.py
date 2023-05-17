import pytest
from fuel import convert, gauge

def main():
    test_convert_integer()
    test_ValueError()
    test_ZeroDivisionError()
    test_gauge()
    test_not_printing_persent_in_gauge()

def test_convert_integer():
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("3/4") == 75
def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/1")
def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_gauge():
    assert gauge(1.0) == "E"
    assert gauge(99.0) == "F"

def test_not_printing_persent_in_gauge():
    assert gauge(50) == "50%"


if __name__ == "__main__":
    main()