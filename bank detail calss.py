class bankaccount:
    def id(self):
        self.a = int(input("account_number :"))
        self.c = str(input("customer_name :"))
        self.d = str(input("date_of_opening :"))
        self.b = float(input("initial_balance :"))

    def deposit(self, amount):
        self.b += amount
        return self.b

    def withdraw(self, amount):
        if amount > self.b:
            print("Insufficient balance!")
            return self.b
        self.b -= amount
        return self.b

    def check_balance(self):
        return self.b


account = bankaccount()
account.id()
print("Initial balance:", account.check_balance())
account.deposit(500.0)
print("Balance after deposit:", account.check_balance())
account.withdraw(200.0)
print("Balance after withdrawal:", account.check_balance())