def check_client_id(clients):
    try:
        client_id = int(input("Please add ID of a client: "))
    except ValueError:
        print("No client with such ID")
        return

    for client in clients:
        if client["id"] == client_id:
            print(">>>Client information<<<\n"
                  f"ID: {client['id']}\n"
                  f"Name: {client['name']} {client['surname']}\n"
                  f"Address: {client['address']}\n"
                  f"Phone: {client['phone']}\n"
                  f"Balance: ${client['balance']:.2f}\n"
                  "_________________________________\n")
            return

