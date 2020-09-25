"""
To retrieve the values saved in the task table from within a Python program, create a
Cursor from a database connection. A cursor produces a consistent view of the data, and
is the primary means of interacting with a transactional database system like SQLite.
"""

import sqlite3

db_filename = "../todo.db"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pymotw'
    """)

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print("{:2d} [{:d}] {:<25} [{:<8}] ({})".format(
            task_id, priority, details, status, deadline))


"""
Querying is a two-step process. First, run the query with the cursor’s execute() method
to tell the database engine which data to collect. Then, use fetchall() to retrieve the
results. The return value is a sequence of tuples containing the values for the columns
included in the select clause of the query.
"""