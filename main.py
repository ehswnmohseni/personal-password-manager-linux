import check
import return_pass
import os
import getpass
import time
import internet_connection
import face

try:
    internet = internet_connection.check_internet_connection()
    status = check.check_for_change()
    number = 0
    start_time = 0

    while internet == False:
        
        print("send me picture key.jpg in /home/your_os_name/Pictures/images or enable webcam")
        word = getpass.getpass(":")

        img_status = face.check_validaty()
        status = check.check_validaty(word,number,img_status)

        if status == True and img_status == True:  
            start_time = time.time()
            os.system("clear")

        else:
            number = number + 1
            os.system("clear")

        while status == True and time.time() - start_time < 120 and img_status == True:

            word = input("?")
            if time.time() - start_time < 120:
                return_pass.return_pass(word)

            else:
                import main
                break

    if internet == True:
        print("Please disconnect the internet, And run the program again.")
except:
    print("i got error in main file")