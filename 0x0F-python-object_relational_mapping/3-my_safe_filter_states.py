#!/usr/bin/python3
# 3-my_safe_filter_states.py: script that safe from SQL Injection...

if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    statename = argv[4]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cur = db.cursor()
    ask = "SELECT * FROM states WHERE name=%s"

    cur.execute(ask, (statename,))

    rows = cur.fetchall()
    for row in rows:
        print (row)
