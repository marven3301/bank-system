# 💰 Bank System (Python)

A simple console application simulating a basic banking system. Built with Python, this project allows you to create clients, manage their balances, transfer funds, and search for client accounts — all through a console interface.

---

## 🖥️ Running the Project in PyCharm

### ✅ Requirements

- Python 3.10 or newer
- [PyCharm](https://www.jetbrains.com/pycharm/) (Community or Professional edition)

### 📦 Optional Dependency

- `Faker` library for generating fake client data (only used in some parts)

To install Faker:

```bash
pip install faker
```

Or via PyCharm:
- Go to `File > Settings > Project > Python Interpreter`
- Click `+`, then search and install `faker`

---

## 🚀 How to Open and Run in PyCharm

1. **Clone the repository:**

   ```bash
   git clone https://github.com/marven3301/bank-system
   ```

   Or download the ZIP and extract it.

2. **Open in PyCharm:**
   - Launch PyCharm
   - Click **"Open"**
   - Select the project folder `bank-system`

3. **Configure the interpreter (if needed):**
   - Go to `File > Settings > Project > Python Interpreter`
   - Choose an existing interpreter or create a new virtual environment

4. **Run the application:**
   - Open `main.py`
   - Right-click anywhere in the file and choose **"Run 'main'"**
   - The console will launch with the main menu

---

## 🧠 Features

- Create new bank clients
- Deposit and withdraw funds
- Transfer money between accounts
- View account balances
- Search clients by ID
- (Coming soon) Save/load data and view transaction history

---

## 📁 Project Structure

```
bank-system/
├── main.py               # Main menu and program entry point
├── create_client.py      # Client creation logic
├── money_operations.py   # Deposit, withdrawal, and transfer functions
├── id_check.py           # ID validation and client lookup
├── search.py             # Sort/search features
├── requirements.txt      # Optional: list of Python packages
└── README.md             # Project documentation
```

---

## 🛠 Technologies Used

- Python 3.10+
- Faker (for testing data)

---

## ✨ To-Do / Planned Features

- [ ] JSON-based saving/loading of client data (done)
- [ ] Transaction history per client
- [ ] Export client data to CSV
- [ ] Unit tests with `unittest` or `pytest`
- [ ] Refactor using classes (OOP)
- [ ] Improved terminal UI (with `colorama`)

---

## 👨‍💻 Author

**[@marven3301](https://github.com/marven3301)**  
Feel free to fork, open issues, or submit pull requests!

---
