#!/usr/bin/python3
"""
Filter states
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
        if str(i[1]).startswith("N"):
            print(i)
    c.close()
    server.close()
