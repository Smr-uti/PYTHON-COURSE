print("start program")
class BankATM:

    # ── Constructor ──────────────────────────────────────
    def __init__(self):
        self.secret_code = ''     # Attribute 1: PIN
        self.account_bal  = 0     # Attribute 2: Balance
        self.show_menu()          # Auto-show menu!

    # ── Method 1: Menu & Routing ─────────────────────────
    def show_menu(self):
        choice = input('''
                  Welcome! Choose an option:
                  1. Create PIN
                  2. Change PIN
                  3. Check Balance
                  4. Withdraw Cash
                  5. Exit
                  Your choice: ''')
        if   choice == '1':
            self.set_pin()
        elif choice == '2':
            self.update_pin()
        elif choice == '3':
            self.check_balance()
        elif choice == '4':
            self.do_withdraw()
        elif choice == '5':
            exit()

    # ── Method 2: Create PIN ─────────────────────────────
    def set_pin(self):
        new_code          = input('Enter new PIN: ')
        self.secret_code  = new_code
        opening           = input('Opening balance: ')
        self.account_bal  = int(opening)
        print('PIN created!')
        self.show_menu()

    # ── Method 3: Change PIN ─────────────────────────────
    def update_pin(self):
        current = input('Current PIN: ')
        if current == self.secret_code:
            fresh            = input('New PIN: ')
            self.secret_code = fresh
            print('PIN updated!')
        else:
            print('Wrong PIN!')
        self.show_menu()

    # ── Method 4: Check Balance ──────────────────────────
    def check_balance(self):
        entered = input('PIN: ')
        if entered == self.secret_code:
            print('Balance:', self.account_bal)
        else:
            print('Wrong PIN!')
        self.show_menu()

    # ── Method 5: Withdraw ───────────────────────────────
    def do_withdraw(self):
        entered = input('PIN: ')
        if entered == self.secret_code:
            amt = int(input('Amount: '))
            if amt <= self.account_bal:  # Balance Guard!
                self.account_bal -= amt
                print('Done! New bal:', self.account_bal)
            else:
                print('Insufficient!')
        else:
            print('Wrong PIN!')
        self.show_menu()

    # ── Launch Application ───────────────────────────────────
obj1 = BankATM()  # One line starts EVERYTHING!
print("end program")