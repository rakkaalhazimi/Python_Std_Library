"""
Use named parameters for more complex queries with a lot of parameters, or where some
parameters are repeated multiple times within the query. Named parameters are prefixed
with a colon (e.g., :param_name).
"""

import sqlite3
import sys

db_filename = "../todo.db"
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = :project_name
    order by deadline, priority
    """

    cursor.execute(query, {"project_name": project_name})

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

"""
Neither positional nor named parameters need to be quoted or escaped, since they are
given special treatment by the query parser.
"""