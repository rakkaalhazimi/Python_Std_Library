"""
SQL syntax supports calling functions during queries, either in the column list or in the
where clause of the select statement. This feature makes it possible to process data before
returning it from the query. It can be used to convert between different formats, perform
calculations that would be clumsy in pure SQL, and reuse application code.
"""

import codecs
import sqlite3

db_filename = '../todo.db'

def encrypt(s):
    print("Encrypting {!r}".format(s))
    return codecs.encode(s, "rot-13")

def decrypt(s):
    print("Decrypting {!r}".format(s))
    return codecs.encode(s, "rot-13")

with sqlite3.connect(db_filename) as conn:

    conn.create_function("encrypt", 1, encrypt)
    conn.create_function("decrypt", 1, decrypt)
    cursor = conn.cursor()

    # Raw values
    print("Original values:")
    query = "select id, details from task"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

    print("\nEncrypting...")
    query = "update task set details = encrypt(details)"
    cursor.execute(query)

    print("\nRaw encrypted values:")
    query = "select id, details from task"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

    print('\nDecrypting in query...')
    query = "select id, decrypt(details) from task"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

    print("\nDecrypting...")
    query = "update task set details = decrypt(details)"
    cursor.execute(query)


"""
Functions are exposed using the create_function() method of the Connection. The
parameters are the name of the function (as it should be used from within SQL), the
number of arguments that the function takes, and the Python function to expose.
"""