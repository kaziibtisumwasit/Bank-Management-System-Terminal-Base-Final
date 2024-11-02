import random
import datetime
from abstruct_base_user import User


class Account(User):
    def __init__(self, name, email, address, account_type, bank):
        super().__init__(name, email, address)
        self.account_type = account_type
        self._balance = 0
        self.account_history = []
        self._account_number = self.generate_account_number()
        self.take_loan_count = 0
        self.bank = bank

    def generate_account_number(self):
        return random.randint(101100, 1019999)

    def get_account_number(self):
        return self._account_number

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            now = datetime.datetime.now()
            done = f"Deposited: Done ✅\nDate & Time: {
                now}\nDeposited Amount: {amount}"
            self.account_history.append(done)
            print(f"{done}\n\n")
            self.bank.add_bank_balance(amount)
            self.check_balance()
        else:
            print("Failed! You entered an invalid amount! ❌\n")

    def withdraw(self, amount):

        if amount > 0 and amount <= self._balance and not self.bank.bankrupt:
            self._balance -= amount
            now = datetime.datetime.now()
            done = f"Withdrawn: Done ✅\nDate & Time: {
                now}\nWithdrawn Amount: {amount}"
            self.account_history.append(done)
            print(f"{done}\n\n")
            self.bank.decrease_bank_balance(amount)
            self.check_balance()
        elif self.bank.bankrupt():
            print("This Bank is currently Bankrupt!\n")
        else:
            print("Failed! Withdrawal amount exceeded ❌\n")

    def check_balance(self):
        print(f"Your current balance is: {self._balance}\n")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.account_history:
            print(transaction)

    def take_loan(self, amount):
        if self.take_loan_count < 2 and self.bank.loan_option and self.bank.get_bank_balance() > amount and not self.bank.bankrupt:
            self.take_loan_count += 1
            self._balance += amount
            # self.bank.decrease_bank_balance(amount)
            now = datetime.datetime.now()
            done = f"Loan Approved ✅\nDate & Time: {
                now}\nLoan Amount: {amount}"
            self.account_history.append(done)
            self.bank.add_loan_balance(amount)
            self.check_balance()
            print(done+"\n\n")
        elif self.bank.get_bank_balance() > amount:
            print("This bank not avail of the amount\n")
        elif self.bank.bankrupt:
            print("This Bank is currently Bankrupt!\n")
        else:
            print("Loan limit exceeded or Bank loan option is off\n")

    def transfer_money(self, user_name, amount):
        if amount > 0 and amount <= self._balance and not self.bank.bankrupt:
            account = self.bank.find_account(user_name)
            if account:
                self._balance -= amount
                account._balance += amount
                now = datetime.datetime.now()
                print(f"Balance transfer successful! ✅\nSender: {
                      self.name} | Receiver: {user_name} | Transfer Amount: {amount}\n")
                done = f"Balance Transfer Successful! To {
                    user_name}\nDate & Time: {now}\nTransfer Amount: {amount}"
                self.account_history.append(done)
                self.check_balance()
            elif self.bank.bankrupt:
                print("This Bank is currently Bankrupt!\n")
            else:
                print("Account not found! ❌\n")
        else:
            print("Failed! Transfer amount exceeded ❌\n")
