import csv
import os

def delete():

    bad_number = 0 

    with open(r'logs.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:

            if "War" in row:
                bad_number = bad_number + 1
                
            if "True" in row:
                bad_number = 0

    if bad_number >= 3:

        os.remove(r'no_data.csv')

        os.remove(r"logs.csv")

        os.remove(r"path.csv")

        os.remove(r'data1.csv')

        os.remove(r'check.py')

        os.remove(r'return_pass.py')

        os.remove(r'log.py')

        os.remove(r'main.py')

        os.remove(r'emergency.py')

        os.remove(r'make_hash.py')

        os.remove(r'decrypt.py')

            #os.removedirs(r'C:\Users\free\AppData')

    else:
        return "safe"