class Bankaccount:
    def __init__(self,account_holder,balance=0.0):
        self._account_holder=account_holder
        self.__balance=balance
    def __str__(self):
        return f"{self._account_holder} : {self.__balance}"

    def deposit_(self, amount):
        if amount>0:
            self.__balance+= amount
            print(f"Deposited amount {amount}.")
        else:
            print("amount must be more."
                  "Don't be broke")
    def display_balance(self):
        print(f"New Balance is {self.__balance}")

class SavingAccount(Bankaccount):
    def __int__(self, account_holder, balance, add_intrest):
        super().__init__(account_holder,balance)
    @staticmethod
    def rate(balance):
        intrest=balance*2.5
        balance=intrest+balance
        print(balance)


name =input("Enter your name:")
account= Bankaccount(name)

#console program
while True:
    print("\n Welcome to Chad's Bank!")
    print("1. Deposit Money")
    print("2. Saving")
    print("4. Exit")

    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        amount = int(input("Enter the amount to Deposit"))
        account.deposit_(amount)
    if choice ==2 :
        amount=int(input("Enter the amount to Save"))
        amount.SavingAccount(Bankaccount)
    elif choice == 4:
        print("Thank You for Using Safari Bank ")
        break
    else:
        print("Invalid Choice."
              " Don't be DUMB")
