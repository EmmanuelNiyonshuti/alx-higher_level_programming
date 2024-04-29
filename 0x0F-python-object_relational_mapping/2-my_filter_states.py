#!/usr/bin/python3
"""
This script takes in an argument and displays all values
in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'

    """connect to the db"""
    conn = MySQLdb.connect(host, user, passwd, db)
    """create a cursor and use it to execute sql queries
    and fetch the rows from the table"""
    curr = conn.cursor()
    state_name = sys.argv[4]
    """sql injection vulnerable query"""
    curr.execute("""SELECT * FROM states
                 WHERE BINARY name = '{}' ORDER BY states.id ASC
                 """.format(state_name))
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    conn.close()
