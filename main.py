from bank import Bank
from admin import Admin
from account import Account


def admin_fun():
    print("Welcome to Admin Menu:")
    admin = None
    while True:
        if admin is None:
            print("1.Login Admin")
            print("2. Create A New Admin")
            print("3. Exit From User Login Page...")
            try:
                op = int(input("Enter A Option : "))
            except ValueError:
                print("Choose A Valid Option : ")
                continue
            if op == 1:
                print("----Admin Login Option----")
                name = input("Enter Your User Name : ")
                password = input("Enter Your Password : ")
                ad = bank.find_admin(name, password)
                if ad:
                    admin = ad
                    print("Admin Login Successfully!")
                else:
                    print("This Admin Account Not Found!")
                    continue

            elif op == 2:
                print("----New Admin Regstation Option----")
                name = input("Enter Your Name :")
                mail = input("Enter Your Gmail or Yahoo Only :")
                address = input("Enter Your Address :")
                password = input("Enter Your Password :")

                if "gmail" or "yahoo" in mail:
                    email = mail
                else:
                    print("We Accept only  Gmail & Yahoo!\n")
                    continue
                admin = Admin(name, email, address, password, bank)
            elif op == 3:
                print("Exit From Admin Login Page!")
                print("Back To main menu...\n\n\n")
                break

            else:
                print("Invalid Option Choose!Try Again\n")
                continue

        else:
            print("Welcome To Admin Oparation System :")
            print("1. Delete User")
            print("2. User List")
            print("3. Total Available Balance")
            print("4. Total Bank Loan Amount")
            print("5. Check Loan Option Status")
            print("6. Turn off Loan Option")
            print("7. Turn on Loan Option")
            print("8. Bank Is Bankrpted !")
            print("9. Bank is Not Bankrpted")
            print("10. Exit")
            try:
                option = int(input("Enter option: "))
            except ValueError:
                print("You Enter Wrong Option!Please Enter Valid Option")
                try:
                    option = int(input("Enter option: "))
                except ValueError:
                    print("You Enter Wrong Value Again!")
                    continue

            if option == 1:
                username = input("Enter User Name: ")
                admin.delete_user(username)

            elif option == 2:
                admin.user_list()

            elif option == 3:
                admin.total_available_balance()

            elif option == 4:
                admin.total_loan()

            elif option == 5:
                bank.loan_option_status()

            elif option == 6:
                admin.off_loan()
                print("Turned off loan option successfully")
            elif option == 7:
                admin.on_loan_option()
                print("Turned on loan option successfully")
            elif option == 8:
                admin.bankrupted_option_on()
                print("Bank is now bankrupt")

            elif option == 9:
                admin.bankrupted_option_off()
                print("Bank is no longer bankrupt")
            elif option == 10:
                print("Thank you admin for using This Banking System\n\n\n")
                break

# User Menu----------------------------------------------------------------------------------------


def user_fun():
    print("\nWelcome to User Menu:")
    user = None
    while True:
        if user is None:
            print("1.User Login")
            print("2.Create New Account")
            print("3.Exit From User Login Option !")
            try:
                opt = int(input("Enter A Option :"))
            except ValueError:
                print("You Enter Invalid Option!Please Try Again")
                continue

            if opt == 1:
                print("----User Login Option----")
                name = input("Enter Your Name : ")
                user = bank.find_account(name)
                if user:
                    print("Login Successfully!")
                else:
                    print("This Account Not Found!Try Again")
                    continue

            elif opt == 2:
                print("----Create New User account----")
                name = input("Enter Your name : ")
                email = input("Enter Your Email : ")
                address = input("Enter Your Address : ")
                print("Select A Account Type : ")
                account_type = input("Enter Your Account Type : ")
                user = Account(name, email, address, account_type, bank)
                bank.add_account(user)
            elif opt == 3:
                print("Back To Main Menu...")
                break

            else:
                print("Invalid Option!Try Again")
                continue

        else:
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Check Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money")
            print("7. Exit")
            try:
                option = int(input("Enter option: "))
            except ValueError:
                print("Press Valid option!")
                continue

            if option == 1:
                username = input("Enter User Name: ")
                amount = int(input("Enter Deposit Amount: "))
                user = bank.find_account(username)
                if user:
                    user.deposit(amount)
                else:
                    print("This User Account not found!")
            elif option == 2:
                username = input("Enter User Name: ")
                amount = int(input("Enter Withdrawal Amount: "))
                user = bank.find_account(username)
                if user:
                    user.withdraw(amount)
                else:
                    print("This User Account Not Found!")
            elif option == 3:
                username = input("Enter User Name: ")
                user = bank.find_account(username)
                if user:
                    user.check_balance()
                else:
                    print("User not found!")
            elif option == 4:
                username = input("Enter User Name: ")
                user = bank.find_account(username)
                if user:
                    user.check_transaction_history()
                else:
                    print("This User Account not found!")
            elif option == 5:
                username = input("Enter User Name: ")
                amount = int(input("Enter Loan Amount: "))
                user = bank.find_account(username)
                if user:
                    user.take_loan(amount)
                else:
                    print("User not found!")
            elif option == 6:
                sender_name = input("Enter Your Name: ")
                receiver_name = input("Enter Receiver Name: ")
                amount = int(input("Enter Transfer Amount: "))
                sender = bank.find_account(sender_name)
                if sender:
                    sender.transfer_money(receiver_name, amount)
                else:
                    print("Sender not found!")
            elif option == 7:
                print("Thank you for using This Banking System!")
                break
            else:
                print("Incorrect option! Please try again.")


bank = Bank()

while True:
    print("Press 1 For admin interface")
    print("Press 2 For user interface")
    print("Press 3 For Exit")
    try:
        option_function = int(input('Enter A Option Here: '))
    except ValueError:
        print("Press Valid option!")
        continue

    if option_function == 1:
        admin_fun()
    elif option_function == 2:
        user_fun()
    elif option_function == 3:
        print("Thank you for using this Banking System!")
        break
    else:
        print("Incorrect option! Please try again.")
