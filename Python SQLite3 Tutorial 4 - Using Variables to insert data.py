import sqlite3

dbase = sqlite3.connect('Our_data.db') # Open a database File
print 'Database opened'

dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL) ''')

print 'Table created'

def insert_record(ID,NAME,DIVISION,STARS):
    dbase.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
            VALUES(?,?,?,?)''',(ID,NAME,DIVISION,STARS))

    dbase.commit()
    print 'REcord inserted'
    
insert_record(6,'Bob','Hardware',4)

dbase.close()
print ' Database Closed'
