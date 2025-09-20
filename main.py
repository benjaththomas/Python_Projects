#main.py
from account import Savingsaccount, Checkingaccount
def main():
    accounts = {}
    running = True

    while running:
        print("\n\n============= WELCOME TO ICICI BANK =============")
        print("1. Create a savings account")
        print("2. Create Checking Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View Balance")
        print("6. See all accounts")
        print("7. See all unique account numbers")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("Generating your account number....")
                accowner = str(input("Enter your name :"))
                if accowner.replace(" ", "").isalpha():  # remove spaces, then check only alphabets
                    temp = Savingsaccount(None, None)
                    accno = temp.accountnumbergenerator()
                    print(accno)
                    if accno not in accounts:
                        accounts[accno] = Savingsaccount(accno, accowner)
                        print(f'\nAccount created for {accowner}. And your account number is {accno}')
                    else:
                        print('Account number exists')
                else:
                    print("Invalid input. Name must only contain letters and spaces.")



            case 2:
                accno = int(input("Enter your checking account number: "))
                accowner = input("Enter your name :")
                if accno not in accounts:
                    accounts[accno] = Checkingaccount(accno, accowner)
                    print(f'\nChecking Account created for {accowner}.')
                else:
                    print('Account number exists.')

            case 3:
                accno = int(input("Enter your checking account number: "))
                deposit = float(input("Enter deposit amount: "))
                if accno in accounts:
                    if deposit>0:
                        print(f'${deposit} has been credited to {accno}.')
                        print(f'Your account balance is ${accounts[accno].deposit(deposit)}')
                    else:
                        print(f'Enter a amount above $0.')
                else:
                    print('Account number does not exist in our Database.')

            case 4:
                accno = int(input("Enter your checking account number: "))
                wdramt = float(input("Enter withdrawal amount: "))
                if accno in accounts:
                    if accounts[accno].check(wdramt):
                        print(f'${wdramt} has been debited from {accno}.')
                        print(f'Your account balance is ${accounts[accno].withdraw(wdramt)}')
                    else:
                        print(f'Your account does not hold the amount to withdraw')
                else:
                    print('Account number does not exist in our Database.')

            case 5:
                accno = int(input("Enter your checking account number: "))
                if accno in accounts:
                    print(f'Your account balance is ${accounts[accno].get_balance()}.')

            case 6:
                for key, values in accounts.items():
                    print(f'{key}:{values}')

            case 7:
                print(f'{accounts[accno].all_accounts()}')

            case 8:
                running = False
                print("Goodbye!")

            case _:
                print("Invalid choice. Please try again..")


if __name__ == "__main__":
    main()