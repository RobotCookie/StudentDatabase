#Adam Baker
#5.10.17
#Launch Code
import time
print('Welcome To ARK OS v8.0.9 C++ Edition')
time.sleep(0.5)
print('------------------------------------------------------------------------')
time.sleep(1)
print('Writing base.pak for safe launch')
f= open("base.pak","w+")
time.sleep(0.2)
user = input('Enter A Logname ')
text =('Access User:',user,'Launch C++ Edition')
text = str(text)
f.write(text)
time.sleep(0.5)
print('base.pak created')
time.sleep(0.4)
print('Ready For Safe Launch')
time.sleep(0.5)
print('Welcome',user)
time.sleep(0.5)
print('Launching Program')
time.sleep(0.2)
print('-------------------------------------------------------')
import teacher.py


