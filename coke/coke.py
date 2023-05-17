amount = [25, 10, 5]
amount_due = 0
insert_coin = 50

while amount_due < 50:
    if amount_due == 0:
        print("Amount Due: 50")
    user_input = int(input("Insert Coin: "))
    if user_input in amount:
        amount_due += user_input
        if amount_due == 50:
            print(f"Change Owed: 0")
            break
        elif amount_due < 50:
            insert = insert_coin - amount_due
            print(f"Amount Due: {insert}")
        elif amount_due > 50:
            amount_due = amount_due - insert_coin
            print(f"Change Owed: {amount_due}")
            break