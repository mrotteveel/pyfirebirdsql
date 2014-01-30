import firebirdsql
import unittest
import tempfile

# backwards compatibility:
if not hasattr(unittest, "skip"):
    def _empty(func):
        pass
    def _skip(message):
        return _empty
    unittest.skip = _skip

class TestBase(unittest.TestCase):
    host='localhost'
    port=3050
    user='sysdba'
    password='masterkey'
    page_size=2<<13

    def setUp(self):
        self.database=tempfile.mktemp()
        self.connection = firebirdsql.create_database(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
                page_size=self.page_size)

    def tearDown(self):
        self.connection.close()
