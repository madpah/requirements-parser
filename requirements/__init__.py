from .parser import parse

_MAJOR = 0
_MINOR = 0
_PATCH = 2

def version_tuple():
    '''
    Returns a 3-tuple of ints that represent the version
    '''
    return (_MAJOR, _MINOR, _PATCH)

def version():
    '''
    Returns a string representation of the version
    '''
    return '%d.%d.%d' %(version_tuple())


__version__ = version()

