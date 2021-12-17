Changelog
=========

<!--next-version-placeholder-->

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