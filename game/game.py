import random

def main():
    while True:
        try:
            inputed_level = int(input("Level: "))
            final_level = game(inputed_level)
            if inputed_level <= 0:
                print('Please enter a positive integer.')
            else:
                break
        except ValueError:
            print("Invalid")

    while True:
        try:
            inputed_guess = int(input("Guess: "))
            if inputed_guess < final_level:
                print("Too small!")
            elif inputed_guess <= 0:
                print("invalid")

            elif inputed_guess > final_level:
                print("Too large!")

            elif inputed_guess == inputed_guess:
                print("Just right!")
                break
        except ValueError:
            print("invalid")

def game(text):
    while True:
        text = int(text)
        guess = random.randrange(1, text)
        return guess


if __name__ == "__main__":
    main()