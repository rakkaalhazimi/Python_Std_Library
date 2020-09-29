import sqlite3

db_filename = "todo.db"

query = """delete from project where name == 'virtualenvwrapper'"""

with sqlite3.connect(db_filename) as conn:
    conn.execute(query)
