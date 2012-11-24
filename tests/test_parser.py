import unittest
from StringIO import StringIO

from reqfileparser import parse

class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parse(''), [])
        self.assertEqual(parse(StringIO('')), [])

    def test_comment(self):
        self.assertEqual(parse('#comment>>1.2.'), [])

    def test_invalid(self):
        # invalid operators
        self.assertRaises(ValueError, parse, 'test>>1.2.0')
        self.assertRaises(ValueError, parse, 'test=>1.2.0')

        # invalid editables
        self.assertRaises(ValueError, parse, 'novcs+http://example.com#egg=a')
        self.assertRaises(ValueError, parse, 'svn+http://example.com#egg')
    
    def test_editable(self):
        out = parse('-e svn+svn://svn.myproject.org/svn/MyProject#egg=MyProject')
        self.assertEqual(out[0]['vcs'], 'svn')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'svn://svn.myproject.org/svn/MyProject')

    def test_file(self):
        out = parse('file:///path/to/your/lib/project#egg=MyProject')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['path'], 'file:///path/to/your/lib/project')

    def test_normal(self):
        out = parse('MyPackage')
        self.assertEqual(out[0]['name'], 'MyPackage')

    def test_extras(self):
        out = parse('MyPackage[PDF]==3.0')
        self.assertEqual(out[0]['name'], 'MyPackage')
        self.assertEqual(out[0]['extras'], 'PDF')
        self.assertEqual(out[0]['operator'], '==')
        self.assertEqual(out[0]['version'], '3.0')
