user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
if user_input == "42":
    print("yes")
elif user_input == "forty two":
    print("yes")
elif user_input == "forty-two":
    print("yes")
else:
    print("no")