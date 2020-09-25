"""
An aggregation function collects many pieces of individual data and summarizes it in some
way. Examples of built-in aggregation functions include avg() (average), min(), max(), and
count().

The API for aggregators used by sqlite3 is defined in terms of a class with two methods.
The step() method is called once for each data value as the query is processed. The
finalize() method is called one time at the end of the query and should return the aggregate
value. This example implements an aggregator for the arithmetic mode. It returns the
value that appears most frequently in the input.
"""

import sqlite3
import collections

db_filename = '../todo.db'

class Mode:
    def __init__(self):
        self.counter = collections.Counter()

    def step(self, value):
        print('step({!r})'.format(value))
        self.counter[value] += 1

    def finalize(self):
        result, count = self.counter.most_common(1)[0]
        print('finalize() -> {!r} ({} times)'.format(
        result, count))
        return result

with sqlite3.connect(db_filename) as conn:
    conn.create_aggregate('mode', 1, Mode)

    cursor = conn.cursor()
    cursor.execute("""
    select mode(deadline) from task where project = 'pymotw'
    """)
    row = cursor.fetchone()
    print('mode(deadline) is:', row[0])