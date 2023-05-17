grocery_list = []

def main():
    while True:
        try:
            user = input().upper().strip()
            grocery_list.append(user)
        except EOFError:
            break
    a, b = grocery(grocery_list)
    for i in range(len(a)):
        print(f"{a[i]} {b[i]}")

def grocery(text):
    number_list = []
    items_list = []
    text = sorted(text)
    for i in text:
        if i not in items_list:
            items_list.append(i)
            number_list.append(text.count(i))
    return number_list, items_list

if __name__ == "__main__":
    main()