
bank_balance = 5000

def deposit(amount):
    global bank_balance
    bank_balance += amount
    print("Amount deposited:", amount)

def withdraw(amount):
    global bank_balance

    if amount <= bank_balance:
        bank_balance -= amount
        print("Amount withdrawn:", amount)
    else:
        print("Insufficient balance!")

deposit(1000)
print("Balance after deposit:", bank_balance)

withdraw(2000)
print("Balance after withdrawal:", bank_balance)