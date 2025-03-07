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
        server=argv[3]
    )
    c = server.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id;")
    for i in c.fetchall():
        print(i)
    c.close()
    server.close()
