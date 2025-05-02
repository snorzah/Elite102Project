from sqlConnection import *
def mainMenu():
    hasAccount = input("Welcome to ___ Banking!\nDo you have an Account?(yes/no) ")
    if (hasAccount == "yes"):
        withAccountMenu()
    elif (hasAccount == "no"):
        accountCreationMenu()

def withAccountMenu():
    userIn = input("Please Enter an Action:\n1: Update Email\n2: Update Password\n3: Deposit\n4: Withdraw \n5: Display Balance\n6: Delete Account\n")
    if (userIn == "1"):
        oldEmail = input("Please Enter Your Old Email: ")
        newEmail = input("Please Enter Your New Email: ")
        password1 = input("Please Enter Your Password: ")
        updateEmail(oldEmail, newEmail, password1)
        print("Email Changed Successfully!")
    elif (userIn == "2"):
        email = input("Please Enter Your Email: ")
        oldPassword = input("Please Enter Your Old Password: ")
        newPassword = input("Please Enter Your New Password: ")
        updatePassword(email, oldPassword, newPassword)
    elif (userIn == "3"):
        email = input("Please Enter Your Email: ")
        password = input("Please Enter Your Password: ")
        amount = float(input("Please Enter Your Deposit Amount: "))
        addBalance(email, password, amount)
    elif (userIn == "4"):
        email = input("Please Enter Your Email: ")
        password = input("Please Enter Your Password: ")
        amount = float(input("Please Enter Your Withdraw Amount: "))
        withdrawBalance(email, password, amount)
    elif (userIn == "5"):
        email = input("Please Enter Your Email: ")
        password = input("Please Enter Your Password: ")
        displayBalance(email, password)
    elif (userIn == "6"):
        confirmation = input("Are You Sure You Would Like to do This? (yes/no)")
        if (confirmation == "yes"):
            email = input("Please Enter Your Email: ")
            password = input("Please Enter Your Password: ")
            deleteAccount(email, password)
        elif (confirmation == "no"):
            print("Okay! Returning to Main Menu...\n")

def accountCreationMenu():
    print("Welcome to the Account Creation Portal!")
    email = input("Please Input Your Email: ")
    password = input("Please Enter a Password: ")
    startingBalance = float(input("Please Enter a Starting Balance: "))
    makeAccount(email, password, startingBalance)

if __name__ == "__main__":
    wantsToContinue = True
    adminPassword = "123asd123asd"
    while True:
        mainMenu()
        if (input("Would You Like to Continue? (yes/no): ") == "no"):
            if (input("Please Enter the Admin Password: ") == adminPassword):
                break