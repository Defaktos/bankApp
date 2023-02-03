class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to the account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from the account.")

    def transfer(self, to_account, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.withdraw(amount)
            to_account.deposit(amount)
            print(f"{amount} transferred to {to_account.name}.")

    def show_balance(self):
        print(f"Name: {self.name}\nBalance: {self.balance}")

if __name__ == '__main__':
    blokhinDima = BankAccount("Blokhin Dima")
    blokhinaAlina = BankAccount("Blokhina Alina")
    blokhinDima.deposit(1000)
    blokhinDima.transfer(blokhinaAlina, 500)
    blokhinDima.show_balance()
    blokhinaAlina.show_balance()
