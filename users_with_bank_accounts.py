from bank_account import BankAccount
class User:		
    def __init__(self, name,int_rate, balance):
        self.name = name
        self.account =  BankAccount(int_rate = int_rate , balance = balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
       
        return self 
    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self 
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

def main():
    guido = User(name="guido",int_rate= 0.2 , balance=100)
    guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

if __name__ == "__main__":
    main()