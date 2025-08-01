""" Project: Personal Diary App """

import getpass
from cryptography.fernet import Fernet
import os
from datetime import datetime

# ENCRYPTION SETUP

# generate and save a key
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

# load the key
def load_key():
    return open("secret.key", "rb").read()

# encrypt text
def encrypt_text(text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

# decrypt text
def decrypt_text(encrypted_text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode()

# DIARY FUNCTION

def create_entry():
    title = input("Enter the title of your dairy entry: ")
    content = input("Enter your diary content: ")
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # encrypt content
    encrypted_content = encrypt_text(content)

    os.makedirs("entries", exist_ok= True)

    file_name = f"{date}_{title}.txt"
    with open(os.path.join("entries", file_name), "wb") as file:
        file.write(encrypted_content)
    print(f"Diary entry '{title}' saved successfully")

def list_entries():
    os.makedirs("entries", exist_ok= True)
    entries = os.listdir("entries")
    if entries:
        print("Your diary entries: ")
        for index, entry in enumerate(entries, start = 1):
            print(f"{index}. {entry}")
    else:
        print("No diary entries found.")

def read_entry():
    list_entries()
    file_name = input("Enter the name of the entry to read: ")
    file_path = os.path.join("entries", file_name)

    try:
        with open(file_path, "rb") as file:
            encrypted_content = file.read()
        content = decrypt_text(encrypted_content)
        print("\nDiary entry content: ")
        print(content)

    except FileNotFoundError:
        print("Entry not found!")

# authentication
def authenticate():
    correct_password = "mypassword" # set your password here
    password = getpass.getpass("Enter your password: ")
    if password == correct_password:
        print("Accessed Granted!")
        return True
    else:
        print("Access denied!")
        return False

# main app  
def main():
    generate_key()
    if authenticate():
        while True:
            print("\nOptions:")
            print("1. Create new entry")
            print("2. View all entries")
            print("3. Read an entry")
            print("4. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                create_entry()
            elif choice == "2":
                list_entries()
            elif choice == "3":
                read_entry()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()