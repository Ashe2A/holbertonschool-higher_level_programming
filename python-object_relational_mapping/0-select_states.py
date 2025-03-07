#!/usr/bin/python3
"""
Get all states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id;")
    print(i for i in cursor.fetchall())
    cursor.close()
    db.close()
