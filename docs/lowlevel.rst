Low level API
=============

Higher level parsing
--------------------

Typically this is called via:

::

     >>> import requirements
     >>> requirements.parse('django>=1.5')

.. automodule:: requirements.parser
    :members:


Lower level parsing
-------------------

Under the hood, the :class:`Requirement <requirements.requirement.Requirement>`
class does most of the heavy lifting.

.. automodule:: requirements.requirement
    :members:


Misc functions
--------------

.. automodule:: requirements
    :members:
