import sqlite3

dbase = sqlite3.connect('Our_data.db') # Open a database File
print 'Database opened'


dbase.close()
print ' Database Closed'
