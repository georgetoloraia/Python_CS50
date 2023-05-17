import sys
import random
from pyfiglet import Figlet

def print_usage_and_exit():
    print("Usage: figlet.py [-f/--font font_name]")
    sys.exit(1)

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            print_usage_and_exit()
        else:
            print("Invalid command-line arguments")
            print_usage_and_exit()

    font_name = None
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("Invalid command-line arguments")
            print_usage_and_exit()
        font_name = sys.argv[2]

    figlet = Figlet(font=font_name)
    text = input("Enter the text: ")

    if not font_name:
        fonts = figlet.getFonts()
        font_name = random.choice(fonts)
        figlet.setFont(font=font_name)

    output = figlet.renderText(text)
    print(output)

if __name__ == "__main__":
    main()
