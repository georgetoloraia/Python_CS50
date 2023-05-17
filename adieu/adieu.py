import inflect


def main():
    user_input_list = []
    while True:
        try:
            user_input = input("")
            user_input_in_list = user_input_list.append(user_input)
        except EOFError:
            break
    p = inflect.engine()
    output = p.join((user_input_list))
    print(output)
    print(f"Adieu, adieu, to {output}")

main()
