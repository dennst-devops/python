# Dennis S
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
    def display_account_info(self):
        #print("The balance for", self.name, "is", str(self.balance), ".")
        print("Balance: $" + str(self.balance))
        return self
    def yield_interest(self):  #A = P(1 + rt)
        if self.balance > 0:
            # need to round this to 2 decimal places
            self.balance = round(self.balance * (1 + (self.int_rate / 100) * 1), 2)
        return self

acct1 = BankAccount(5, 1000)
acct2 = BankAccount(4, 2500)
acct3 = BankAccount(4, 25500)
acct4 = BankAccount(4, 25050)
acct5 = BankAccount(4, 25090)
acct1.deposit(500).deposit(500).deposit(500).withdraw(1).yield_interest().display_account_info()
acct2.deposit(5).deposit(15).withdraw(5).withdraw(5).withdraw(5).withdraw(2505).yield_interest().display_account_info()
acct3.display_account_info()
acct4.display_account_info()
acct5.display_account_info()