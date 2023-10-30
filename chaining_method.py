
class User:		
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount 
       
        return self 
    def make_withdrawal(self, amount):
        self.account_balance-= amount
        return self 
    
    def display_user_balance(self):
        print(self.account_balance)
        return self

def main():
    guido = User("guido")
    guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

if __name__ == "__main__":
    main()