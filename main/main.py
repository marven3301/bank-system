import time
from functions import fake_client, money_operations
from functions.id_check import check_client_id
from functions.all_clients import show_all_clients
import json

# trying to open file in json, if not possible adding the list with clients
try:
    with open("../data/clients_data.json", "r") as file:
        clients = json.load(file)
except FileNotFoundError:
    clients = []

wrong = "Wrong value"

print("Welcome to Daniel's banking system")
while True:
    print("1. Add/Delete a client\n"
          "2. Deposit money\n"
          "3. Withdraw money\n"
          "4. Transfer money from one client to another\n"
          "5. Check client by ID\n"
          "6. All clients\n"
          "To exit press 0")
    val = input(">>> ")
    if val == "1":
        choose = input("1. Add new client\n"
                           "2. Delete the client\n"
                           "Press q to exit\n"
                            ">>>")
        # new client adding
        if choose == "1": # client adding
            print("Adding new client, please stand by...")
            time.sleep(0.7)
            fake_client.new_client(clients)
            print("New client was added")
            time.sleep(0.8)
        elif choose == "2": # client deleting
            fake_client.delete_client(clients)
        elif choose.upper() == "Q": #exiting
            continue
        else:
            print(wrong)

    elif val == "2": # depositing money
        money_operations.deposit_money(clients)
        time.sleep(0.8)
    elif val == "3": # withdrawing money
        money_operations.withdraw_money(clients)
        time.sleep(0.8)
    elif val == "4": # transfer money from one client to another
        money_operations.money_transfer(clients)
    elif val == "5": #client ID checking
        check_client_id(clients)
    elif val == "6": # all clients table
        print(">>>All clients menu<<<\n"
              "1. All clients table(from new to old)\n"
              "2. All clients table(From most money to least)\n"
              "3. All clients table(From least money to most)")
        try:
            val1 = input(">>>")
            if val1 == "1":
                show_all_clients(clients, sort_order=0)
                time.sleep(1)
            elif val1 == "2":
                show_all_clients(clients, sort_order=1)
                time.sleep(1)
            elif val1 == "3":
                show_all_clients(clients, sort_order=2)
                time.sleep(1)
            else:
                print(wrong)

        except ValueError:
            print("Wrong number")
    elif val == "0": # exiting the programm
        print("See you later...")
        time.sleep(0.8)
        break
    else:
        print(wrong)
