from twttr import shorten
def main():
    test_shorten_no_vowels()

def test_shorten_no_vowels():
    assert shorten("xyz") == "xyz"
    assert shorten("twttr") == "twttr"
    assert shorten("Python") == "Pythn"
    assert shorten("Eureka") == "rk"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("") == ""
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("123") == "123"

if __name__ == "__main__":
    main()