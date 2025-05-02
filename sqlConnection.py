import mysql.connector

def makeAccount(email, password, balance):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"INSERT INTO banking (email, password, balance) VALUES ('{email}', '{password}', {balance})")
    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def deleteAccount(email, password):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"DELETE FROM banking WHERE email='{email}' AND password='{password}'")
    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def updatePassword(email, oldPassword, newPassword):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"UPDATE banking SET password='{newPassword}' WHERE email='{email}' AND password='{oldPassword}'")
    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def updateEmail(oldEmail, newEmail, password):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"UPDATE banking SET email='{newEmail}' WHERE email='{oldEmail}' AND password='{password}'")
    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def addBalance(email, password, deposit):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"SELECT balance FROM banking WHERE email='{email}' AND password='{password}'")
    cursor = connection.cursor()
    cursor.execute(query)
    result = float(cursor.fetchone()[0])
    newBalance = result + deposit

    query = (f"UPDATE banking SET balance='{newBalance}' WHERE email='{email}' AND password='{password}'")
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

def displayBalance(email, password):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"SELECT balance FROM banking WHERE email='{email}' AND password='{password}'")
    cursor = connection.cursor()
    cursor.execute(query)
    result = float(cursor.fetchone()[0])

    connection.commit()
    cursor.close()
    connection.close()
    print(result)

def withdrawBalance(email, password, withdrawBalance):
    connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'bankingdata', password = 'haur@b0t')
    query = (f"SELECT balance FROM banking WHERE email='{email}' AND password='{password}'")
    cursor = connection.cursor()
    cursor.execute(query)
    result = float(cursor.fetchone()[0])
    newBalance = result - withdrawBalance

    query = (f"UPDATE banking SET balance='{newBalance}' WHERE email='{email}' AND password='{password}'")
    cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    print("all G")