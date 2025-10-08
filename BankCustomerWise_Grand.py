class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.account_active = True
        self.cheque_book_requested = False

    def check_balance(self):
        if not self.account_active:
            print("Error: Account is frozen.")
            return None
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")
        return True

    def withdraw(self, amount):
        if not self.account_active:
            print("Error: Account is frozen.")
            return False
        if amount > self.balance:
            print("Error: Insufficient funds.")
            return False
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")
        return True

    def request_cheque_book(self):
        if self.cheque_book_requested:
            print("Error: A cheque book has already been requested.")
            return False
        self.cheque_book_requested = True
        print("Cheque book request approved.")
        return True

    def freeze_account(self):
        if not self.account_active:
            print("Error: Account is already frozen.")
            return False
        self.account_active = False
        print("Account has been frozen.")
        return True

    def unfreeze_account(self):
        if self.account_active:
            print("Error: Account is already active.")
            return False
        self.account_active = True
        print("Account has been unfrozen.")
        return True


class SavingsAccount(BankAccount):
    def __init__(self, name, initial_balance, pin):
        super().__init__(initial_balance)
        self.name = name
        self._pin = pin
        self.daily_withdrawal_limit = 1000
        self.atm_card_requested = False

    def _validate_pin(self, entered_pin):
        return self._pin == entered_pin

    def check_balance(self, pin):
        if not self._validate_pin(pin):
            print("Error: Invalid PIN.")
            return None
        print(f"Balance for {self.name}: {super().check_balance()}")

    def withdraw(self, amount, pin):
        if not self._validate_pin(pin):
            print("Error: Invalid PIN.")
            return False
        if not self.account_active:
            print("Error: Account is frozen.")
            return False
        if amount > self.daily_withdrawal_limit:
            print(f"Error: Exceeds daily withdrawal limit of {self.daily_withdrawal_limit}.")
            return False
        return super().withdraw(amount)

    def deposit(self, amount, pin):
        if not self._validate_pin(pin):
            print("Error: Invalid PIN.")
            return False
        return super().deposit(amount)

    def request_atm_card(self):
        if self.atm_card_requested:
            print("Error: An ATM card has already been requested.")
            return False
        self.atm_card_requested = True
        print("ATM card request approved.")
        return True


class BusinessAccount(BankAccount):
    def __init__(self, business_name, initial_balance):
        super().__init__(initial_balance)
        self.business_name = business_name
        self.overdraft_limit = 5000  # Example limit
        self.loan_limit = 25000  # Example limit

    def check_balance(self):
        print(f"Balance for {self.business_name}: {super().check_balance()}")

    def withdraw(self, amount):
        if not self.account_active:
            print("Error: Account is frozen.")
            return False
        if amount > (self.balance + self.overdraft_limit):
            print("Error: Withdrawal amount exceeds balance and overdraft limit.")
            return False
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")
        return True

    def request_loan(self, amount):
        if amount > self.loan_limit:
            print(f"Error: Loan request exceeds the limit of {self.loan_limit}.")
            return False
        print(f"Loan request of {amount} approved.")
        return True


# 1. Create Savings Account object
savings = SavingsAccount("John Doe", 2000, "1234")

# 2. Check balance with correct PIN
savings.check_balance("1234")

# 3. Check balance with wrong PIN
savings.check_balance("0000")

# 4. Withdraw money within limit with correct PIN
savings.withdraw(500, "1234")

# 5. Withdraw money above limit
savings.withdraw(1500, "1234")

# 6. Withdraw money with wrong PIN
savings.withdraw(100, "9999")

# 7. Deposit money with correct PIN
savings.deposit(300, "1234")

# 8. Deposit money with wrong PIN
savings.deposit(100, "9999")

# 9. Request ATM card
savings.request_atm_card()

# 10. Request ATM card again
savings.request_atm_card()

# 11. Request cheque book
savings.request_cheque_book()

# 12. Request cheque book again
savings.request_cheque_book()

# 13. Freeze account
savings.freeze_account()

# 14. Withdraw after freeze
savings.withdraw(100, "1234")

# 15. Unfreeze account
savings.unfreeze_account()

print("____________________________________________________________________________")

# 16. Create Business Account object
business = BusinessAccount("Grand Enterprises", 10000)

# 17. Check balance
business.check_balance()

# 18. Withdraw money within overdraft limit
business.withdraw(12000)

# 19. Withdraw money above overdraft limit
business.withdraw(4000)

# 20. Request loan within limit
business.request_loan(20000)

# 21. Request loan above limit
business.request_loan(30000)

# 22. Request cheque book
business.request_cheque_book()
