from cryptography.fernet import Fernet
import csv

def encrypt(text):

    try:

        with open('no_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                kilid = (row[0])
                if "b'" in kilid:
                    kilid = kilid.replace("'","")
                    kilid = kilid.replace("b","")
                    kilid = kilid.replace("\n","")
                    kilid=kilid.encode()
    
        f = Fernet(kilid)
        encrypted = f.encrypt(text)

        return encrypted
    
    except:
        return False

def decrypt(hash):

    try:

        with open('no_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                kilid = (row[0])
                if "b'" in kilid:
                    kilid = kilid.replace("'","")
                    kilid = kilid.replace("b","")
                    kilid = kilid.replace("\n","")
                    kilid=kilid.encode()

        m = Fernet(kilid)
        decrypted = m.decrypt(hash)

        return decrypted

    except:
        return False
 
def encrypt_with_key(password,key):

    try:

        password = str(password)
        key = str(key)

        if "b'" in key:
            key = key.replace("'","")
            key = key.replace("b","")
            key = key.replace("\n","")

        if "b'" in password:
            password = password.replace("'","")
            password = password.replace("b","")
            password = password.replace("\n","")
            password = password.encode()

        key = key.encode()

        try:
            func = Fernet(key)
            encrypted = func.encrypt(password)
            return encrypted

        except ValueError:
            pass

    except:
        return False
    
