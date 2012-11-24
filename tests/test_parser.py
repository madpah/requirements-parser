import unittest
from StringIO import StringIO

from reqfileparser import parse

class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parse(''), [])
        self.assertEqual(parse(StringIO('')), [])
    
