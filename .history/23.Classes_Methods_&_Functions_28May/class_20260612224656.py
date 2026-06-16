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
              2.)