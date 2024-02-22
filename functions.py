import bcrypt
import base64
from cryptography.fernet import Fernet
import sql_queries
from title_maker import table_maker


def hash_password(password):
    salt = bcrypt.gensalt()  
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)  
    return salt, hashed_password  


def verify_password(stored_salt, stored_password, password_to_check):
    hashed_password = bcrypt.hashpw(password_to_check.encode('utf-8'), stored_salt)
    return hashed_password == stored_password


def add_password(u_name, key, name, address, username, password):
    enc_password = encrypt_password(password, key)
    sql_queries.add_password(u_name, name, address, username, enc_password)


def get_password(u_name, key):
    res = sql_queries.read_password(u_name)
    if res != []:
        for i in res:
            enc_password = i[5]
            dec_password = decrypt_password(enc_password, key) 
            text = f"  name: {i[2]} address: {i[3]} username: {i[4]} PASSWORD: {dec_password}  "
            table_maker(text)
    else:
        text = "Passwords aren't found"
        table_maker(text)
        


def get_password_with_name(name, u_name, key):
    i = sql_queries.search_with_name(name, u_name)
    enc_password = i[0][5]
    dec_password = decrypt_password(enc_password, key)
    n = i[0][2] #site name
    a = i[0][3] #address
    us = i[0][4] #username
    return n, a, us, dec_password
    
    


def text_to_base64(text):
    base64_encoded = base64.b64encode(text.encode())
    while len(base64_encoded) < 32:
        base64_encoded += base64_encoded
    base64_encoded = base64_encoded[:32]
    url_safe_encoded = base64.urlsafe_b64encode(base64_encoded).decode()
    return url_safe_encoded


def encrypt_password(password, encryption_key):
    f = Fernet(encryption_key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, encryption_key):
    f = Fernet(encryption_key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password