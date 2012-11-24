Reqfile Parser
==============

This is a small Python module for parsing Pip_ requirement files.

.. _Pip: http://www.pip-installer.org/

Examples
========

Reqfile Parser can parse a file-like object or a text string.

::

    >>> import reqfileparser
    >>> import pprint
    >>> with open('requirements.txt', 'rb') as f:
    ...     pprint.pprint(reqfileparser.parse(f)))
    [
        ('requests', '>=', '0.14.1'),
        ('requests-oath2', None, None),
        ('Django', '==', '1.4.2'),
    ]

