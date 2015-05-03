Changelog
=========

**Version 0.1.0** (2 May 2015)

* Fix a bug involving parsing projects with underscores (`#17`_)
* Parse recursive requirements (`#19`_)

.. _#17: https://github.com/davidfischer/requirements-parser/pull/17
.. _#19: https://github.com/davidfischer/requirements-parser/pull/19


**Version 0.0.6** (16 August 2013)

* Fixed a packaging error in v0.0.5


**Version 0.0.5** (16 August 2013)

* **Backwards incompatible change** to refactor the parser.
* Parser now handles VCS specific revisions and parses out data such as
  whether the requirement is a local file or "editable".
* Improved handling of "editable" requirements
* Improved handling of non-VCS URI requirements
* Fixes: `#8`_, `#10`_ and `#12`_

.. _#8: https://github.com/davidfischer/requirements-parser/issues/8
.. _#10: https://github.com/davidfischer/requirements-parser/issues/10
.. _#12: https://github.com/davidfischer/requirements-parser/issues/12
