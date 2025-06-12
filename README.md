# 💰 Bank System (Python)

A simple console application simulating a basic bank system. It allows you to create clients, manage balances, make transfers, and search for users.

---

## 📌 Features

- 👤 Create new clients
- 💵 Deposit and withdraw funds
- 🔁 Transfer money between clients
- 📊 View client balance
- 🔍 Search clients by ID
- 📚 (Planned) Data saving and transaction history

---

## 🖼️ Example Usage

```
=== Bank System ===
1. Create a new client
2. Deposit money
3. Withdraw money
4. Transfer money
5. Check balance
6. Find client
7. Exit
Choose an option: _
```

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/marven3301/bank-system
cd bank-system
```

2. (Optional) Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

---

## 📂 Project Structure

```
bank-system/
├── main.py               # Main menu interface
├── create_client.py      # Client creation logic
├── money_operations.py   # Deposit, withdraw, transfer functions
├── id_check.py           # Client ID validation and lookup
├── search.py             # Sorting clients
├── README.md
└── requirements.txt
```

---

## 🧩 Planned Improvements

- [ ] Save/load client data from JSON
- [ ] Add transaction history per client
- [ ] Export client data to CSV
- [ ] Unit testing with unittest or pytest
- [ ] Refactor using OOP (classes)
- [ ] Improved console UI (e.g., using `colorama`)

---

## 🛠️ Built With

- Python 3.10+
- [Faker](https://faker.readthedocs.io/en/master/) — for generating mock data

---

## 🤝 Contact

Developer: [@marven3301](https://github.com/marven3301)  
Feel free to open issues, give feedback, or submit pull requests!

---