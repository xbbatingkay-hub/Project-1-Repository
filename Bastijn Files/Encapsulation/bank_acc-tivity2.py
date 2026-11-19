# ============================================================
#  BankAccount Encapsulation — complete the class below.
#  The class name, the @property getter lines, and the set_
#  method signatures are already set for you; just fill in the
#  bodies marked with TODO.
# ============================================================

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        self.frozen = False
        pass

    # ----- read-only getters via @property (NO @property.setter!) -----
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    # ----- traditional setter METHODS (called WITH parentheses) -----
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        # check if bank account is frozen
        if self.frozen:
            print("Error: Cannot set balance while bank account is frozen.")
            return

        print(f"Update balance to {balance}")
        # prevent quantum physicists from making another paradox
        if balance < 0:
            print("Error: balance should not be negative")
            return

        self.__balance = balance
        # if sussy, then freeze
        # sussy threshold: 50000 money or greater
        if balance >= 50000:
            print("Warning: suspicious transaction. Bank account has been frozen.")
            self.frozen = True


# ------------------------------------------------------------
#  Step 6 — Test your class.
#  Uncomment and complete the lines below once your class works.
# ------------------------------------------------------------
acct = BankAccount("ACC1", 500)

print(acct.account_number)   # Expected: ACC1   (read — no parentheses)
print(acct.balance)          # Expected: 500    (read — no parentheses)

acct.set_balance(800)        #                 (change via the METHOD)
print(acct.balance)          # Expected: 800

acct.set_balance(-50)        # Expected: a warning is printed
print(acct.balance)          # Expected: 800    (negative was IGNORED!)

# Bonus stuff
acct.set_balance(50000)      # Excepted: suspicious transaction. Bank account has been frozen.
print(acct.balance)          # Expected: 50000    (deposits may still work)

acct.set_balance(800)        # Expected: Cannot set balance while bank account is frozen.
print(acct.balance)          # Expected: 50000