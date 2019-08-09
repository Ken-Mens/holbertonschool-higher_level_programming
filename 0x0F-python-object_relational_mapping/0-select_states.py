#!/usr/bin/python3
# 0-select_states.py: lists all states from database hbtn_0e_0_usa

if __name__ == "__main__":

import MySQLdb
def a_function(username, password, database)

db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
cur = db.cursor()

cursor.execute('SELECT * FROM states ORDER by ASC')

for row in cursor.fetchall():
print (row)
