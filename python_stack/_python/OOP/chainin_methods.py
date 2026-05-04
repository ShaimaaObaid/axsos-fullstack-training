class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self   # 

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self   # 

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self   # 

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self   # 


# create 3user
user1 = User("User One", 100)
user2 = User("User Two", 200)
user3 = User("User Three", 50)


#chaining 
user1.make_deposit(50).make_deposit(20).make_deposit(30).make_withdrawal(40).display_user_balance()

user2.make_deposit(100).make_deposit(50).make_withdrawal(80).make_withdrawal(30).display_user_balance()

user3.make_deposit(200).make_withdrawal(50).make_withdrawal(30).make_withdrawal(20).display_user_balance()


# BONUS chaining
user1.transfer_money(user3, 50).display_user_balance()
user3.display_user_balance()