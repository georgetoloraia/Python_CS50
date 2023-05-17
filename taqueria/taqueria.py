grocery_list = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    amount = 0
    while True:
        try:
            user = input("Items: ").lower()
            amount += check(user)
            print(f"${amount:.2f}", end="\n")
        except EOFError: # KeyErrorS
            break

def check(user):
    if user in grocery_list:
        return grocery_list[user]
    else:
        return 0

main()