import emoji

def main():
    user_input = input("Input: ")
    output = convert_to_emoji(user_input)
    print(emoji.emojize(output))

def convert_to_emoji(text):
    if "," not in text:
        if ":" in text and " " not in text:
            return f"{text}"
main()