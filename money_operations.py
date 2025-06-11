# money deposit function
def deposit_money(clients):
    # id check
    try:
        check = int(input("Input id of a client: "))
    except ValueError:
        print("Invalid ID")
        return

    for client in clients:
        if client["id"] == check:
            try:
                # adding amount of money
                money = float(input("Add amount of money: "))
                client["balance"] += money
                print(f"Successfully added ${money:.2f}. New balance: ${client['balance']:.2f}")
                return
            # Error, if amount is invalid
            except ValueError:
                print("Invalid amount")
                return

# money withdraw function
def withdraw_money(clients):
    # id check
    try:
        check = int(input("Input id of a client: "))
    except ValueError:
        print("Invalid ID")
        return

    for client in clients:
        if client["id"] == check:
            try:
                money = float(input("Withdraw amount of money: "))
                if client["balance"] >= money: # checking if amount of money is greater than taking amount
                    # taking amount of money
                    client["balance"] -= money
                    print(f"Successfully withdrawn ${money:.2f}. New balance: ${client['balance']:.2f}")
                    return
                else:
                    print("Error! Client balance couldn't be below zero")
            except ValueError:
                print("Invalid amount")
                return

