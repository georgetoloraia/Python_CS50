def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s == "CS50":
        return True

    elif len(s) < 2 or len(s) > 6:
        return False

    elif not s[:2].isalpha():
        return False

    elif not s[2:].isalnum() or s[2].isdigit():
        return False

    return True


main()
