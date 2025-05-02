import mysql.connector

# Making an account to the database based on email, password, and initial balance
def makeAccount(email, password, balance):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"INSERT INTO banking (email, password, balance) VALUES ('{email}', '{password}', {balance})")
    cursor = connection.cursor()
    cursor.execute(query)
    # Add and close the connection to SQL
    connection.commit()
    cursor.close()
    connection.close()

# Deleting an account based on email. Requires password (self explanatory: for safety reasons)
def deleteAccount(email, password):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"DELETE FROM banking WHERE email='{email}' AND password='{password}'")
    # Create a cursor and execute the command
    cursor = connection.cursor()
    cursor.execute(query)
    # Add and close the connection to SQL
    connection.commit()
    cursor.close()
    connection.close()

# Update your password based on your email, previous password, and new password. Requires old password (self explanatory: for safety reasons)
def updatePassword(email, oldPassword, newPassword):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"UPDATE banking SET password='{newPassword}' WHERE email='{email}' AND password='{oldPassword}'")
    # Create a cursor and execute the command
    cursor = connection.cursor()
    cursor.execute(query)
    # Add and close the connection to SQL
    connection.commit()
    cursor.close()
    connection.close()

# Update your email based on your old email, new email, and password (needed for safety reasons)
def updateEmail(oldEmail, newEmail, password):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"UPDATE banking SET email='{newEmail}' WHERE email='{oldEmail}' AND password='{password}'")
    # Create a cursor and execute the command
    cursor = connection.cursor()
    cursor.execute(query)
    # Add and close the connection to SQL
    connection.commit()
    cursor.close()
    connection.close()

# Add money to your balance based on your email, password, and the amount you want to sign in with
def addBalance(email, password, deposit):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"SELECT balance FROM banking WHERE email='{email}' AND password='{password}'")
    # Create a cursor and execute the command
    cursor = connection.cursor()
    cursor.execute(query)
    result = float(cursor.fetchone()[0])
    newBalance = result + deposit

    query = (f"UPDATE banking SET balance='{newBalance}' WHERE email='{email}' AND password='{password}'")
    cursor.execute(query)
    # Add and close the connection to SQL
    connection.commit()
    cursor.close()
    connection.close()

# Show your balance based on your email and password
def displayBalance(email, password):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"SELECT balance FROM banking WHERE email='{email}' AND password='{password}'")
    # Create a cursor and execute the command
    cursor = connection.cursor()
    cursor.execute(query)
    result = float(cursor.fetchone()[0])
    # Add and close the connection to SQL
    connection.commit()
    cursor.close()
    connection.close()
    print(result)

# Takes money out of your account based on email, password, and how much you want to take out
def withdrawBalance(email, password, withdrawBalance):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"SELECT balance FROM banking WHERE email='{email}' AND password='{password}'")
    # Create a cursor and execute the command
    cursor = connection.cursor()
    cursor.execute(query)
    result = float(cursor.fetchone()[0])
    newBalance = result - withdrawBalance

    query = (f"UPDATE banking SET balance='{newBalance}' WHERE email='{email}' AND password='{password}'")
    cursor.execute(query)
    # Add and close the connection to SQL
    connection.commit()
    cursor.close()
    connection.close()

#Test cases
if __name__ == "__main__":
    #makeAccount("hamzah@gmail.com", "1234asdf", 99.99)
    #updatePassword("hamzah@gmail.com", "1234asdf", "properPassword123")
    #updateEmail("hamzah@gmail.com", "hamzahR@gmail.com", "properPassword123")
    #addBalance("hamzahR@gmail.com", "properPassword123", 100.99)
    #withdrawBalance("hamzahR@gmail.com", "properPassword123", 20.99)
    #displayBalance("hamzahR@gmail.com", "properPassword123")
    #deleteAccount("hamzahR@gmail.com", "properPassword123")
    print("All Good!")