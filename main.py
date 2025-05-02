from sqlConnection import * # Import the methods
# The Main menu function, where everything else branches from
def mainMenu():
    hasAccount = input("Welcome to Hamzah's Banking!\nDo you have an Account?(yes/no) ")
    if (hasAccount == "yes"):
        withAccountMenu()
    elif (hasAccount == "no"):
        accountCreationMenu()

# The Menu for people who already have an account
def withAccountMenu():
    userIn = input("Please Enter an Action:\n1: Update Email\n2: Update Password\n3: Deposit\n4: Withdraw \n5: Display Balance\n6: Delete Account\n")
    if (userIn == "1"):
        # Input the user's necessary info to execute the updateEmail method
        oldEmail = input("Please Enter Your Old Email: ")
        newEmail = input("Please Enter Your New Email: ")
        password1 = input("Please Enter Your Password: ")
        updateEmail(oldEmail, newEmail, password1)
        print("Email Changed Successfully!")
    elif (userIn == "2"):
        # Input the user's necessary info to execute the updatePassword method
        email = input("Please Enter Your Email: ")
        oldPassword = input("Please Enter Your Old Password: ")
        newPassword = input("Please Enter Your New Password: ")
        updatePassword(email, oldPassword, newPassword)
    elif (userIn == "3"):
        # Input the user's necessary info to execute the addBalance method
        email = input("Please Enter Your Email: ")
        password = input("Please Enter Your Password: ")
        amount = float(input("Please Enter Your Deposit Amount: "))
        addBalance(email, password, amount)
    elif (userIn == "4"):
        # Input the user's necessary info to execute the withdrawBalance method
        email = input("Please Enter Your Email: ")
        password = input("Please Enter Your Password: ")
        amount = float(input("Please Enter Your Withdraw Amount: "))
        withdrawBalance(email, password, amount)
    elif (userIn == "5"):
        # Input the user's necessary info to execute the displayBalance method
        email = input("Please Enter Your Email: ")
        password = input("Please Enter Your Password: ")
        displayBalance(email, password)
    elif (userIn == "6"):
        # Confirm to see if the user really wants to delete their account
        confirmation = input("Are You Sure You Would Like to do This? (yes/no)")
        if (confirmation == "yes"):
            # If they confirm, input their details and delete their account
            email = input("Please Enter Your Email: ")
            password = input("Please Enter Your Password: ")
            deleteAccount(email, password)
        elif (confirmation == "no"):
            # Otherwise, return to main menu
            print("Okay! Returning to Main Menu...\n")

# The menu for people who don't have an account and to create an account
def accountCreationMenu():
    print("Welcome to the Account Creation Portal!")
    # Input the user's information to create an account using the makeAccount method
    email = input("Please Input Your Email: ")
    password = input("Please Enter a Password: ")
    startingBalance = float(input("Please Enter a Starting Balance: "))
    makeAccount(email, password, startingBalance)

# Test case to see if the functions work
if __name__ == "__main__":
    wantsToContinue = True
    # Admin password to stop the ATM from running when necessary
    adminPassword = "123asd123asd"
    while True:
        mainMenu()
        if (input("Would You Like to Continue? (yes/no): ") == "no"):
            if (input("Please Enter the Admin Password: ") == adminPassword):
                break