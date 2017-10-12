#Adam Baker
#6.10.17
#Ultimate School Database

import pickle

f = open('settings.pckl', 'rb') #Tests if program is first time launch
obj = pickle.load(f)
f.close()

if obj == int(0):
    username = str(input('What Do You Want Your Username To Be? '))
    password = str(input('What Do You Want Your Password To Be? '))
    f = open('d#1.pckl', 'wb') #Saves Username
    pickle.dump(username, f)
    f.close()
    f = open('d#2.pckl', 'wb') #Saves Password
    pickle.dump(password, f)
    f.close()
    obj = obj+1
    f = open('settings.pckl', 'wb')#Sets First Time Launch To Complete
    pickle.dump(obj, f)
    f.close()
else:
        f = open('d#1.pckl', 'rb') #Loads Username
        user = pickle.load(f)
        f.close()
        f = open('d#2.pckl', 'rb') #Loads Password
        pw = pickle.load(f)
        f.close()
        u = str(input('Enter Username: '))
        if u == user:
            p = str(input('Enter Password: '))
            if p == pw:
                print ('Welcome To The Program')
                input()
        else:
            print('Incorrect')




