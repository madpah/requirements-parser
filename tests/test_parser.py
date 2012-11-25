import os.path
import unittest
import warnings
from StringIO import StringIO

from reqfileparser import parse

this_dir = os.path.dirname(__file__)

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

        out = parse('--editable git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject')
        self.assertEqual(out[0]['vcs'], None)
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709')

        out = parse('--editable hg+http://hg.myproject.org/MyProject/@special_feature#egg=MyProject')
        self.assertEqual(out[0]['vcs'], 'hg')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'http://hg.myproject.org/MyProject/@special_feature')

        out = parse('-e bzr+lp:MyProject#egg=MyProject')
        self.assertEqual(out[0]['vcs'], 'bzr')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'lp:MyProject')

    def test_file(self):
        out = parse('file:///path/to/your/lib/project#egg=MyProject')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['path'], 'file:///path/to/your/lib/project')

        out = parse('file:../../lib/project#egg=MyProject')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['path'], 'file:../../lib/project')

    def test_normal(self):
        out = parse('MyPackage')
        self.assertEqual(out[0]['name'], 'MyPackage')

        out = parse('Framework==0.9.4')
        self.assertEqual(out[0]['name'], 'Framework')
        self.assertEqual(out[0]['operator'], '==')
        self.assertEqual(out[0]['version'], '0.9.4')

        out = parse('Library>=0.2')
        self.assertEqual(out[0]['name'], 'Library')
        self.assertEqual(out[0]['operator'], '>=')
        self.assertEqual(out[0]['version'], '0.2')

    def test_extras(self):
        out = parse('MyPackage[PDF]==3.0')
        self.assertEqual(out[0]['name'], 'MyPackage')
        self.assertEqual(out[0]['extras'], 'PDF')
        self.assertEqual(out[0]['operator'], '==')
        self.assertEqual(out[0]['version'], '3.0')

    def test_warnings(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            out = parse('--requirement reqfile.txt')
            self.assertEqual(len(w), 1)
            self.assertEqual(out, [])

    def test_fullfile(self):
        with open(os.path.join(this_dir, 'reqfiles', 'rtfd_requirements.txt'), 'rb') as f:
            out = parse(f)
            self.assertEqual(len(out), 31)
            self.assertEqual(out[0]['name'], 'Distutils2')
            self.assertEqual(out[0]['operator'], '==')
            self.assertEqual(out[0]['version'], '1.0a3')
            self.assertEqual(out[1]['name'], 'Sphinx')
            self.assertEqual(out[1]['operator'], '==')
            self.assertEqual(out[1]['version'], '1.1.2')
            self.assertEqual(out[24]['name'], 'django_haystack')
            self.assertEqual(out[24]['vcs'], 'git')
            self.assertEqual(out[24]['uri'], 'git://github.com/toastdriven/django-haystack@259274e4127f723d76b893c87a82777f9490b960')

        with open(os.path.join(this_dir, 'reqfiles', 'rtfd_deploy_requirements.txt'), 'rb') as f:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                out = parse(f)
                self.assertEqual(len(out), 5)
                self.assertEqual(len(w), 1)  # warning for recursive reqs
                self.assertEqual(out[0]['name'], 'psycopg2')
                self.assertEqual(out[4]['name'], 'dnspython')

        with open(os.path.join(this_dir, 'reqfiles', 'crateio_requirements.txt'), 'rb') as f:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                out = parse(f)
                self.assertEqual(len(w), 1)  # warning for --extra-index-url
                self.assertEqual(out[0]['name'], 'Babel')
                self.assertEqual(out[0]['operator'], '==')
                self.assertEqual(out[0]['version'], '0.9.6')
                
