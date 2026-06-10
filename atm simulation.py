class ATM:
    def __init__(self):
        self.balance = 1000.0
        self.pin = "1234"
        self.account_active = True

    def display_menu(self):
        print("\n=== ATM Menu ===")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Delete Account")
        print("5. Exit")
        print("================")

    def balance_inquiry(self):
        if not self.account_active:
            print("Account is deleted. Cannot perform operations.")
            return
        print(f"\nCurrent Balance: ${self.balance:.2f}")

    def deposit(self):
        if not self.account_active:
            print("Account is deleted. Cannot perform operations.")
            return
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
                return
            self.balance += amount
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdrawal(self):
        if not self.account_active:
            print("Account is deleted. Cannot perform operations.")
            return
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
                return
            if amount > self.balance:
                print("Insufficient funds.")
                return
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def delete_account(self):
        if not self.account_active:
            print("Account is already deleted.")
            return
        confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
        if confirm == "yes":
            pin_verify = input("Enter your PIN to confirm deletion: ")
            if pin_verify == self.pin:
                self.account_active = False
                self.balance = 0
                print("Account deleted successfully.")
            else:
                print("Incorrect PIN. Account deletion cancelled.")
        else:
            print("Account deletion cancelled.")

    def run(self):
        print("Welcome to the ATM Simulation!")
        
        # PIN verification
        pin_attempts = 3
        while pin_attempts > 0:
            pin = input("Enter your PIN (default: 1234): ")
            if pin == self.pin:
                print("PIN verified. Access granted.")
                break
            else:
                pin_attempts -= 1
                print(f"Incorrect PIN. {pin_attempts} attempts remaining.")
        
        if pin_attempts == 0:
            print("Too many incorrect attempts. Access denied.")
            return

        # Main menu loop
        while self.account_active:
            self.display_menu()
            try:
                choice = input("Enter your choice (1-5): ")
                
                if choice == "1":
                    self.balance_inquiry()
                elif choice == "2":
                    self.deposit()
                elif choice == "3":
                    self.withdrawal()
                elif choice == "4":
                    self.delete_account()
                elif choice == "5":
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                break
        
        if not self.account_active:
            print("Account has been deleted. Session ended.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
