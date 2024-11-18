import datetime
import csv

def write_log(status):

    current_time = datetime.datetime.now()
    data = [[str(current_time),str(status)]]

    with open(r'logs.csv','a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return True