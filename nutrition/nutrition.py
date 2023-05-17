# program for calculate calory

# dictionaries of fructs
fructs = {
        "apple": "130",
        "banana": "110",
        "grapes": "70",
        "orange": "80",
        "strawberries": "50",
        "pineapple": "50",
        "mango": "60",
        "blueberries": "80",
        "watermelon": "40",
        "cantaloupe": "50",
        "peaches": "60",
        "plums": "70",
        "raspberries": "60",
        "kiwifruit": "90",
        "pears": "100",
        "blackberries": "60",
        "cherries": "50",
        "grapefruit": "60",
        "avocado": "50",
        "pomegranate": "80",
        "pear": "100",
        "sweet cherries": "100"
    }

# users input
def main():
    user_input = calculate(input("input: ").lower())
    if calculate(user_input):
        user_input = fructs[user_input]
        print(f"{user_input}")
    else:
        pass

# calculate fructs calory
def calculate(c):
    while c in fructs:
        return c
    else:
        return False

main()

