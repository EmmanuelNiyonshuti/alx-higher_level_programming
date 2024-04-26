#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    my_dict = {
        'host': '127.0.0.1',
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3]
    }
    connect = MySQLdb.connect(**my_dict)
    cursor = connect.cursor()
    cursor.execute("""
                   SELECT cities.id, cities.name, states.name FROM cities
                   INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC
                   """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    connect.close()