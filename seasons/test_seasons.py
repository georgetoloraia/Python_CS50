from seasons import minutes, minutes_to_words, valid_format

def main():
    test_minutes()
    test_minutes_to_word()
    test_valid_foramt()


def test_minutes():
    assert minutes("1995-01-01") == 14919840
    assert minutes("2023-04-23") == 31680

def test_minutes_to_word():
    assert minutes_to_words(1) == "One minutes"
    assert minutes_to_words(50) == "Fifty minutes"
    assert minutes_to_words(120) == "One hundred twenty minutes"

def test_valid_foramt():
    assert valid_format("2001-06-06") == True
    assert valid_format("2001/06/06") == False

if __name__ == "__main__":
    main()