class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Balance is too low!")
        else:
            self.balance -= amount
            return self.balance
        
    def summary(self):
        print(f"The acount holder is {self.owner} with a current balance of: ${self.balance}")


charles = BankAccount('Charles', 44.58)
# print(charles.deposit(63))
# print(charles.withdraw(22))
print(charles.withdraw(63))
charles.summary()
