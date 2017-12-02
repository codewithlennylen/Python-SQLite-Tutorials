import sqlite3

dbase = sqlite3.connect('Our_data.db') # Open a database File
print 'Database opened'

dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL) ''')

print 'Table created'


dbase.close()
print ' Database Closed'
