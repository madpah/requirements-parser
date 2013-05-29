Requirements Parser
===================


.. image:: https://secure.travis-ci.org/davidfischer/requirements-parser.png?branch=master
    :target: https://travis-ci.org/davidfischer/requirements-parser

This is a small Python module for parsing Pip_ requirement files.

.. _Pip: http://www.pip-installer.org/


Examples
========

Requirements parser can parse a file-like object or a text string.

::

    >>> import requirements
    >>> import pprint
    >>> with open('requirements.txt', 'r') as f:
    ...     for req in requirements.parse(f):
    ...         pprint.pprint(req)
    ...
    {'name': 'requirements',
     'uri': 'git://github.com/davidfischer/requirements-parser.git',
     'vcs': 'git'}
    {'extras': [], 'name': 'Django', 'specs': [('>=', '1.5'), ('<', '1.6')]}
    {'extras': [], 'name': 'numpy', 'specs': []}
    {'extras': ['pdf'], 'name': 'DocParser', 'specs': []}

