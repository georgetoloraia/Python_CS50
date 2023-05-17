
def main():
    user = value(input("Greeting: ").lower().strip())
    print(user)


def value(b):
    if b.startswith("hello"):
        b = "$0"
        return b
    elif b[0] == "h":
        b = "$20"
        return b
    else:
        b = "$100"
        return b

if __name__ == "__main__":
    main()