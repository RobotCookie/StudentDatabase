#Adam Baker
#12.10.17
#Data Viewer Code

print('Scanning Data')
file = open("database.csv","r")
for line in file:
    database = line.split(",")
    students = (database[0]+','+database[1]+','+database[2])
    print(students)
    input()
    
