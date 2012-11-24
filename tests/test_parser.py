import unittest
from reqfileparser import parse

class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parse(''), [])
    
