.. # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at
   #
   #     http://www.apache.org/licenses/LICENSE-2.0
   #
   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.
   #
   # SPDX-License-Identifier: Apache-2.0

Welcome to Requirements Parser's documentation!
===============================================

Requirements parser is a Python module for parsing Pip_ requirement files.

.. _Pip: http://www.pip-installer.org

Requirements parser is (now) `Apache 2.0`_ licensed.

.. _Apache 2.0: https://www.apache.org/licenses/LICENSE-2.0

Quickstart:

.. code-block:: python

    import requirements

    reqfile = """
    Django>=1.5,<1.6
    DocParser[PDF]==1.0.0
    """

    for req in requirements.parse(reqfile):
        print(req.name, req.specs, req.extras)

Will output:

::

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

