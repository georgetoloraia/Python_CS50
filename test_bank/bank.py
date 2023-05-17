
def main():
    user = value(input("Greeting: "))
    print(user)


def value(greeting):
    greeting = greeting.strip()
    if greeting.startswith("hello") or greeting.startswith("Hello"):
        greeting = "$0"
        return greeting
    if greeting[0] == "h" and greeting != "hello" or greeting[0] == "H" and greeting != "Hello":
        greeting = "$20"
        return greeting
    else:
        greeting = "$100"
        return greeting

if __name__ == "__main__":
    main()