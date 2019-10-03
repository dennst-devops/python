# Dennis S

class User:		
    def __init__(self, username, email_address): 
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.name, self.account_balance)
    def make_transfer(self, self2, amount):
        self.account_balance -= amount
        self2.account_balance += amount
        print("The balance for", self.name, "is", str(self.account_balance), ".")
        print("The balance for", self2.name, "is", str(self.account_balance), ".")

guido = User("Guido van Rossum", "guido@python.com")
guido.display_user_balance()
monty = User("Monty Python", "monty@python.com")
dave = User("Dave Lister", "dave@reddwarf.com")
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawal(50)
guido.display_user_balance()
monty.make_deposit(5000)
monty.make_deposit(4000)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
monty.display_user_balance()
dave.make_deposit(100)
dave.make_withdrawal(100)
dave.make_withdrawal(100)
dave.make_withdrawal(100)
dave.display_user_balance()
guido.make_transfer(dave, 550)
guido.display_user_balance()
dave.display_user_balance()
