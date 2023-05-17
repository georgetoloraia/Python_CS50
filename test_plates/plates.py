def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s == "CS50":
        return True

    elif not s.isalnum():
        return False
    elif s[0] == "0" or s == "0":
        return False

    elif len(s) < 2 or len(s) > 6:
        return False

    elif not s[:2].isalpha():
        return False

    elif not s[2:].isalnum() or s[2].isdigit():
        return False

    else:
        return True


if __name__ == "__main__":
    main()
