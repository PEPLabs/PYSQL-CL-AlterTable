import unittest

from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_problem1(self):
        """
        We verify the lastname column was added correctly two ways:
        1. It must be queryable at all (if the ALTER statement is broken, this raises an exception).
        2. It must actually have a text/string type, not just any column with that name - e.g.
           "ADD lastname INTEGER" should NOT pass this test, even though it does create a column named
           "lastname".

           SQLite doesn't strictly enforce declared column types - it uses "type affinity" instead. Per
           SQLite's own rules (https://www.sqlite.org/datatype3.html#determination_of_column_affinity), a
           column gets TEXT affinity if its declared type contains "CHAR", "CLOB", or "TEXT" - so
           varchar(100), TEXT, and CHAR(50) are all valid text types, while INTEGER, INT, and REAL are not.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("select lastname from site_user;")
            cur.execute("PRAGMA table_info(site_user);")
            columns = {row[1]: row[2] for row in cur.fetchall()}
        except Exception as e:
            print(f"problem1: {e}\n")
            self.fail(str(e))
        finally:
            conn.close()

        self.assertIn("lastname", columns, "lastname column was not found")

        declared_type = (columns["lastname"] or "").upper()
        has_text_affinity = any(marker in declared_type for marker in ("CHAR", "CLOB", "TEXT"))
        self.assertTrue(
            has_text_affinity,
            f"lastname should be a text type (e.g. varchar(100)), "
            f"but it was declared as '{columns['lastname']}'",
        )


if __name__ == "__main__":
    unittest.main()
