class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount


# create 3 users
user1 = User("User One", 100)
user2 = User("User Two", 200)
user3 = User("User Three", 50)

# user1: 3 deposits و 1 withdrawal
user1.make_deposit(50)
user1.make_deposit(20)
user1.make_deposit(30)
user1.make_withdrawal(40)
user1.display_user_balance()

# user2: 2 deposits و 2 withdrawals
user2.make_deposit(100)
user2.make_deposit(50)
user2.make_withdrawal(80)
user2.make_withdrawal(30)
user2.display_user_balance()

# user3: 1 deposit و 3 withdrawals
user3.make_deposit(200)
user3.make_withdrawal(50)
user3.make_withdrawal(30)
user3.make_withdrawal(20)
user3.display_user_balance()

# BONUS
user1.transfer_money(user3, 50)

user1.display_user_balance()
user3.display_user_balance()