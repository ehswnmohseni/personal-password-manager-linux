import csv
import decrypt
import time
import os
import getpass
import new_pass
import check
import change_password
import pyperclip

def return_pass(word):

    try:

        number = 0

        if word == "list" or word == "LIST" or word == "مهسف":
            with open(r'path.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row[0])


        elif word == "exit" or word == "EXIT" or word == "ثطهف":
            print("ok")
            exit()


        elif word == "add" or word == "ADD" or word == "شیی":

            status = False

            while status != True:

                name = input("?")
                if name == "exit":
                    exit()

                password = getpass.getpass(":")
                t_password = getpass.getpass("2:")

                if password == t_password:
                    status = new_pass.add_pass(name,password)


        elif word == "change" or word == "CHANGE" or word == "زاشدلث":

            status = False

            password = getpass.getpass(":")

            status = check.check_validaty(password,number,img_status = True)

            if status == True:
                change_password.change_password(password)

            if status == False:
                number = number + 1
                return_pass("change")

        else:
            with open(r'path.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == word:
                        password = row[1]

                        if "'" in row[1]:
                            password = password.split("'")
                            password = password[1]


                        password = (decrypt.decrypt(password))
                        print("get it",password)
                        pyperclip.copy(password.decode())
                        time.sleep(10)
                        os.system("clear")

    except:
        return False


def return_all():

    try:

        words = []
        passwords = []

        with open(r'path.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                words.append(row[0])
                passwords.append(row[1])

        return [words,passwords]
    
    except:
        return False


def return_all_pass(word):

    try:

        with open(r'path.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row[0] = row[0].encode()
                if row[0] == word:
                    password = row[1]

                    if "'" in row[1]:
                        password = password.split("'")
                        password = password[1]

                    password = (decrypt.decrypt(password))
                    return password
                
    except:
        return False