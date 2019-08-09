#!/usr/bin/python3
# 0-select_states.py: lists all states from database hbtn_0e_0_usa

if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER by id ASC')

    rows = cur.fetchall()
    for row in rows:
        print (row)
