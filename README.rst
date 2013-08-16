Requirements Parser
===================


.. image:: https://secure.travis-ci.org/davidfischer/requirements-parser.png?branch=master
    :target: https://travis-ci.org/davidfischer/requirements-parser
.. image:: https://coveralls.io/repos/davidfischer/requirements-parser/badge.png
    :target: https://coveralls.io/r/davidfischer/requirements-parser

This is a small Python module for parsing Pip_ requirement files.

.. _Pip: http://www.pip-installer.org/


Installation
============

::

    pip install requirements-parser


Examples
========

Requirements parser can parse a file-like object or a text string.

::

    >>> import requirements
    >>> reqfile = """
    ...     Django>=1.5,<1.6
    ...     DocParser[PDF]==1.0.0
    ...     """
    >>> for req in requirements.parse(reqfile):
    ...     print(req.name, req.specs, req.extras)
    ...
    ('Django', [('>=', '1.5'), ('<', '1.6')], [])
    ('DocParser', [('==', '1.0.0')], ['pdf'])
