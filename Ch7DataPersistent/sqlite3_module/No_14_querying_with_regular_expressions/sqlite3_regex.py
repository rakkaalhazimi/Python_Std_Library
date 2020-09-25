"""
SQLite supports several special user functions that are associated with SQL syntax. For
example, the function regexp can be used in a query to check whether a column’s string
value matches a regular expression using the following syntax.

SELECT * FROM table
WHERE column REGEXP '.*pattern.*'
"""

import re
import sqlite3

db_filename = '../todo.db'

def regexp(pattern, input):
    return bool(re.match(pattern, input))

with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.create_function('regexp', 2, regexp)
    cursor = conn.cursor()

    pattern = '.*[wW]rite [aA]bout.*'

    cursor.execute(
        """
        select id, priority, details, status, deadline from task
        where details regexp :pattern
        order by deadline, priority
        """,
        {'pattern': pattern},
    )

for row in cursor.fetchall():
    task_id, priority, details, status, deadline = row
    print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
    task_id, priority, details, status, deadline))