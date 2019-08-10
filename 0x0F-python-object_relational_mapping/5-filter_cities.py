#!/usr/bin/python3
# 5-filter_cities.py: takes in name of a state as an argument and list cities
""" filter cities by State
"""


if __name__ == "__main__":

    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]
    statename = argv[4]

    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    ask = "SELECT cities.name FROM \
        cities JOIN states ON cities.state_id = states.id WHERE \
        states.name=%s"

    cursor.execute(ask, (statename,))

    prod = []
    rows = cursor.fetchall()
    for cities in rows:
        prod.append(cities[0])
    prod = ", ".join(prod)
    print(prod)
