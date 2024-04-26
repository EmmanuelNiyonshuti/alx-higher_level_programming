#!/usr/bin/python3

"""
This scripts takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'

    connect = MySQLdb.connect(host, user, passwd, db)
    cursor = connect.cursor()

    state_name = sys.argv[4]

    cursor.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s ORDER BY cities.id ASC
                   """, (state_name, ))

    cities = cursor.fetchall()

    city_names = ', '.join(city[0] for city in cities)
    print(city_names)

    cursor.close()
    connect.close()
