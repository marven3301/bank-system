import json
from faker import Faker
from random import randint

faker = Faker()
#new fake client adding function
def new_client(clients):
    # client dictionary
    client = {
        "id": randint(1000, 9999),
        "name": faker.first_name(),
        "surname": faker.last_name(),
        "address": faker.address(),
        "phone": faker.phone_number(),
        "balance": 0.0,
        "history": []
    }
    # save client in json
    clients.append(client)
    with open("clients_data.json", "w") as file:
        json.dump(clients, file, indent=4)

    # new client information
    print("New client created:\n"
          f"ID: {client['id']}\n"
          f"Name: {client['name']} {client['surname']}\n"
          f"Address: {client['address']}\n"
          f"Phone: {client['phone']}\n"
          f"Balance: ${client['balance']:.2f}\n")

    return client


def delete_client(clients):
    # ID inputting
    try:
        client_id = int(input("Please add ID of a client: "))
    except ValueError:
        print("No client with such ID")
        return
    # Search the client by ID
    for client in clients:
        if client["id"] == client_id:
            clients.remove(client) # removing the client from list
            with open("clients_data.json", "w") as file:
                json.dump(clients, file, indent=4) # removing the client from json
                print(f"Client with ID{client['id']} was deleted")
                return

    print("Client not found")
