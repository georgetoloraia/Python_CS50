def main():
    user_input = camel(input(": "))
    print(user_input)


def camel(c):
    snake_case = ""
    for i in c:
        if i.isupper():
            snake_case += "_" + i.lower()
        else:
            snake_case += i
    return snake_case

main()