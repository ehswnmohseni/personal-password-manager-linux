import csv
import decrypt
import getpass
import os

def change_password(password):

    try:

        status = False

        while status != True:

            print("you can exit")

            password = getpass.getpass("new:")
            if password == "exit": 
                exit()
        
            password_2 = getpass.getpass("new 2:")
            if password_2 == "exit":
                exit()

            if password == password_2:
                status = True

        password = password.encode()
        password = decrypt.encrypt(password)

        data = [[password]]

        os.remove(r"data1.csv")

        with open(r"data1.csv",'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    except:
        return False