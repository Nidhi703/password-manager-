import sqlite3
import functions
import uuid

# creating database
connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  salt TEXT NOT NULL,
                  hash TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                  u_name TEXT NOT NULL,
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  address TEXT,
                  username TEXT,
                  password TEXT NOT NULL)''')

connection.commit()


def add_data(name, salt, hash):
    # writing new user to database
    cursor.execute("INSERT INTO accounts (name, salt, hash) VALUES (?, ?, ?)", (name, salt, hash))
    connection.commit()


def login_data(name, password):
    # it reads the data and checks user. then returns status
    cursor.execute("SELECT * FROM accounts WHERE name = ?", [name])
    connection.commit()
    result = cursor.fetchall() 
    status = False
    for row in result:
        d_name = row[1]
        d_salt = row[2]
        d_hash = row[3]
        if functions.verify_password(d_salt, d_hash, password) and d_name == name:
            status = True
        else:
            status = False        
    return status


def add_password(u_name, name, address, username, password):
    # writing new password
    cursor.execute("INSERT INTO passwords (u_name, name, address, username, password) VALUES (?, ?, ?, ?, ?)", (u_name, name, address, username, password))
    connection.commit()


def read_password(u_name):
    # reading all password. it filters with main username
    cursor.execute("SELECT * FROM passwords WHERE u_name = ?", [u_name])
    connection.commit()   
    result = cursor.fetchall()
    return result


def search_with_name(name, u_name):
    # it searches with name
    cursor.execute("SELECT * FROM passwords WHERE u_name = ? AND name = ?", (u_name, name))
    connection.commit()   
    result = cursor.fetchall()
    return result


def delete_password(name, u_name):
    # delete password permanently
    cursor.execute("DELETE FROM passwords WHERE u_name = ? AND name = ?", (u_name, name))
    connection.commit()   


def search_with_address(name, u_name):
    # it searches with site address
    cursor.execute("SELECT * FROM passwords WHERE u_name = ? AND address = ?", (u_name, name))
    connection.commit()   
    result = cursor.fetchall()
    return result


def check_name(name):
    # it searches the name in database. it blocks using same username 
    cursor.execute("SELECT name FROM accounts WHERE name = ?", [name])
    connection.commit()   
    result = cursor.fetchall()
    try:
        if name == result[0][0]:
            return True
        else:
            return False
    except:
        return False
