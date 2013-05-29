import os.path
import unittest
import warnings

try:
    # Python 2.x compatibility
    from StringIO import StringIO
except ImportError:
    # Python 3.x only
    from io import StringIO

from requirements import parse

this_dir = os.path.dirname(__file__)

# useful for testing purposes
listparse = lambda x: list(parse(x))


class TestParser(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(listparse(''), [])
        self.assertEqual(listparse(StringIO('')), [])

    def test_comment(self):
        self.assertEqual(listparse('#comment>>1.2.'), [])

        # This gets handled even though it's against the spec
        out = listparse('req==1.0    # comment')
        self.assertEqual(out[0]['name'], 'req')
        self.assertEqual(out[0]['specs'], [('==', '1.0')])

    def test_invalid(self):
        # invalid operators
        self.assertRaises(ValueError, listparse, 'test>>1.2.0')
        self.assertRaises(ValueError, listparse, 'test=>1.2.0')

        # invalid editables
        self.assertRaises(ValueError, listparse, 'novcs+http://example.com#egg=a')
        self.assertRaises(ValueError, listparse, 'svn+http://example.com#egg')

    def test_editable(self):
        out = listparse('-e svn+svn://svn.myproject.org/svn/MyProject#egg=MyProject')
        self.assertEqual(out[0]['vcs'], 'svn')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'svn://svn.myproject.org/svn/MyProject')

        out = listparse('--editable git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject')
        self.assertEqual(out[0]['vcs'], None)
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709')

        out = listparse('--editable hg+http://hg.myproject.org/MyProject/@special_feature#egg=MyProject')
        self.assertEqual(out[0]['vcs'], 'hg')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'http://hg.myproject.org/MyProject/@special_feature')

        out = listparse('-e bzr+lp:MyProject#egg=MyProject')
        self.assertEqual(out[0]['vcs'], 'bzr')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['uri'], 'lp:MyProject')

    def test_file(self):
        out = listparse('file:///path/to/your/lib/project#egg=MyProject')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['path'], 'file:///path/to/your/lib/project')

        out = listparse('file:../../lib/project#egg=MyProject')
        self.assertEqual(out[0]['name'], 'MyProject')
        self.assertEqual(out[0]['path'], 'file:../../lib/project')

    def test_normal(self):
        out = listparse('MyPackage')
        self.assertEqual(out[0]['name'], 'MyPackage')

        out = listparse('Framework==0.9.4')
        self.assertEqual(out[0]['name'], 'Framework')
        self.assertEqual(out[0]['specs'][0], ('==', '0.9.4'),)

        out = listparse('Library>=0.2')
        self.assertEqual(out[0]['name'], 'Library')
        self.assertEqual(out[0]['specs'][0], ('>=', '0.2'),)

    def test_extras(self):
        out = listparse('MyPackage[PDF]==3.0')
        self.assertEqual(out[0]['name'], 'MyPackage')
        self.assertEqual(out[0]['extras'], ['pdf'])
        self.assertEqual(out[0]['specs'][0], ('==', '3.0'),)

        out = listparse('Fizzy [foo, bar]')
        self.assertEqual(out[0]['name'], 'Fizzy')
        self.assertEqual(out[0]['extras'], ['foo', 'bar'])

    def test_specs(self):
        out = listparse('PickyThing<1.6,>1.9,!=1.9.6,<2.0a0,==2.4c1')
        self.assertEqual(out[0]['name'], 'PickyThing')
        self.assertEqual(len(out[0]['extras']), 0)
        self.assertEqual(len(out[0]['specs']), 5)
        self.assertEqual(out[0]['specs'], [
            ('<', '1.6'),
            ('>', '1.9'),
            ('!=', '1.9.6'),
            ('<', '2.0a0'),
            ('==', '2.4c1'),
        ])

    def test_names(self):
        # Checks '.' in names
        out = listparse('z3c.checkversions==0.4.1')
        self.assertEqual(out[0]['name'], 'z3c.checkversions')
        self.assertEqual(out[0]['specs'], [('==', '0.4.1')])

    def test_warnings(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            out = listparse('--requirement reqfile.txt')
            self.assertEqual(len(w), 1)
            self.assertEqual(out, [])

    def test_fullfile(self):
        with open(os.path.join(this_dir, 'reqfiles', 'rtfd_requirements.txt'), 'r') as f:
            out = listparse(f)
            self.assertEqual(len(out), 31)
            self.assertEqual(out[0]['name'], 'Distutils2')
            self.assertEqual(out[0]['specs'], [('==', '1.0a3')])
            self.assertEqual(out[1]['name'], 'Sphinx')
            self.assertEqual(out[1]['specs'], [('==', '1.1.2')])
            self.assertEqual(out[24]['name'], 'django_haystack')
            self.assertEqual(out[24]['vcs'], 'git')
            self.assertEqual(out[24]['uri'], 'git://github.com/toastdriven/django-haystack@259274e4127f723d76b893c87a82777f9490b960')

        with open(os.path.join(this_dir, 'reqfiles', 'rtfd_deploy_requirements.txt'), 'r') as f:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                out = listparse(f)
                self.assertEqual(len(out), 5)
                self.assertEqual(len(w), 1)  # warning for recursive reqs
                self.assertEqual(out[0]['name'], 'psycopg2')
                self.assertEqual(out[4]['name'], 'dnspython')

        with open(os.path.join(this_dir, 'reqfiles', 'crateio_requirements.txt'), 'r') as f:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                out = listparse(f)
                self.assertEqual(len(w), 1)  # warning for --extra-index-url
                self.assertEqual(out[0]['name'], 'Babel')
                self.assertEqual(out[0]['specs'], [('==', '0.9.6')])
