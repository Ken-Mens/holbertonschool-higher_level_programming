#!/usr/bin/python3
# 4-cities_by_state.py: lists all cities from database hbtn_0e_4_usa

if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    ask = "SELECT cities.id, cities.name, states.name FROM \
            cities JOIN states on cities.state_id = states.id"

    cursor.execute(ask)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
