
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user = input("Input: ")
text = ""

for c in user:
    if c not in vowel:
        text += c

print(f"Output: {text}")
