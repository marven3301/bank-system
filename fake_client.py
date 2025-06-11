from faker import Faker
from random import randint

faker = Faker()

def new_client(clients):
    client = {
        "id": randint(1000, 9999),
        "name": faker.first_name(),
        "surname": faker.last_name(),
        "address": faker.address(),
        "phone": faker.phone_number(),
        "balance": 0.0
    }
    clients.append(client)

    print("New client created:")
    print(f"ID: {client['id']}")
    print(f"Name: {client['name']} {client['surname']}")
    print(f"Address: {client['address']}")
    print(f"Phone: {client['phone']}")
    print(f"Balance: ${client['balance']:.2f}\n")

    return client
