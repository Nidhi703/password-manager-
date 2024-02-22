import functions
import sql_queries
from title_maker import table_maker


def main_menu(key, u_name):
    print("You're logged in.")
    print("Choose what you want to do:")
    print("<", "-" * 30, ">")
    print("(1) Add password ")
    print("(2) Delete password")
    print("(3) Search password with site name")
    print("(4) Search password with site address")
    print("(5) List all passwords")
    print("(q) Quit")
    print("<", "-" * 30, ">")
    
    choice = input("Select something: ")

    if choice == "1":
        print("Add password")
        print("<", "-" * 30, ">")
        name = input("Site name: ")
        address = input("Site address: ")
        username = input("Username: ")
        password = input("Password: ")
        print("<", "-" * 30, ">")
        functions.add_password(u_name, key, name, address, username, password)
        main_menu(key, u_name) 
    elif choice == "2":
        print("Delete password")
        name = input("Site name: ")
        sql_queries.delete_password(name, u_name)
        main_menu(key, u_name)
    elif choice == "3":
        print("Search password with site name")
        name = input("Site name: ")
        try:
            pass_text = functions.get_password_with_name(name, u_name, key)
            f_text = f"name: {pass_text[0]} | address: {pass_text[1]} | username: {pass_text[2]} | PASSWORD: {pass_text[3]}"
            table_maker(f_text)
            main_menu(key, u_name)
        except:
            text = "Password isn't found"
            table_maker(text)
            main_menu(key, u_name) 
    elif choice == "4":
        print("Search password with site address")
        address = input("Site address: ")
        try:
            passwords = sql_queries.search_with_address(address, u_name)
            for i in passwords:
                f_text = f"name: {i[2]} | address: {i[3]} | username: {i[4]} | PASSWORD: {functions.decrypt_password(i[5], key) }"
                table_maker(f_text)
                main_menu(key, u_name)
        except:
            text = "Password isn't found"
            table_maker(text)
            main_menu(key, u_name)
    elif choice == "5": 
        try:
            print("List all passwords")
            functions.get_password(u_name, key) 
            main_menu(key, u_name) 
        except:
            text = "Passwords aren't found"
            table_maker(text)
            main_menu(key, u_name)    
    elif choice == "q":
        print("Goodbye!")
    else:
        text = "Invalid choice. Please try again."
        table_maker(text)
        main_menu(key, u_name)