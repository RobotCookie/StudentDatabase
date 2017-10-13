#Adam Baker
#12.10.17
#Student Database CSV Handler

fname = str(input('What is the students First Name? '))
sname = str(input('What is the students Last Name? '))
uid =(input('What is the students Unique ID: '))
dob = input('What is the students Date Of Birth? ')
haddress = str(input('What is the students Home Address? '))
hnumber =(input('What is the students Home Phone Number? '))
gender = str(input('What is the students gender? '))
tg = input('What is the students Tutor Group? ')
email = fname+'.'+sname+'@gpuacademy.co.uk'
writefile = open('database.csv','a')
writefile.write(fname+','+sname+','+uid+','+dob+','+haddress+','+hnumber+','+gender+','+tg+','+email+','+'\n')
writefile.close
import LogoutCode.py
