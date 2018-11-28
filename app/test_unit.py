import os

import unittest

import server
import tempfile

class serverTestCase(unittest.TestCase):

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def tearDown(self):
        pass

    def test_first_page(self):
        rv = self.app.get('/')
        assert b'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()
