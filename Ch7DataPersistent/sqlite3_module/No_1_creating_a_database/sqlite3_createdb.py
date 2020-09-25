"""
An SQLite database is stored as a single file on the file system. The library manages access
to the file, including locking it to prevent corruption when multiple writers use it. The
database is created the first time the file is accessed, but the application is responsible for
managing the table definitions, or schema, within the database.
"""

import os
import sqlite3

db_filename = "../todo.db"

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print("Need to create schema")
else:
    print("Database exists; assume schema does, too.")

conn.close()