try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name = 'requirements-parser',
    version = '0.0.3',
    description = 'Parses Pip requirement files',
    long_description = long_description,
    author = 'David Fischer',
    author_email = 'djfische@gmail.com',
    url = 'https://github.com/davidfischer/requirements-parser',
    license = 'BSD',
    platforms = ['OS Independent'],
    packages = ['requirements'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests',
)
