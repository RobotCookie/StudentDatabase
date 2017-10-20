#Adam Baker
#12.10.17
#Data Viewer Code

import csv
import sys


uid = input('Enter Unique ID to find\n')
csv_file = csv.reader(open('database.csv', "r"), delimiter=",")
for row in csv_file:
    email = row[8]
    address = row[4]
    phone = row[5]
    fname = row[0]
    sname = row[1]
    gender = row[6]
    house = row[7]
    if uid == row[2]:
        print('[email][contact][info]')
        report = input('What would you like to view? ')
        if report == ('email'):
            print (email)
        elif report == ('contact'):
            print (email,address,phone)
        elif report == ('info'):
            print (fname,sname,gender,house)
import LogoutCode.py
        
    

