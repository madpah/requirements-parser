Welcome to Requirements Parser's documentation!
===============================================


Requirements parser is a Python module for parsing Pip_ requirement files.


.. _Pip: http://www.pip-installer.org


Requirements parser is BSD_ licensed.

.. _BSD: http://opensource.org/licenses/BSD-2-Clause


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

   changelog
   lowlevel



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

