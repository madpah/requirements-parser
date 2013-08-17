Usage
=====

Requirements parser works very similarly to the way pip actually parses
requirement files except that pip typically proceeds to install the
relevant packages.

Requirements come in a variety of forms such as requirement specifiers
(such as requirements>=0.0.5), version control URIs, other URIs and local
file paths.


Parsing requirement specifiers
------------------------------

::

    import requirements
    req = "django>=1.5,<1.6"
    parsed = list(requirements.parse(req))[0]
    parsed.name       # django
    parsed.specs      # [('>=', '1.5'), ('<', '1.6')]
    parsed.specifier  # True


Parsing version control requirements
------------------------------------

::

    req = "-e git+git://github.com/toastdriven/django-haystack@259274e4127f723d76b893c87a82777f9490b960#egg=django_haystack"
    parsed = list(requirements.parse(req))[0]
    parsed.name      # django_haystack
    parsed.vcs       # git
    parsed.revision  # 259274e4127f723d76b893c87a82777f9490b960
    parsed.uri       # git+git://github.com/toastdriven/django-haystack
    parsed.editable  # True (because of the -e option)


Parsing local files
-------------------

::

    req = "-e path/to/project"
    parsed = list(requirements.parse(req))[0]
    parsed.local_file    # True
    parsed.path          # path/to/project
