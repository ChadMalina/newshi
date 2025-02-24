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
    def display_Balance(self,amount):
        print(f"New Balance is {self.__balance}")

class SavingAccount(Bankaccount):
    def __int__(self, account_holder, balance, add_intrest):
        super().__init__(account_holder,balance)
    def
