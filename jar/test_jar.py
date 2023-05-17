from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
    try:
        jar.deposit(3)  # Exceeds capacity
    except ValueError as e:
        assert str(e) == "Exceeded jar capacity"


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    try:
        jar.withdraw(10)  # Not enough cookies
    except ValueError as e:
        assert str(e) == "Not enough cookies in the jar"



if __name__ == "__main__":
    main()
