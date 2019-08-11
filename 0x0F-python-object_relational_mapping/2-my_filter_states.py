#!/usr/bin/python3
# 2-my_filter_states.py: filter states by user input

if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    ask = """SELECT id, name
            FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC"""

    cur = db.cursor()

    cur.execute(ask.format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
