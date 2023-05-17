from bank import value

def main():
    test()

def test():
    assert value("What's happening?") == 100
    assert value("Hello, Newman") == 0
    assert value("Hello") == 0
    assert value("How you doing?") == 20
    assert value("hallo") == 20
    assert value("123") == 100
    assert value("What's up?") == 100
    # assert value(" ") == "$0"
    assert value(" hello") == 0


if __name__ == "__main__":
    main()