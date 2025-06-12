# clients sorting function
def show_all_clients(clients, sort_order=0):
    # check if there are now clients
    if not clients:
        print("No clients found.")
        return
    #sorting orders
    if sort_order == 1: #from most money to least
        sorted_clients = sorted(clients, key=lambda c: c['balance'], reverse=True)
    elif sort_order == 2: #from least money to most
        sorted_clients = sorted(clients, key=lambda c: c['balance'])
    else:
        sorted_clients = clients
    # table of clients
    print(f"{'ID':<6} {'Name':<15} {'Surname':<15} {'Balance':>10}")
    print("-" * 50)
    for client in sorted_clients:
        print(f"{client['id']:<6} {client['name']:<15} {client['surname']:<15} ${client['balance']:>9.2f}")
