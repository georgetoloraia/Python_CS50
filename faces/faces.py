def main():
    user_input = replace_user_input(input("input: "))
    print(user_input)

def replace_user_input(r):
    r = r.replace(":)", "🙂")
    r = r.replace(":(", "🙁")
    return r

main()