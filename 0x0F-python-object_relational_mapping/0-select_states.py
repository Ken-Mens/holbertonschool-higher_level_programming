#!/usr/bin/python3
# 0-select_states.py: lists all states from database hbtn_0e_0_usa
""" Write a script that lists all states from the database hbtn_0e_0_usa:
"""
if __name__ == "__main__":

    # get arguments
    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # connect to database
    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)
    # set our cursor
    cur = db.cursor()

    # execute the commmand
    cur.execute('SELECT * FROM states ORDER by id ASC')

    # print output
    rows = cur.fetchall()
    for row in rows:
        print (row)
