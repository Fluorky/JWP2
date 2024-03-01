class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance  # Private attribute

    def deposit_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} PLN.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw_money(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} PLN.")
        else:
            print("Invalid withdrawal amount.")

    def show_account_balance(self):
        print(f"Account balance: {self.__balance} PLN.")


# Using the class
account = BankAccount('123456789', 1000)
account.deposit_money(500)
account.withdraw_money(200)
account.show_account_balance()  # Prints the current account balance
