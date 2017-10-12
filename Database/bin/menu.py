#Adam Baker
#12.10.17
#Menu Code

import time
def menus():
    menu = input('Would you like to [(1) Add Data] [(2) View Data] [(3) Shutdown] ')
    if menu == ('1'):
        import CSVHandler.py
    elif menu == ('2'):
        import viewer.py
    elif menu == ('3'):
        print('Shutting Down')
        time.sleep(0.5)
    else:
        print('[(1) Add Data] [(2) View Data] [(3) Shutdown]')
        menus()
menus()
                
