"""
Changes to the database, made through either insert or update statements, need to be saved
by explicitly calling commit(). This requirement gives an application an opportunity to make
several related changes together, so they are stored atomically instead of incrementally.
Such an approach avoids the situation where partial updates are seen by different clients
connecting to the database simultaneously.

The effect of calling commit() can be seen with a program that uses several connections
to the database. A new row is inserted with the first connection, and then two attempts are
made to read it back using separate connections.
"""

import sqlite3
db_filename = '../todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print(' ', name)

with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    show_projects(conn1)

    # Insert in one cursor.
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into project (name, description, deadline)
    values ('virtualenvwrapper', 'Virtualenv Extensions',
    '2011-01-01')
    """)

    print('\nAfter changes in conn1:')
    show_projects(conn1)

    # Select from another connection, without committing first.
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        show_projects(conn2)

    # Commit, then select from another connection.
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        show_projects(conn3

"""
When show_projects() is called before conn1 has been committed, the results depend
on which connection is used. Since the change was made through conn1, this connection
sees the altered data. Conversely, conn2 does not. After committing, the new connection
conn3 sees the inserted row.
"""