class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        # BONUS: user have multiple accounts
        self.accounts = {}

    def add_account(self, account_name, int_rate=0.02, balance=0):
        # create account with specified name
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, account_name, amount):
        # deposite
        self.accounts[account_name].deposit(amount)
        return self

    def make_withdrawal(self, account_name, amount):
        # withdraw
        self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        # display_account_info
        print(f"User: {self.name} - Account: {account_name}")
        self.accounts[account_name].display_account_info()
        return self
    
user1 = User("Shaimaa", "test@test.com")

# create accounts
user1.add_account("saving", 0.03, 1000)
user1.add_account("checking", 0.01, 500)

#deposit,withdrawal
user1.make_deposit("saving", 200)
user1.make_withdrawal("checking", 100)

# display
user1.display_user_balance("saving")
user1.display_user_balance("checking")