# IMPORTANT
# YOU NEVER DELETE THE "databse.db". IT INCLUDES ALL USERS, PASSWORDS, ETC.

import sql_queries
import title_maker
import main_menu
import functions


def main():
    # writing title and starting login menu
    title_maker.write_title()
    print("Welcome to your terminal password manager.")
    menu()   


def signup():
    # create a new user. before the saving to the database, it hashes the password
    name = input("username: ")
    new_password = input("New password: ")
    new_password_repeat = input("New password(repeat): ")
    check_result = sql_queries.check_name(name)
    if check_result == False:
        if new_password == new_password_repeat:
            hashed_password = functions.hash_password(new_password)
            sql_queries.add_data(name=name, salt=hashed_password[0], hash=hashed_password[1])
        else:
            print("Passwords don't match.")
    else:
        print("This name used before. Please select different name.")
        signup()


def login():
    # it creates a key and the key uses for almost every function in main menu
    name = input("username: ")
    password = input("password: ")
    stat = sql_queries.login_data(name, password)
    if stat == True:
        key_text = name + password
        key = functions.text_to_base64(key_text)
        main_menu.main_menu(key, name)
        return True
    else:
        print("fail")
        return False
        

def menu():
    while True:
        print("For using this app please login. If you don't have an account, you must create an account.")
        print("Choose what you want to do:")
        print("<", "-" * 30, ">")
        print("(1) Log in")
        print("(2) Sign up")
        print("(q) Quit")
        print("<", "-" * 30, ">")

        choice = input("Select something: ")

        if choice == "1":
            print("LOG IN")
            if login() == True:
                break      
        elif choice == "2":
            print("SIGN UP")
            signup()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
