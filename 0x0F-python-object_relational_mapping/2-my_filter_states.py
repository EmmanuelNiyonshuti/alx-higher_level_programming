#!/usr/bin/node
"""
This script takes in an argument and displays all values
in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    """get the arguments"""
    my_dict = {
        'host': '127.0.0.1',
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3]
    }
    """connect to the db"""
    conn = MySQLdb.connect(**my_dict)
    """create a cursor and use it to execute sql queries
    and fetch the rows from the table"""
    curr = conn.cursor()

    state_name = sys.argv[4]
    """sql injection vulnerable"""
    curr.execute(f"SELECT * FROM states WHERE name = '{state_name}' ORDER BY states.id ASC")
    rows = curr.fetchall()
    for row in rows:
        print(row)

    curr.close()
    conn.close()
