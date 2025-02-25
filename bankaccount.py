class BankAccount:
    def __init__(self, account_holder,balance=0.0):
        self.__account_holder=account_holder
        self.__balance=balance
    def __str__(self):
        return f"{self.__account_holder} : {self.__balance}"

    def deposit_(self, amount):
        if amount>0:
            self.__balance+= amount
            print(f"Deposited amount {amount}. New Bal: {self.__balance}")
        else:
            print("amount must be more."
                  "Don't be broke")

    def withdraw(self, amount):
        if amount <=self.__balance:
            self.__balance-=amount
            print(f"Withdrawing amount{amount}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Balance: {self.__balance}")


name =input("Enter your name:")
account= BankAccount(name)

#console program
while True:
    print("\n Welcome to Safari Bank!")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice=int(input("Enter Your Choice:"))
    if choice== 1:
        amount=int(input("Enter the amount to Deposit"))
        account.withdraw(amount)
    elif choice==2:
        amount= int(input("Enter amount to Withdraw:"))
        account.withdraw(amount)
    elif choice ==3:
        account.check_balance()
    elif choice==4:
        print("Thank You for Using Safari Bank ")
        break
    else:
        print("Invalid Choice. Don't be DUMB")