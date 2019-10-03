# Dennis S

class User:		
    def __init__(self, username, email_address): 
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self
    def make_transfer(self, self2, amount):
        self.account_balance -= amount
        self2.account_balance += amount
        print("The balance for", self.name, "is", str(self.account_balance), ".")
        print("The balance for", self2.name, "is", str(self.account_balance), ".")
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
dave = User("Dave Lister", "dave@reddwarf.com")
guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()
monty.make_deposit(5000).make_deposit(4000).make_withdrawal(50).make_withdrawal(50).display_user_balance()
dave.make_deposit(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()
guido.make_transfer(dave, 550)
guido.display_user_balance()
dave.display_user_balance()
