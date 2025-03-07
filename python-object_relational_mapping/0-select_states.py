#!/usr/bin/python3
"""
Get all states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    server = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    c = server.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id;")

    print(i for i in c.fetchall())
    c.close()
    server.close()
