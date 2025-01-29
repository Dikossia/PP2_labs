class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Депозит: {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Ошибка: недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снятие: {amount}. Новый баланс: {self.balance}")


account = BankAccount("Иван", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
