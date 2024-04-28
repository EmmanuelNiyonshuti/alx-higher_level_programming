#!/usr/bin/python3

"""This script lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    """Get the arguments"""
    username = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    """connect to the db"""
    conn = MySQLdb.connect(host = 'localhost', port = 3306, user = username, passwd = passwd, db = db)
    """create a cursor and use it to execute sql queries"""
    cur = conn.cursor()
    cur.execute("""
                SELECT * FROM states WHERE SUBSTRING(name, 1, 1) = 'N'
                ORDER BY states.id ASC
                """)

    """fetch the rows and print the results"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    """close the connection"""
    cur.close()
    conn.close()