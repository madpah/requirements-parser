import re
import warnings
from pkg_resources import Requirement


# Compiled regular expressions

uri_regex = re.compile(r'^(svn|git|bzr|hg|http|https|file|ftp):(\.+)')
file_uri_regex = re.compile(
    r'^(?P<path>[^#]+)#egg=(?P<name>[^&]+)$', re.MULTILINE)
editable_uri_regex = re.compile(r'^((?P<vcs>svn|git|bzr|hg)\+)?'
                                '(?P<uri>[^#&]+)#egg=(?P<name>[^&]+)$',
                                re.MULTILINE)
vcs_uri_regex = re.compile(r'^(?P<vcs>svn|git|bzr|hg)\+'
                           '(?P<uri>[^#&]+)#egg=(?P<name>[^&]+)$',
                           re.MULTILINE)

# Pip's pip/download.py:is_url() function doesn't check THAT closely


def is_uri(uri):
    uri = uri.lower()
    match = re.match(uri_regex, uri)
    return match is not None


def is_vcs_uri(uri):
    uri = uri.lower()
    match = re.match(vcs_uri_regex, uri)
    return match is not None


# See pip/req.py:parse_requirements()
def parse(reqstr):
    try:
        # Python 2.x compatibility
        if not isinstance(reqstr, basestring):
            reqstr = reqstr.read()
    except NameError:
        # Python 3.x only
        if not isinstance(reqstr, str):
            reqstr = reqstr.read()

    for line in reqstr.splitlines():
        line = line.strip()
        if line == '':
            continue
        elif not line or line.startswith('#'):
            # comments are lines that start with # only
            continue
        elif line.startswith('-r') or line.startswith('--requirement'):
            warnings.warn('Recursive requirements not supported. Skipping.')
            continue
        elif line.startswith('-f') or line.startswith('--find-links') or \
                line.startswith('-i') or line.startswith('--index-url') or \
                line.startswith('--extra-index-url') or \
                line.startswith('--no-index'):
            warnings.warn('Private repos not supported. Skipping.')
            continue
        elif line.startswith('-Z') or line.startswith('--always-unzip'):
            warnings.warn('Unused option --always-unzip. Skipping.')
            continue
        elif line.startswith('file:'):
            match = re.match(file_uri_regex, line)
        elif line.startswith('-e') or line.startswith('--editable') or \
                is_uri(line) or is_vcs_uri(line):
            if line.startswith('-e'):
                tmpstr = line[len('-e'):].strip()
            elif line.startswith('--editable'):
                tmpstr = line[len('--editable'):].strip()
            else:
                tmpstr = line
            match = re.match(editable_uri_regex, tmpstr)
        else:
            try:
                # Handles inline comments despite not being strictly legal
                req = Requirement.parse(line)
                yield {
                    'name': req.project_name,
                    'extras': list(req.extras),
                    'specs': req.specs,
                }
                continue
            except ValueError:
                match = None

        if match:
            yield match.groupdict()
        else:
            raise ValueError('Invalid requirement line "%s"' % line)
