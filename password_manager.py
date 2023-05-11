from cryptography.fernet import Fernet
import os
import os.path
from os.path import exists

#Will Make key for encryiption/decryption(Comment out lines 7-11 after first excecution)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()

#Will load the key from key.key file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#Deletes password, takes the line of the stored information as a parameter
def delete(skip):
    if skip - 1 <= 0:
        print("Invalid Input, Redicting to main menu.")
        cont()
    else:
        with open('passwords.txt', 'r') as read_file:
            lines = read_file.readlines()

        currentLine = 1
        with open('passwords.txt', 'w') as write_file:
            for line in lines:
                if currentLine == skip:
                    pass
                else:
                    write_file.write(line)

                currentLine += 1
        print("Line deleted! Redirecting to main menu.")
        print(' ')
        cont()

#Will let user view the stored information
def view():
    print(' ')

    with open('passwords.txt', 'r') as f:
        next(f)
        index = 0
        for line in f.readlines():
            index += 1
            data = line.rstrip()
            web, user, passw = data.split("|")
            print(index, ": ", "Website:", web, "| User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

    print(' ')
    cont()

#Will let user input information 
def add():
    print(' ')

    website = input('Website: ')
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(website + '|' + name + "|" +
                fer.encrypt(pwd.encode()).decode() + "\n")

    print("Added! Returning to main menu.")
    print(' ')
    cont()

#Main Menu - redirects user from input
def cont():

    print("If you want to add a password, type add")
    print("If you want to view a password, type view")
    print("If you want to delete a password, type delete")
    print("If you want to quit , type q")

    while True:
        mode = input("Enter a choice listed above: ")
        if mode == "q":
            break
        elif mode == 'view':
            view()
        elif mode == 'add':
            add()
        elif mode == 'delete':
            print(' ')
            with open('passwords.txt', 'r') as f:
                next(f)
                index = 0
                for line in f.readlines():
                    index += 1
                    data = line.rstrip()
                    web, user, passw = data.split("|")
                    print(index, ": ", "Website:", web, "| User:", user, "| Password:",
                          fer.decrypt(passw.encode()).decode())
            print(' ')
            index = int(input("Enter line number to be deleted: "))
            index += 1
            delete(index)
        else:
            print("Invalid mode.")
            continue


file_exists = os.path.exists('passwords.txt')

#If passwords.txt does not exist or is empty, create a master password
if file_exists == False or os.path.getsize('passwords.txt') == 0:

    master_pwd = input("Create a master password by entering a password (Don't forget this!): ")
    print("Master Password Set: " + master_pwd)

    key = load_key() + master_pwd.encode()
    fer = Fernet(key)

    with open('passwords.txt', 'a') as f:
        f.write(fer.encrypt(master_pwd.encode()).decode() + "\n")

    cont()

#If passwords.txt is not empty or does exist, enter the master password and authenticate
else:

    input_pass = input('Welcome back! Enter the Master password to continue: ')

    with open('passwords.txt', 'r') as fp:
        first_item = fp.readline().strip()

    key = load_key()
    fer = Fernet(key)

    if input_pass.encode() in fer.decrypt(first_item.encode().decode()):
        print("Master Password Entered: " + input_pass)
        print("Redirecting to main menu")
        cont()
    else:
        print("Master Password Entered: " + input_pass)
        print("Incorrect password, run program to try again.")
