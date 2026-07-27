import os
import sqlite3

"""
SQL sublanguage: DDL (Data Definition Language)

Let's say we created the following table:
site_user table:
|    id    |     firstname     |
--------------------------------
|1         |'Kevin'            |
|2         |'Brian'            |
|3         |'Charles'          |

The site_user table when it was created, forgot to add the 'lastname' column.

The ALTER keyword allows us to add / remove columns and constraints on an existing table.
     - Adding a column:
         - ALTER TABLE table_name ADD column_name data_type [constraint];
     - Removing a column:
         - ALTER TABLE table_name DROP column_name;
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    In problem1.sql, write a SQL statement that adds a "lastname" column to the site_user table, of type
    varchar(100).

      site_user table:
      |    id    |     firstname     |
      --------------------------------
      |1         |'Kevin'            |
      |2         |'Brian'            |
      |3         |'Charles'          |

    Sets up the site_user table, runs the student's statement against it, and returns the open connection so
    the caller can verify the lastname column was added correctly.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE site_user (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname varchar(100));")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Kevin');")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Brian');")
    cur.execute("INSERT INTO site_user (firstname) VALUES ('Charles');")
    conn.commit()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
