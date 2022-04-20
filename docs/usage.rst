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

Usage
=====

Requirements parser works very similarly to the way pip actually parses requirement files except that pip typically
proceeds to install the relevant packages.

Requirements come in a variety of forms such as requirement specifiers (such as requirements>=0.0.5), version control
URIs, other URIs and local file paths.

Parsing requirement specifiers
------------------------------

.. code-block:: python

    import requirements
    req = "django>=1.5,<1.6"
    parsed = list(requirements.parse(req))[0]
    parsed.name       # django
    parsed.specs      # [('>=', '1.5'), ('<', '1.6')]
    parsed.specifier  # True

Parsing version control requirements
------------------------------------

.. code-block:: python

    req = "-e git+git://github.com/toastdriven/django-haystack@259274e4127f723d76b893c87a82777f9490b960#egg=django_haystack"
    parsed = list(requirements.parse(req))[0]
    parsed.name      # django_haystack
    parsed.vcs       # git
    parsed.revision  # 259274e4127f723d76b893c87a82777f9490b960
    parsed.uri       # git+git://github.com/toastdriven/django-haystack
    parsed.editable  # True (because of the -e option)


Parsing local files
-------------------

.. code-block:: python

    req = "-e path/to/project"
    parsed = list(requirements.parse(req))[0]
    parsed.local_file    # True
    parsed.path          # path/to/project
