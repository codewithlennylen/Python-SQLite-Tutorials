import sqlite3

dbase = sqlite3.connect('Our_data.db') # Open a database File
cursor = dbase.cursor()
print 'Database opened'
print 'Cursor crwated'

dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL) ''')

print 'Table created'

def read_Data():
    # from math import *
    data = cursor.execute(''' SELECT * FROM employee_records ORDER BY NAME''')
    for record in data:
        print 'ID : '+str(record[0])
        print 'NAME : '+str(record[1])
        print 'DIVISION : '+str(record[2])
        print 'STARS : '+str(record[3])+'\n'


##read_Data()

def check_Data():
    # from math import *
    data = cursor.execute(''' SELECT NAME FROM employee_records WHERE ID =2''')
    x = data.fetchall()
    if x == []:
        print 'Doesnt exist'
    else:
        print (x)

##    for record in data:
##        print 'NAME : '+str(record[0])
####        print 'NAME : '+str(record[1])
####        print 'DIVISION : '+str(record[2])
####        print 'STARS : '+str(record[3])+'\n'


check_Data()


def update_record():
    dbase.execute(''' UPDATE employee_records set STARS=3 WHERE ID=2 ''')
    dbase.commit()
    print 'Updated'


dbase.close()
print ' Database Closed'
