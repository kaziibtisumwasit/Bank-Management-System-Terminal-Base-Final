from abstruct_base_user import User
from bank import Bank


class Admin(User):
    def __init__(self, name, email, address, password, bank):
        super().__init__(name, email, address)
        self.password = password
        self.bank = bank

    def delete_user(self, username):
        self.bank.delete_user(username)

    def user_list(self):
        self.bank.user_list()

    def total_available_balance(self):
        print(f"Total Available Balance: {self.bank.get_bank_balance()}")

    def total_loan(self):
        self.bank.total_loan()

    def off_loan(self):
        self.bank.loan_option_off()

    def on_loan_option(self):
        self.bank.loan_option_on()

    def bankrupted_option_on(self):
        self.bank.bankrupt = True

    def bankrupted_option_off(self):
        self.bank.bankrupt = False
