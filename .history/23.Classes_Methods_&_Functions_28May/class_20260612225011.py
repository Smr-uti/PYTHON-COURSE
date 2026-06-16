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
        elif choice ==