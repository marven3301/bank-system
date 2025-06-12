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
                if client["balance"] >= money: # checking if amount of money is greater than taken amount
                    # taking amount of money
                    client["balance"] -= money
                    print(f"Successfully withdrawn ${money:.2f}. New balance: ${client['balance']:.2f}")
                    return
                else:
                    print("Error! Client balance couldn't be below zero")
            except ValueError:
                print("Invalid amount")
                return

# money transferring function
def money_transfer(clients):
    try:
        # client id inputting
        id1 = int(input("Input id of a client, whose money will be transferred: "))
        id2 = int(input("Input id of a client, who will receive the money: "))
        money = float(input("Add amount of money: "))

        sender = None
        receiver = None
        # check if client exists
        for client in clients:
            if client["id"] == id1:
                sender = client
            elif client["id"] == id2:
                receiver = client
        # check if client do not exist
        if sender is None:
            print("Sender not found")
            return
        if receiver is None:
            print("Receiver not found")
            return
        if sender["id"] == receiver["id"]:
            print("You cant transfer yourself the money")
        # money adding
        if sender["balance"] >= money:
            sender["balance"] -= money
            receiver["balance"] += money
            print(f"Successfully added ${money:.2f} to client{receiver["name"]}{receiver["surname"]}. New balance: ${receiver['balance']:.2f}")
        elif sender["balance"] < money:
            print("Error! Client balance couldn't be below zero")
    except ValueError:
        print("Invalid Input")
        return

