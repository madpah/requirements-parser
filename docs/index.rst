Welcome to Requirements Parser's documentation!
===============================================


Requirements parser is a Python module for parsing Pip_ requirement files.


.. _Pip: http://www.pip-installer.org


Requirements parser is (now) `Apache 2.0`_ licensed.

.. _Apache 2.0: https://www.apache.org/licenses/LICENSE-2.0


Quickstart:

::

    >>> import requirements
    >>> reqfile = """
    Django>=1.5,<1.6
    DocParser[PDF]==1.0.0
    """
    >>> for req in requirements.parse(reqfile):
    ...     print(req.name, req.specs, req.extras)
    ...
    Django [('>=', '1.5'), ('<', '1.6')] []
    DocParser [('==', '1.0.0')] ['pdf']


Contents:

.. toctree::
   :maxdepth: 2

   usage
   changelog
   lowlevel



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

