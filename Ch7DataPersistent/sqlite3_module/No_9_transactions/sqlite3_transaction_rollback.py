"""
Uncommitted changes can also be discarded entirely using rollback(). The commit() and
rollback() methods are usually called from different parts of the same try:except block,
with errors triggering a rollback.
"""

import sqlite3
db_filename = '../todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print(' ', name)

with sqlite3.connect(db_filename) as conn:
    print('Before changes:')
    show_projects(conn)
    try:
        # Insert
        cursor = conn.cursor()
        cursor.execute("""delete from project
        where name = 'virtualenvwrapper'
        """)

        # Show the settings.
        print('\nAfter delete:')
        show_projects(conn)

        # Pretend the processing caused an error.
        raise RuntimeError('simulated error')

    except Exception as err:
        # Discard the changes.
        print('ERROR:', err)
        conn.rollback()

    else:
        # Save the changes.
        conn.commit()

    # Show the results.
    print('\nAfter rollback:')
    show_projects(conn)

"""
After calling rollback(), the changes to the database are no longer present.
"""