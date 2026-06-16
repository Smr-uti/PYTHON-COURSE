print("Start Program")

class BankATM:
    def __init__(self):
        self.secret_code = ''
        self.account_bal = 0
        self.show_menu()

    def show_menu(self):
        input(''' 
              Welcome! Choose an option:
              1. Create PIN
              2. Change PIN
              3. Check Balance
              4. Withdraw Cash
              5. Exit
              Your Choice: ''')

        if choice == '1':
            self.set_pin()
        elif choice == '2':
            self.update_pin()
        elif choice == '3':
            self.check_balance()
        elif choice == '4':
            self.withdraw_cash()
        elif choice == '5':
            exit()

    def set_pin(self):
        new_code = input("Enter new PIN: ")
        self.secret_code = new_code
        opening = input("Opening Balance: ")
        self.account_bal = float(opening)
        print("PIN created!")
        self.show_menu()

    def update_pin(self):
        current = input("Enter Current PIN: ")
        if current == self.secret_code:
            fresh = input("Enter New PIN: ")
            self.secret_code = fresh
            print("PIN updated!")
        else:
            print("Wrong PIN!")
        self.show_menu()

    def check_balance(self):
        entered = input("PIN:")
        if entered == self.secret_code:
            print("Balance :" self.account_bal)
        else:
            print("Wrong PIN!")
        self.show_menu()

    def