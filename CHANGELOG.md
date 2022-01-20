Changelog
=========

<!--next-version-placeholder-->

## v0.5.0 (2022-01-20)
### Feature
* Support all documented options in requirements files #62 ([#63](https://github.com/madpah/requirements-parser/issues/63)) ([`f92c0c0`](https://github.com/madpah/requirements-parser/commit/f92c0c079bce03b1860c78852d2c8c48cf32d539))

## v0.4.0 (2022-01-18)
### Feature
* Library is now typed according to PEP561 ([`0e1bb6a`](https://github.com/madpah/requirements-parser/commit/0e1bb6a746857a59c50530155d24da487a40c4be))

## v0.3.1 (2021-12-17)
### Fix
* Readthedocs config ([`ac1e7fb`](https://github.com/madpah/requirements-parser/commit/ac1e7fb616a2c15e83b8a5ca630ffd50aad4aedb))

## v0.3.0 (2021-12-17)
### Feature
* Added some typing ([`169ff6e`](https://github.com/madpah/requirements-parser/commit/169ff6e79657d8091e6e1a4e21c7da794d507832))
* Removed Python 2 code ([`82f9473`](https://github.com/madpah/requirements-parser/commit/82f94733f912e140fdcc0254020f4208d3e4a892))

### Fix
* Removed version from __init__ ([`4e83b9d`](https://github.com/madpah/requirements-parser/commit/4e83b9d3bdd5534da7adfdeb292ad2a1fae73ea8))

**Version 0.2.0** (11 Jan 2018)

This release dropped support for Python 3.2.

-   Support multiple hashing algorithms at the end of the URL
    ([\#24](https://github.com/davidfischer/requirements-parser/pull/24))
-   Preserve login info in requirement URI
    ([\#33](https://github.com/davidfischer/requirements-parser/pull/33))
-   Support subdirectory fragments
    ([\#32](https://github.com/davidfischer/requirements-parser/pull/32))
-   Support version control URLs with extras
    ([\#30](https://github.com/davidfischer/requirements-parser/pull/30))

**Version 0.1.0** (2 May 2015)

-   Fix a bug involving parsing projects with underscores
    ([\#17](https://github.com/davidfischer/requirements-parser/pull/17))
-   Parse recursive requirements
    ([\#19](https://github.com/davidfischer/requirements-parser/pull/19))

**Version 0.0.6** (16 August 2013)

-   Fixed a packaging error in v0.0.5

**Version 0.0.5** (16 August 2013)

-   **Backwards incompatible change** to refactor the parser.
-   Parser now handles VCS specific revisions and parses out data such
    as whether the requirement is a local file or \"editable\".
-   Improved handling of \"editable\" requirements
-   Improved handling of non-VCS URI requirements
-   Fixes:
    [\#8](https://github.com/davidfischer/requirements-parser/issues/8),
    [\#10](https://github.com/davidfischer/requirements-parser/issues/10)
    and
    [\#12](https://github.com/davidfischer/requirements-parser/issues/12)