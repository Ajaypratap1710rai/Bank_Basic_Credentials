import getpass

class Bank:
    def __init__(self, bank_name, ifsc_code, branch):
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.branch = branch

class User:
    def __init__(self, name, account_number, balance, user_id, password):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.user_id = user_id
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        print(f"Withdrew {amount}. New Balance: {self.balance}")
        return True 

    def transfer(self, amount, recipient):
        if self.withdraw(amount):
            recipient.deposit(amount)
            print(f"Transferred {amount} to {recipient.name}")

    def authenticate(self, password):
        return self.password == password

def display_menu():
    print("\nChoose Below Option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Transfer Money")
    print("4. Check Balance")
    print("5. Exit")

def create_user(users):
    user_name = input("Enter the Name for the new User: ")
    account_number = input("Enter the Account Number for the new User: ")
    balance = float(input("Enter the Initial Amount for the new User: "))
    user_id = input("Enter Username for the new User: ")
    while True:
        password = getpass.getpass("Enter Password for the new User: ")
        confirm_password = getpass.getpass("Confirm Password: ")
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")
    new_user = User(user_name, account_number, balance, user_id, password)
    users[user_id] = new_user
    print(f"User {user_name} created successfully.")

def main():
    # Bank Details
    bank_name = input("Enter the Bank Name: ")
    ifsc_code = input("Enter the IFSC Code: ")
    branch_name = input("Enter the Branch Name: ")
    bank = Bank(bank_name, ifsc_code, branch_name)

    users = {}

    create_user(users)
    while True:
        create_new_user = input("Do you want to create another user? (yes/no): ").strip().lower()
        if create_new_user == 'yes':
            create_user(users)
        elif create_new_user == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        display_menu()
        choice = input("Enter Your Choice: ")

        if choice == '1':  # Deposit Money
            user_id = input("Enter the User ID for Deposit: ")
            amount = float(input("Enter the amount to deposit: "))
            user = users.get(user_id)
            if user:
                user.deposit(amount)
            else:
                print("Invalid user ID.")

        elif choice == '2':  # Withdraw Money
            user_id = input("Enter the User ID for Withdrawal: ")
            password = getpass.getpass("Enter Password: ")
            user = users.get(user_id)
            if user and user.authenticate(password):
                amount = float(input("Enter the amount to withdraw: "))
                user.withdraw(amount)
            else:
                print("Invalid user ID or incorrect password.")

        elif choice == '3':  # Transfer Money
            sender_id = input("Enter the Sender's User ID: ")
            receiver_id = input("Enter the Receiver's User ID: ")
            password = getpass.getpass("Enter Sender's Password: ")
            sender = users.get(sender_id)
            receiver = users.get(receiver_id)
            if sender and receiver and sender.authenticate(password):
                amount = float(input("Enter the amount to transfer: "))
                sender.transfer(amount, receiver)
            else:
                print("Invalid sender ID, receiver ID, or incorrect password.")

        elif choice == '4':  # Check Balance
            while True:
                user_id = input("Enter the User ID to check balance: ")
                password = getpass.getpass("Enter Password: ")
                user = users.get(user_id)
                if user and user.authenticate(password):
                    print(f"Current Balance for {user.user_id}: {user.balance}")
                    break
                else:
                    print("Invalid user ID or incorrect password. Please try again.")

        elif choice == '5':  # Exit
            print("Thanks for using the banking system!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
