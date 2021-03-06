#!/usr/bin/python3
""" script that filters states """


if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password,
                         db=database)
    cur = db.cursor()

    ask = "SELECT * FROM states WHERE\
                name LIKE BINARY 'N%' ORDER by id ASC"

    cur.execute(ask)

    rows = cur.fetchall()
    for row in rows:
        print(row)
