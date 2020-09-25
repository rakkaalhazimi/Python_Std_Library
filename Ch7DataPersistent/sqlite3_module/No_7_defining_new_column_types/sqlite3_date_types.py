"""
Although SQLite supports only a few data types internally, sqlite3 includes facilities
for defining custom types to allow a Python application to store any type of data in a
column. Conversion for types beyond those supported by default is enabled in the database
connection using the detect_types flag. Use PARSE_DECLTYPES if the column was declared
using the desired type when the table was defined.
"""

import sqlite3
import sys

db_filename = '../todo.db'

sql = "select id, details, deadline from task"

def show_deadline(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    for col in ['id', 'details', 'deadline']:
        print(' {:<8} {!r:<26} {}'.format(
            col, row[col], type(row[col])))
    return

print('Without type detection:')
with sqlite3.connect(db_filename) as conn:
    show_deadline(conn)
    print('\nWith type detection:')
    with sqlite3.connect(db_filename,
                         detect_types=sqlite3.PARSE_DECLTYPES, # the type is str without it
                         ) as conn:
        show_deadline(conn)

"""
sqlite3 provides converters for date and timestamp columns, using the classes date
and datetime, respectively, from the datetime (page 221) module to represent the values
in Python. Both date-related converters are enabled automatically when type detection is
turned on.
"""