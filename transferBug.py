class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdrawal", amount))

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        self.accounts[account_number] = BankAccount(initial_balance)

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            from_account.withdraw(amount)
        else:
            raise ValueError("Invalid account number")

def main():
    bank = Bank()
    bank.create_account("12345", 1000)
    bank.create_account("67890", 500)

    bank.transfer("12345", "67890", 200)

    print(bank.get_account("12345").get_balance())  # Expected output: 800
    print(bank.get_account("67890").get_balance())  # Expected output: 700

if __name__ == "__main__":
    main()
