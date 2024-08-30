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
    print("4. Exit")

def main():
    # Bank Details
    bank_name = input("Enter the Bank Name: ")
    ifsc_code = input("Enter the IFSC Code: ")
    branch_name = input("Enter the Branch Name: ")
    bank = Bank(bank_name, ifsc_code, branch_name)

    # User Details
    user1_name = input("Enter the Name for User 1: ")
    user1_account_number = input("Enter the Account Number for User 1: ")
    user1_balance = float(input("Enter the Initial Amount for User 1: "))
    user1_id = input("Enter Username for User 1: ")
    while True:
        password = getpass.getpass("Enter Password for User 1: ")
        confirm_password = getpass.getpass("Confirm Password: ")
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")
    user1 = User(user1_name, user1_account_number, user1_balance, user1_id, password)

    user2_name = input("Enter the Name for User 2: ")
    user2_account_number = input("Enter the Account Number for User 2: ")
    user2_balance = float(input("Enter the Initial Amount for User 2: "))
    user2_id = input("Enter Username for User 2: ")
    while True:
        password = getpass.getpass("Enter Password for User 2: ")
        confirm_password = getpass.getpass("Confirm Password: ")
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")
    user2 = User(user2_name, user2_account_number, user2_balance, user2_id, password)

    while True:
        display_menu()
        choice = input("Enter Your Choice: ")

        if choice == '1':  # Deposit Money
            user_input = input("Enter the User Name for Deposit: ")
            amount = float(input(f"Enter the amount to deposit for {user_input}: "))
            if user_input == user1_name:
                user1.deposit(amount)
            elif user_input == user2_name:
                user2.deposit(amount)
            else:
                print("Invalid user name.")    

        elif choice == '2':  # Withdraw Money
            user_input = input("Enter the User Name for Withdrawal: ")
            password = getpass.getpass("Enter Password: ")

            if user_input == user1_name:
                user = user1
            elif user_input == user2_name:
                user = user2
            else:
                print("Invalid user name.")
                continue
            
            if user.authenticate(password):                 #        -----------Authentication process------------------------
                amount = float(input(f"Enter the amount to withdraw for {user_input}: "))
                user.withdraw(amount)
            else:
                print("Incorrect password.")

        elif choice == '3':  # Transfer Money
            sender_name = input("Enter the Sender's User Name: ")
            receiver_name = input("Enter the Receiver's User Name: ")
            password = getpass.getpass("Enter Sender's Password: ")

            if sender_name == user1_name:
                sender = user1
            elif sender_name == user2_name:
                sender = user2
            else:
                print("Invalid sender name.")
                continue
            
            if sender.authenticate(password):
                if receiver_name == user1_name:
                    recipient = user1
                elif receiver_name == user2_name:
                    recipient = user2
                else:
                    print("Invalid recipient name.")
                    continue
                
                amount = float(input(f"Enter the amount to transfer from {sender_name} to {receiver_name}: "))
                sender.transfer(amount, recipient)
            else:
                print("Incorrect password.")
        
        elif choice == '4':  # Exit
            print("Thanks for using the banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Display updated balances
        print(f"Current Balance for {user1_name}: {user1.balance}")
        print(f"Current Balance for {user2_name}: {user2.balance}")

if __name__ == "__main__":
    main()
