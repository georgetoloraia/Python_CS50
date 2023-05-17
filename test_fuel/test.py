from fuel import convert, gauge

def main():
    user = input("input: ")
    test1 = test(user)
    print(test1)

def test(s):
    output = gauge(s)
    return output


if __name__ == "__main__":
    main()