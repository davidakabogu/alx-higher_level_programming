#!/usr/bin/python3
"""Fetches and displays states from the hbtn_0e_0_usa database."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db_params = {
            "host": "localhost",
            "user": sys.argv[1],
            "passwd": sys.argv[2],
            "db": sys.argv[3],
            "port": 3306
            }

    db_connection = MySQLdb.connect(**db_params)
    cursor = db_connection.cursor()

    # Retrieve states starting with 'N' in their name
    query = """SELECT * FROM states
            WHERE name LIKE BINARY 'N%' ORDER BY states.id"""
    cursor.execute(query)

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db_connection.close()
