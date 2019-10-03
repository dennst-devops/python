# Dennis S

class User:
    def __init__(self, username, email_address): 
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print("-"*15)
        myself = self.name
        self.account.display_account_info(myself)
        print("*"*15)
        return self
    def make_transfer(self, self2, amount):
        print("Making transfer from " + self.name + " to " + self2.name)
        self.account.withdraw(amount)
        self2.account.deposit(amount)
        # print("The balance for", self.name, "is", str(self.account.balance))
        # print("The balance for", self2.name, "is", str(self.account.balance))
        myself = self.name
        myself2 = self2.name
        self.account.display_account_info(myself)
        self2.account.display_account_info(myself2)
        return self

class BankAccount:
    def __init__(self, int_rate, balance): 
        # Do we need an acct number here? 
        self.int_rate = int_rate
        # trying to force 2 decimal places...
        self.balance = round(float(balance), 2)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self, myname):
        print("The balance for " + myname, "is $" + str(self.balance))
        # print("Balance: $" + str(self.balance))
        return self
    def yield_interest(self):  #A = P(1 + rt)
        if self.balance > 0:
            # need to round this to 2 decimal places
            self.balance = round(self.balance * (1 + (self.int_rate / 100) * 1), 2)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
dave = User("Dave Lister", "dave@reddwarf.com")

dave.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(1000)
guido.make_withdrawal(500)
guido.display_user_balance()
dave.display_user_balance()
guido.make_transfer(dave, 1)
guido.display_user_balance()
dave.display_user_balance()
dave.make_withdrawal(101)
dave.make_withdrawal(101)
dave.display_user_balance()