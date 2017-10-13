#Adam Baker
#2.10.17
#Log Out Code
import time

def log():
    logout = input('Would You Like To Log Out? ')
    if logout == ('yes'):
        print('Logging Out')
        time.sleep(1)
    elif logout == ('no'):
        import menu.py
    else:
        print('Please Enter [yes] Or [no]')
        log()
log()


