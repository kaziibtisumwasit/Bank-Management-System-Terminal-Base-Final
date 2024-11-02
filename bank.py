class Bank:
    def __init__(self):
        self.user_account_list = []
        self._bank_balance = 0
        self.loan_balance = 0
        self.loan_option = False
        self.bankrupt = False
        self.admin_list = []

    def loan_option_status(self):
        if self.loan_option:
            print("Currently Loan Option Is On \n")
        else:
            print("Currently Loan Option Is Off \n")

    def add_admin(self, admin):
        self.admin_list.append(admin)

    def find_admin(self, name, password):
        for admin in self.admin_list:
            if admin.name == name and admin.password == password:
                return admin
        return None

    def add_account(self, account):
        if self.find_account(account.name):
            print("Account already exists with this user name.\n")
            return
        self.user_account_list.append(account)
        print(f"Account added successfully with account number: {
              account.get_account_number()} \nUser Name: {account.name}\n")

    def find_account(self, user_name):
        for account in self.user_account_list:
            if account.name == user_name:
                return account
        return None

    def user_list(self):
        print("User List:")
        for account in self.user_account_list:
            print(account.name)

    def add_bank_balance(self, balance):
        self._bank_balance += balance

    def decrease_bank_balance(self, balance):
        self._bank_balance -= balance

    def get_bank_balance(self):
        return self._bank_balance

    def add_loan_balance(self, balance):
        self.loan_balance += balance

    def total_loan(self):
        print(f"Total Bank Loan Amount: {self.loan_balance}\n")

    def delete_user(self, username):
        user = self.find_account(username)
        if user:
            self.user_account_list.remove(user)
            print(f"User {username} deleted successfully\n")
        else:
            print(f"User {username} not found\n")

    def loan_option_on(self):
        self.loan_option = True

    def loan_option_off(self):
        self.loan_option = False
