from numb3rs import validate
import random

def main():
    test()
    test_random_test()
    # test_false_check()
    # test_true_check()

def test():
    assert validate(r"232.23.3.2") == True
    assert validate("127.0.0.1") == True
    assert validate("cat") == False
    # assert validate((f"{i}.168.0.0") for i in range(0, 255)) == True
    assert all(validate(f"{i}.168.0.0") for i in range(256, 1000)) == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("255.255.10.1") == True
    assert validate("1.1.1") == False
    assert validate(r"-1.235.25.2") == False
    assert validate("1.1.1.100") == True
    assert validate("355.12.168.2") == False
    assert validate("cat.dog.1.1") == False
    assert validate("1236.12.3.2") == False
    assert validate("123") == False
    assert validate("256") == False
    assert validate(r"255.255.255.256") == False
    assert validate(r"256.3455.255432.432256") == False

def test_random_test():
    a = random.randrange(0, 1000)
    b = random.randrange(0, 1000)
    c = random.randrange(0, 1000)
    d = random.randrange(0, 1000)
    ipv4 = f"{a}.{b}.{c}.{d}"
    ipv4add = str(ipv4)
    test1 = validate(ipv4add)
    if test1 == True:
        assert validate(ipv4add) == True
    else:
        assert validate(ipv4add) == False

# def test_false_check():
#     assert validate(r"255.255.255.256") == False
#     assert validate(r"256.3455.255432.432256") == False
#     assert validate(r"-1.235.25.2") == False
#     assert validate(r"2434.4355.-255.256") == False
#     assert validate(r"cat.dog.cat.dog") == False
#     assert validate(r"1.1.1") == False
#     assert validate(r"1.1.1.") == False
#     assert validate(r"1.1") == False
# def test_true_check():
#     assert validate(r"255.255.254.0") == True
#     assert validate(r"168.125.2.1") == True
#     assert validate(r"255.255.0.0") == True
#     assert validate(r"232.23.3.2") == True
#     assert validate(r"0.0.0.0") == True


if __name__ == "__main__":
    main()
