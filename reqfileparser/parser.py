import re
import warnings

# See pip/req.py:parse_requirements()
def parse(reqstr):
    requirements = []

    if not isinstance(reqstr, basestring):
        reqstr = reqstr.read()

    for line in reqstr.splitlines():
        line = line.strip()
        if len(line[:1]) == 0:
            continue
        elif not line or line.startswith('#'):
            continue
        elif line.startswith('-r') or line.startswith('--requirement'):
            warnings.warn('Recursive requirements are not supported. Skipping.')
            continue
        elif line.startswith('-f') or line.startswith('--find-links') or \
             line.startswith('-i') or line.startswith('--index-url') or \
             line.startswith('--extra-index-url') or \
             line.startswith('--no-index'):
            warnings.warn('Private repos are not supported. Skipping.')
            continue
        elif line.startswith('-Z') or line.startswith('--always-unzip'):
            warnings.warn('Unused option --always-unzip. Skipping.')
            continue
        elif line.startswith('-e') or line.startswith('--editable'):
            if line.startswith('-e'):
                tmpstr = line[len('-e'):].strip()
            else:
                tmpstr = line[len('--editable'):].strip()
            match = re.match(
                r'^((?P<vcs>svn|git|bzr|hg)\+)?'
                '(?P<uri>[^#&]+)'
                '#egg=(?P<name>[^&]+)$', tmpstr, re.MULTILINE)
        elif line.startswith('file:'):
            match = re.match(
                r'^(?P<path>[^#]+)'
                '#egg=(?P<name>[^&]+)$', line, re.MULTILINE)
        else:
            match = re.match(
                r'^(?P<name>[A-Za-z0-9\-_]+)'
                '(\[(?P<extras>[A-Za-z0-9\-\_]+)\])?'
                '(?P<operator>==|>=|>|<=|<=)?'
                '(?P<version>[A-Za-z0-9\.]+)?$', line, re.MULTILINE)
        
        if match:
            requirements.append(match.groupdict())
        else:
            raise ValueError('Invalid requirement line "%s"' %line)

    return requirements

