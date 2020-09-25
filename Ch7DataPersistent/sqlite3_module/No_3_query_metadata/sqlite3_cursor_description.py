"""
The DB-API 2.0 specification says that after execute() has been called, the Cursor should
set its description attribute to hold information about the data that will be returned by
the fetch methods. The API specification defines the description value as a sequence of
tuples containing the column name, type, display size, internal size, precision, scale, and a
flag that says whether null values are accepted.
"""

import sqlite3

db_filename = "../todo.db"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from task where project = 'pymotw'
    """)

    print("Task table has these columns:")
    for colinfo in cursor.description:
        print(colinfo)

"""
Because sqlite3 does not enforce type or size constraints on data inserted into a database,
only the column name value is filled in.
"""