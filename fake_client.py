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
        "balance": 0.0
    }
    clients.append(client)
    # new client information
    print("New client created:\n"
          f"ID: {client['id']}\n"
          f"Name: {client['name']} {client['surname']}\n"
          f"Address: {client['address']}\n"
          f"Phone: {client['phone']}\n"
          f"Balance: ${client['balance']:.2f}\n")

    return client
