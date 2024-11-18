import csv
import return_pass
from cryptography.fernet import Fernet
import decrypt
    
def change_all():

    try:

        org = None

        #read password of login
        with open(r'data1.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                last_pass = (row[0])

                if "b'" in last_pass:
                    last_pass = last_pass.split("'")
                    last_pass = last_pass[1]

                last_pass = last_pass.encode()
                me = decrypt.decrypt(last_pass) 
                me = str(me)
                me = me.replace("'","")
                me = me.replace("b","")
                me = me.replace("\n","")
                last_pass = me.encode()

        #get list of passwords
        data = return_pass.return_all()
        words = data[0]

        #get all of passwords from words
        passwords = [] 
        for word in words:
            word = word.encode()
            password = return_pass.return_all_pass(word)
            if password != None:
                passwords.append(password)

        hashs = [None]
        while None in hashs:
            #change key
            new_key = Fernet.generate_key()
            with open(r'no_data.csv', 'w+',newline='') as new_file:
                me = str(new_key)
                me = me.replace("'","")
                me = me.replace("b","")
                me = me.replace("\n","")
                new_key = [[me]]
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(new_key[0])
            

            #get hash of passwords with new key
            hashs = []
            for password in passwords:
                hash = decrypt.encrypt_with_key(password,new_key[0][0])
                hashs.append(hash)

            #delete older file
            with open(r"path.csv",'w',newline='') as new_file:
                print("changed key!")

            #write data word and pass in file 
            for i in range(len(words)):
                data = [[words[i],hashs[i]]]
                with open(r"path.csv",'a+',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)

            #change login password 
            new_key = new_key[0][0].encode()
            org = decrypt.encrypt_with_key(last_pass,new_key)
            with open(r"data1.csv",'w',newline='') as file:
                writer = csv.writer(file)
                org = [[org]]
                writer.writerows(org)

    except:
        return False