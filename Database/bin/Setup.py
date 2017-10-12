#Adam Baker
#6.10.17
#Setup For Database

import pickle
obj = int(0)
f = open('settings.pckl', 'wb')
pickle.dump(obj, f)
f.close()
