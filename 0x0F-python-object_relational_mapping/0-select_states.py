#!/usr/bin/python3
# script that will list all states from databases
""" 0-select_states list all states from database
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password,
                         db=database)
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER by id ASC')

    rows = cur.fetchall()
    for row in rows:
        print (row)
