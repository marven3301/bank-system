import time
from fake_client import new_client
import money_operations
from id_check import check_client_id
from all_clients import show_all_clients


clients = []


while True:
    print("Welcome to Daniel's banking system\n"
          "1. Add new client\n"
          "2. Deposit money\n"
          "3. Withdraw money\n"
          "4. Check client by ID\n"
          "5. All clients\n"
          "To exit press 0")
    val = input(">>> ")
    if val == "1":
        print("Adding new client, please stand by...")
        time.sleep(0.7)
        new_client(clients)
        print("New client was added")
        time.sleep(0.8)
    elif val == "2":
        money_operations.deposit_money(clients)
        time.sleep(0.8)
    elif val == "3":
        money_operations.withdraw_money(clients)
        time.sleep(0.8)
    elif val == "4":
        check_client_id(clients)
    elif val == "5":
        print(">>>All clients menu<<<\n"
              "1. All clients table(from new to old)\n"
              "2. All clients table(From most money to least)\n"
              "3. All clients table(From least money to most)")
        try:
            val1 = input(">>>")
            if val1 == "1":
                show_all_clients(clients, sort_order=0)
            elif val1 == "2":
                show_all_clients(clients, sort_order=1)
            elif val1 == "3":
                show_all_clients(clients, sort_order=2)
            else:
                print("Wrong value")

        except ValueError:
            print("Wrong number")
    elif val == "0":
        print("See you later...")
        time.sleep(0.8)
        break
    else:
        print("Wrong value")
