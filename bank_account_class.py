class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"AccountHolder Name: {self.name} \nBalance: {self.balance}"
    def deposit(self, amount):
        # amount = int(input("Enter amount to deposit "))
        self.balance += amount
        print(f"You have deposited {amount} into your account!")
        print(f"Your new balance is {self.balance}")
    def withdrawal(self, amount):
        # amount = float(input("Enter amount to withdraw "))
        if amount < self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("You do not have enough balance!")
        print(f"Your new balance is {self.balance}")
tulasi_account = BankAccount("Tulasi", 40)
tulasi_account.deposit(500)
tulasi_account.withdrawal(300)
print(tulasi_account.balance)