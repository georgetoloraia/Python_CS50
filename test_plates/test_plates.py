from plates import is_valid

def main():
    test_False()

def test_False():
    assert is_valid("aaaaaaa") == False
    assert is_valid("$1") == False
    assert is_valid("CS05") == False
    assert is_valid("PI#.14") is False
    assert is_valid("CS50") == True
    assert is_valid("123aaa") == False
    assert is_valid("aaa123") == True
    assert is_valid("Aba123") == True
    assert is_valid("123456") == False
    assert is_valid("aaa2bb") == False




if __name__ == "__main__":
    main()
