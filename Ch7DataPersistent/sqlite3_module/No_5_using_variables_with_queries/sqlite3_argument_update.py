"""
Query parameters can be used with select, insert, and update statements. They can
appear in any part of the query where a literal value is legal.
"""

import sqlite3
import sys

db_filename = '../todo.db'
id = int(sys.argv[1])
status = sys.argv[2]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update task set status = :status where id = :id"
    cursor.execute(query, {'status': status, 'id': id})

"""
This update statement uses two named parameters. The id value is used to find the right
row to modify, and the status value is written to the table.
"""