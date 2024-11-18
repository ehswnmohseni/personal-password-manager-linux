import decrypt
import csv

def add_pass(name,password):

    hash_password = password.encode()
    hash_password = decrypt.encrypt(hash_password)

    data = [[str(name),hash_password]]

    with open(r"path.csv",'a+',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return True