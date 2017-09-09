Requirements Parser
===================


.. image:: https://travis-ci.org/davidfischer/requirements-parser.svg?branch=master
    :target: https://travis-ci.org/davidfischer/requirements-parser
.. image:: https://coveralls.io/repos/github/davidfischer/requirements-parser/badge.svg?branch=master
    :target: https://coveralls.io/github/davidfischer/requirements-parser?branch=master
.. image:: http://readthedocs.org/projects/requirements-parser/badge/?version=latest
    :target: http://requirements-parser.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This is a small Python module for parsing Pip_ requirement files.

The goal is to parse everything in the `Pip requirement file format`_ spec.

.. _Pip: http://www.pip-installer.org/
.. _Pip requirement file format: https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format


Installation
============

::

    pip install requirements-parser


Examples
========

Requirements parser can parse a file-like object or a text string.

.. code-block:: python

    >>> import requirements
    >>> with open('requirements.txt', 'r') as fd:
    ...     for req in requirements.parse(fd):
    ...         print(req.name, req.specs)
    Django [('>=', '1.11'), ('<', '1.12')]
    six [('==', '1.10.0')]

It can handle most if not all of the options in requirement files that do
not involve traversing the local filesystem. These include:

* editables (`-e git+https://github.com/toastdriven/pyelasticsearch.git`)
* version control URIs
* egg hashes and subdirectories (`#egg=django-haystack&subdirectory=setup`)
* extras (`DocParser[PDF]`)
* URLs


Documentation
=============

For more details and examples, the documentation is available at:
http://requirements-parser.readthedocs.io.
