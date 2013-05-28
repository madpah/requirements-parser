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
    >>> with open('requirements.txt', 'rb') as f:
    ...     pprint.pprint(requirements.parse(f)))
    [{'extras': None, 'name': 'requests', 'operator': '>=', 'version': '0.14.1'},
     {'extras': None, 'name': 'requests-oath2', 'operator': None, 'version': None},
     {'extras': None, 'name': 'Django', 'operator': '==', 'version': '1.4.2'}]

