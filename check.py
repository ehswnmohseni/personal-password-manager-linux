import csv
import decrypt
import log
import emergency
import datetime
import change_key

def check_validaty(word,number,img_status):

    try:

        status = emergency.delete()
        if status == "safe":
            
            with open(r'data1.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    kilid = (row[0])

                    if "b'" in kilid:
                        kilid = kilid.split("'")
                        kilid = kilid[1]


                    me = decrypt.decrypt(kilid)
                    me = str(me)
                    me = me.replace("'","")
                    me = me.replace("b","")
                    me = me.replace("\n","")

            if word == me and img_status == True:
                log.write_log(True)
                return True

            if number >= 3:
                log.write_log("War")
                exit()

            else:
                log.write_log(False)
                return False
            
        else:
            print("Repeat after me you can`t hack this program ;)")
            exit()

    except:
        return False


def check_for_change():

    try:

        time = datetime.datetime.now()
        month = time.month
        day = time.day

        with open(r'logs.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                kilid = (row[0])
                
                kilid = kilid.split(" ")
                kilid = kilid[0].split("-")
                last_day = int(kilid[-1])
                last_month = int(kilid[-2])

        if last_day - day >= 1 or last_month - month >= 1:
            status = change_key.change_all()

    except:
        return False
