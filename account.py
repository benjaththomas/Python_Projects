#account.py
import random
count = 0
repeat_count = 0
generated_accounts = set()

class Savingsaccount:
    def __init__(self, accnum, accname):
        self.accnum = accnum
        self.accname = accname
        self.balance = 0.0

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdrawalamt):
        self.balance -= withdrawalamt
        return self.balance

    def get_balance(self):
        return self.balance

    def check(self, withdrawalamount):
        if withdrawalamount > self.balance:
            print(f'Your account balance is ${self.balance}')
            return False
        else:
            return True

    def accountnumbergenerator(self, prefix="600096", total_length=12):
        global count, repeat_count

        remaining = total_length - len(prefix)
        digits = ''.join(str(random.randint(0, 9)) for i in range(remaining))
        new_account = prefix + digits
        if new_account not in generated_accounts:
            generated_accounts.add(new_account)
            count += 1
            return int(new_account)
        else:
            repeat_count += 1
            return int(self.accountnumbergenerator(prefix,total_length))

    def all_accounts(self):
        return generated_accounts


class Checkingaccount:
    def __init__(self, accnum, accname):
        self.accnum = accnum
        self.accname = accname
        self.balance = 0.0

