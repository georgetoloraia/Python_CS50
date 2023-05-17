def main():
    user_input = shorten(input("Input: "))
    print(f"Output: {user_input}")


def shorten(word):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    text = ""
    for c in word:
        if c not in vowel:
            text += c
    return text


if __name__ == "__main__":
    main()