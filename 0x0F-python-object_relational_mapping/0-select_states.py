#!/usr/bin/python3
# script that will list all states from databases


if __name__ == "__main__":
    """ 0-select_states list all states from database
    """
    import MySQLdb
    from sys import argv

    # username = argv[1]
    # password = argv[2]
    # database = argv[3]

    ask = MySQLdb.connect(host='localhost', port=3306,
                          user=argv[1], passwd=argv[2],
                          db=argv[3])
    curse = ask.cursor()

    curse.execute('SELECT * FROM states ORDER by id ASC')

    rows = curse.fetchall()
    for row in rows:
        print (row)

    curse.close()
    ask.close()
