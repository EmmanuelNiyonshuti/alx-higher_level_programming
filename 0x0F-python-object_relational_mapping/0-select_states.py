#!/usr/bin/python3

"""This Script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    """Get the arguments"""
    username = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'

    """connect to the db"""
    conn = MySQLdb.connect(host, username, passwd, db)

    """create a cursor and use it to execute sql queries"""
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    """fetch all the rows and print the results"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """close the connection"""
    cur.close()
    conn.close()
