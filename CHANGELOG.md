# CHANGELOG



## v0.13.0 (2025-05-21)

### Chore

* chore(ci): update `actions/upload-artifact`

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`4ec20b6`](https://github.com/madpah/requirements-parser/commit/4ec20b69807bc9eba08f6a3115c57511c5ddf17a))

* chore(ci): update `actions/upload-artifact`

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`089094f`](https://github.com/madpah/requirements-parser/commit/089094f2abf1b48d74e3d0228f422574b41de4cc))

### Feature

* feat: Remove Python 3.14 support - not yet released

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`80d296e`](https://github.com/madpah/requirements-parser/commit/80d296e22a0ff30e0f17cb1feaf12ea2ea76d5e5))


## v0.12.0 (2025-05-21)

### Chore

* chore(deps): remove obsolete `types-setuptools` (#106)

Before https://github.com/madpah/requirements-parser/pull/105,
`pkg_resources` was implicitly present with `setuptools`, so it was
useful to have `types-setuptools` to check typing. But now that the
usage is gone, the typing dependency should not be needed. It probably
should have never been a direct dependency anyway, but only a dev
dependency, as AFAIK it was only useful locally to verify typing, not
when installing the library for consumers.

Signed-off-by: Mathieu Kniewallner &lt;mathieu.kniewallner@gmail.com&gt; ([`5937fb4`](https://github.com/madpah/requirements-parser/commit/5937fb4ebba1e83a9a79c1faf2b53e35e59f583d))

### Feature

* feat: Add Python 3.13 and 3.14 to the CI test matrix (#109)

Signed-off-by: Edgar Ramírez Mondragón &lt;edgarrm358@gmail.com&gt; ([`cf149b2`](https://github.com/madpah/requirements-parser/commit/cf149b281e9992b3d6b9508b4e79a4069e419f79))


## v0.11.0 (2024-08-12)

### Feature

* feat: replace deprecated `pkg_resources` with `packaging` (#105) - thanks to @oh2fih

Signed-off-by: Esa Jokinen &lt;esa@esajokinen.net&gt;

* Fix errors discovered with the unit tests

- Hashable type required. Convert list to tuple.
- Ignore incompatible types.
- Remove comments before passing the line to Req().
- Extras should be in lower case.
- Complete the list of comparison operators with &#39;!&#39;.

Signed-off-by: Esa Jokinen &lt;esa@esajokinen.net&gt;

---------

Signed-off-by: Esa Jokinen &lt;esa@esajokinen.net&gt; ([`19dddfa`](https://github.com/madpah/requirements-parser/commit/19dddfa2348b2cfaa6f0fb624851c8e36eee59ba))


## v0.10.2 (2024-07-26)

### Fix

* fix: support extras and more chars in names for VCS lines (#103) - thanks @theCapypara

Signed-off-by: Marco &#34;Capypara&#34; Köpcke &lt;hello@capypara.de&gt; ([`90e7f9e`](https://github.com/madpah/requirements-parser/commit/90e7f9ea1946716c67a2440278ee166448ecc039))


## v0.10.1 (2024-07-23)

### Fix

* fix: ValueError when parsing `-e .` (#99) thanks to @vergenzt

Signed-off-by: Tim Vergenz &lt;vergenzt@gmail.com&gt; ([`0e037a4`](https://github.com/madpah/requirements-parser/commit/0e037a45509d04318438900ace9e425f89f4b166))


## v0.10.0 (2024-07-23)

### Chore

* chore(ci): use non-latest macos runner ([`93b2a85`](https://github.com/madpah/requirements-parser/commit/93b2a8546f682e12ee132f193c7a6882227907bb))

* chore(doc): Updated README

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`6736727`](https://github.com/madpah/requirements-parser/commit/673672781d37b64b6f2450760ea46e377d91391b))

### Feature

* feat: added support for alias @ &lt;vcs_url&gt; syntax (#101) - thanks to @Glizzus

Signed-off-by: Cal Crosby &lt;calcruiseby@gmail.com&gt; ([`2927e00`](https://github.com/madpah/requirements-parser/commit/2927e0060d61fde37fa571610e19fbc2281068b5))


## v0.9.0 (2024-04-03)

### Feature

* feat: handle hashes without error (thanks to @dymart via #67) (#98)

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`a9aafc9`](https://github.com/madpah/requirements-parser/commit/a9aafc9a36caa77df6fad6c2dd9a076d72668c28))


## v0.8.0 (2024-04-03)

### Feature

* feat: Add support for Python 3.12 #93 via #94

feat: Drop support for Python 3.7 as part of #91

fix: Publish anciliary files only to sdist #66 via #87 (thanks to Maxwell G &lt;maxwell@gtmx.me&gt;)

fix: Type of `Requirement.specs` was incorrect #78

fix: `-e` in `requirements.txt` did not handle local paths correctly #97

chore(dev-deps): Updated all development dependencies

chore(deps): include types-setuptools as dependency

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`16ffe88`](https://github.com/madpah/requirements-parser/commit/16ffe88b71502c7b41b62893cf6f1408439ba35d))

### Unknown

* 0.7.0 Release (#95)

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt;
Co-authored-by: Maxwell G &lt;maxwell@gtmx.me&gt; ([`5c3442a`](https://github.com/madpah/requirements-parser/commit/5c3442a103e6e6e3c06bc875023da25c5ac9f572))


## v0.7.0 (2024-03-28)

### Chore

* chore: update release workflow to run from main

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`c363b80`](https://github.com/madpah/requirements-parser/commit/c363b805cf88c4cd52947a0cfc428e92468c7961))

* chore: update release workflow to run from main

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`10f0c07`](https://github.com/madpah/requirements-parser/commit/10f0c07ddc372e638e46d9481a40ec402414f66d))

### Feature

* feat: Drop support for Python 3.6, add support for Python 3.11 (#92)

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`1a455be`](https://github.com/madpah/requirements-parser/commit/1a455be331eff38dc19108da7f13c3129dcba43d))


## v0.6.0 (2024-03-27)

### Chore

* chore: revert CHANGELOG

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`2c52fef`](https://github.com/madpah/requirements-parser/commit/2c52fef60a49bee60587f7212a4e9c1a9ddf97b4))

* chore: updates for semantic versioning

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`e27c717`](https://github.com/madpah/requirements-parser/commit/e27c717e24181d8c102fd1d3e29996d2dbf3d081))

* chore: update publishing to PyPi to use Trusted Publishing

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`1a09ab9`](https://github.com/madpah/requirements-parser/commit/1a09ab950d94d049c3279cf56372453eb87c9dc1))

* chore: Revert CHANGELOG.md ([`d71ab54`](https://github.com/madpah/requirements-parser/commit/d71ab54657b25f6985d307c84f61dff017b137c0))

### Feature

* feat: upgrade CI workflows to get them running again (#90)

* ci: update actions to latest for all workflows

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`e76a3f5`](https://github.com/madpah/requirements-parser/commit/e76a3f553d145bcd9fdcb2c8aa7424b607056ee0))

### Unknown

* 0.6.0

Automatically generated by python-semantic-release ([`d6755f2`](https://github.com/madpah/requirements-parser/commit/d6755f2f39884d80dd8147b42969fce1a2ae0562))

* Merge branch &#39;master&#39; of github.com:madpah/requirements-parser ([`58d5e50`](https://github.com/madpah/requirements-parser/commit/58d5e50fe15221ede167960a6ec019104e5436ff))

* 0.6.0

Automatically generated by python-semantic-release ([`3724009`](https://github.com/madpah/requirements-parser/commit/3724009b7d10804fc0938c47950f9967ffe86ed3))

* doc: install requirements.txt before building docs

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`1ce9236`](https://github.com/madpah/requirements-parser/commit/1ce923617147dd984c280d56cb1f02fcd3589a7c))

* doc: minor doc improvements

Signed-off-by: Paul Horton &lt;paul.horton@owasp.org&gt; ([`ee91237`](https://github.com/madpah/requirements-parser/commit/ee9123745ca3cd78826b2eddd3abe2644920d15c))


## v0.5.0 (2022-01-20)

### Chore

* chore: added license header to source files

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`b8d5c56`](https://github.com/madpah/requirements-parser/commit/b8d5c5630c2297d298064c012e352816eb420e86))

### Feature

* feat: support all documented options in requirements files #62 (#63)

* feat: support all documented options in requirements files #62

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* fixed type bug

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`f92c0c0`](https://github.com/madpah/requirements-parser/commit/f92c0c079bce03b1860c78852d2c8c48cf32d539))

### Unknown

* 0.5.0

Automatically generated by python-semantic-release ([`19e3ddf`](https://github.com/madpah/requirements-parser/commit/19e3ddf21e600f92ac29a83811beaff94f8f5410))


## v0.4.0 (2022-01-18)

### Chore

* chore: removed dependency not yet required

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`5184747`](https://github.com/madpah/requirements-parser/commit/51847473358f567be245ae0f993a1ee924ec06ee))

* chore: exclude built docs from git

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`24463ba`](https://github.com/madpah/requirements-parser/commit/24463ba19a88265fc8aa0003c2b7f33f9ef88e93))

* chore: exclude built docs from git

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`9487044`](https://github.com/madpah/requirements-parser/commit/948704494fa8003b5d400f6594d5276400c76e85))

### Feature

* feat: library is now typed according to PEP561

* chore: added static analysis to CI

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`0e1bb6a`](https://github.com/madpah/requirements-parser/commit/0e1bb6a746857a59c50530155d24da487a40c4be))

### Unknown

* 0.4.0

Automatically generated by python-semantic-release ([`a16fd0b`](https://github.com/madpah/requirements-parser/commit/a16fd0b948e44526b8d228240a7692156498ef8e))

* doc: readthedocs config

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`793ce91`](https://github.com/madpah/requirements-parser/commit/793ce914074430882ba447782ae9127d8312d0bf))

* doc: readthedocs config

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`203a0ed`](https://github.com/madpah/requirements-parser/commit/203a0ed322f3a69ffbec2a1c54a27d457583a55d))

* doc: readthedocs config

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`9d22e23`](https://github.com/madpah/requirements-parser/commit/9d22e23317cd87cd73337b8af871c5655dd87fb7))


## v0.3.1 (2021-12-17)

### Fix

* fix: readthedocs config

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`ac1e7fb`](https://github.com/madpah/requirements-parser/commit/ac1e7fb616a2c15e83b8a5ca630ffd50aad4aedb))

### Unknown

* 0.3.1

Automatically generated by python-semantic-release ([`186cfd4`](https://github.com/madpah/requirements-parser/commit/186cfd4a0d90628915a4f6e3bd827a0fe2981ee7))


## v0.3.0 (2021-12-17)

### Chore

* chore: added missing config for mypy

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`4fb1bf5`](https://github.com/madpah/requirements-parser/commit/4fb1bf5d27ed530704823bf7ffee4cabba844bd5))

* chore: addressed flake8 reports

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`d3ee857`](https://github.com/madpah/requirements-parser/commit/d3ee857790a730821c8089f860595846b0ea855a))

* chore: add poetry configuration

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`4b54c79`](https://github.com/madpah/requirements-parser/commit/4b54c79bf703dd927ee686be4413a6eb6687d409))

* chore: migrated to Apache 2.0 license

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`5b7a6e4`](https://github.com/madpah/requirements-parser/commit/5b7a6e49e355a37fa6674876db4b692e8bf82943))

* chore: updated gitignore

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`07bea05`](https://github.com/madpah/requirements-parser/commit/07bea05c08da7e84e75557f6340fc80440d48f4c))

### Ci

* ci: disable type static-code-analysis until we have typed the library

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`c8da36d`](https://github.com/madpah/requirements-parser/commit/c8da36de4e6e16c12216a5b9bf0113bb990fe9aa))

* ci: added GitHub workflow to release `requirements-parser`
doc: updated license and changelog to work with new release process

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`068e3f8`](https://github.com/madpah/requirements-parser/commit/068e3f8b8d55c0d51c721a6b001271b2613e14f5))

* ci: temporarily disable min-requirements testing with tox

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`ae53393`](https://github.com/madpah/requirements-parser/commit/ae5339399fed0e739ee152a3328f2c314ecb17ad))

* ci: temporarily disable min-requirements testing with tox

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`550f8af`](https://github.com/madpah/requirements-parser/commit/550f8af422cc772a5fd16cfa2f947754c4a54115))

* ci: added GitHub workflow for CI

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`ceba061`](https://github.com/madpah/requirements-parser/commit/ceba061868ee62083c6b2c02a1dd3357620ff6e9))

### Feature

* feat: added some typing
fix: corrected a regex

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`169ff6e`](https://github.com/madpah/requirements-parser/commit/169ff6e79657d8091e6e1a4e21c7da794d507832))

* feat: removed Python 2 code

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`82f9473`](https://github.com/madpah/requirements-parser/commit/82f94733f912e140fdcc0254020f4208d3e4a892))

### Fix

* fix: removed version from __init__

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`4e83b9d`](https://github.com/madpah/requirements-parser/commit/4e83b9d3bdd5534da7adfdeb292ad2a1fae73ea8))

### Test

* test: cleaned up some sample code

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`99ffc65`](https://github.com/madpah/requirements-parser/commit/99ffc65e7ad3d1a7842800cd489099cdf2681f88))

* test: migrated test_requirement to use unittest

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`e17734a`](https://github.com/madpah/requirements-parser/commit/e17734a9afec2ebd518baadca6db4e7da6848c25))

* test: migrated test_parser to unittest and added some minor test fixes

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`5d2eebe`](https://github.com/madpah/requirements-parser/commit/5d2eebec15e087a91594778090bcc06ce00d8927))

### Unknown

* 0.3.0

Automatically generated by python-semantic-release ([`8760e01`](https://github.com/madpah/requirements-parser/commit/8760e01d59c1bb60c65dfbc6321eab506d05fab7))

* Merge pull request #56 from madpah/feat/migrate-to-poetry

Migration to Poetry and other updates after David kindly transferred to Paul ([`8833cdb`](https://github.com/madpah/requirements-parser/commit/8833cdb128ce7909c4d0dbe635fce2a410ff4023))

* doc: README is now in Markdown, not RST

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`3d78272`](https://github.com/madpah/requirements-parser/commit/3d78272588ab537e825cd32b37f8a6010d6f8d57))

* doc: README is now in Markdown, not RST

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`2a9dcf7`](https://github.com/madpah/requirements-parser/commit/2a9dcf768d5c7ca542456ad45a8664008ef1b861))

* doc: updated doc generation and changelog generation

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`6f73ee5`](https://github.com/madpah/requirements-parser/commit/6f73ee5e9478176c1efeb72087f3b1d9e9c4340c))

* Merge pull request #27 from belak/belak/editable-eol-comments

Fix parsing lines using -e and end of line comments ([`ea3dbee`](https://github.com/madpah/requirements-parser/commit/ea3dbeec76628878f6b1bbcb865670c29957f2c2))

* Merge pull request #34 from chrislawlor/feature/requirement-equality

Adds equality (and inequality) testing to Requirement class ([`d8e6737`](https://github.com/madpah/requirements-parser/commit/d8e67370cb96e535146c318ac9ec33d91f8231cc))

* Merge pull request #44 from jayvdb/sdist

MANIFEST.in: Add tests and docs ([`beda9cf`](https://github.com/madpah/requirements-parser/commit/beda9cf56111bce73fbbc52ca971407fec46a9f1))

* .travis.yml: Run Python 3.8 without coverage ([`b265c38`](https://github.com/madpah/requirements-parser/commit/b265c3862bbdd88ca76bf0ddd465ca6fc48be220))

* .travis.yml: Replace 3.3 with 3.7 &amp; 3.8

Travis no longer provides 3.3 ([`772412a`](https://github.com/madpah/requirements-parser/commit/772412a1d380517fed41d65889f20cfd828e3f5d))

* MANIFEST.in: Add tests and docs ([`ecabc1d`](https://github.com/madpah/requirements-parser/commit/ecabc1db4ab71618647bf283c49d3e10e6ef139a))

* Merge pull request #38 from cooperlees/master

Add setuptools as a install_requires Dependency ([`ad404ad`](https://github.com/madpah/requirements-parser/commit/ad404add0423d7e1f419c3a48dc884375d57f376))

* Add setuptools as a install_requires

pkg_resources is needed at runtime, lets be explicit and state that so pip etc. do the right thing. ([`212078b`](https://github.com/madpah/requirements-parser/commit/212078ba15e8af7817461fb65e16c257061107fc))


## v0.2.0 (2018-11-15)

### Unknown

* Increment version ([`52f802c`](https://github.com/madpah/requirements-parser/commit/52f802c77573c0e64240cd47246de01ffbf96c0c))

* Update changelog for release ([`2fd0faf`](https://github.com/madpah/requirements-parser/commit/2fd0faf6a742536fd2da20595607426a265f96cf))

* Adds equality (and inequality) testing to Requirement class ([`de158d7`](https://github.com/madpah/requirements-parser/commit/de158d7bf72b8faef8f82c484dbe6f6ca9d149e6))

* Merge pull request #33 from sbidoul/preserve-login-sbi

preserve login part of uri ([`caca172`](https://github.com/madpah/requirements-parser/commit/caca172b80d448c6175c1b4f5777781d583fc9b7))

* preserve login part of uri ([`c34f405`](https://github.com/madpah/requirements-parser/commit/c34f405d7cd4ff1157248c8f883fd5450ce7b7eb))

* Update the README ([`a3dc6d2`](https://github.com/madpah/requirements-parser/commit/a3dc6d256eca92e5e101b045c9de5f7fa07460c7))

* Add an authors file to credit helpful folks ([`90571d3`](https://github.com/madpah/requirements-parser/commit/90571d3d311bc96512d7f204972116c37f6fc3d9))

* Merge branch &#39;subdirectory-sbi&#39; of https://github.com/sbidoul/requirements-parser into sbidoul-subdirectory-sbi ([`b9f0290`](https://github.com/madpah/requirements-parser/commit/b9f0290cd38e3af19ccf4c63dbc5feb473732967))

* Merge pull request #30 from ticosax/fix-vcs-extras_require

Fix vcs urls parsing with extras_require ([`f9e93d0`](https://github.com/madpah/requirements-parser/commit/f9e93d0d057c0fe9a958c4b0dff1353074868835))

* Merge pull request #28 from ticosax/fix-master-py36

Produce more predictable output for tests ([`4aaeae7`](https://github.com/madpah/requirements-parser/commit/4aaeae76275792f4161a22c4e8f6a07f829083a3))

* support subdirectory fragment ([`fd2c098`](https://github.com/madpah/requirements-parser/commit/fd2c09861512b1232d4af723db36c1f4be038be9))

* [FIX] specs and extras are now unordered

Fix tests, reckoning that setuptools.parse does not
preserve ordering of specs and extras anymore. ([`5c8f85d`](https://github.com/madpah/requirements-parser/commit/5c8f85d50d986b36392ec14a17bee53c8f12ab5f))

* fixup! Extract extras from fragment&#39;s egg when vcs is specified ([`cab9ebd`](https://github.com/madpah/requirements-parser/commit/cab9ebdb834498791368dc3d86b9eef4eacf4f47))

* Extract extras from fragment&#39;s egg when vcs is specified ([`01b2f5c`](https://github.com/madpah/requirements-parser/commit/01b2f5c592405feadc833f7eaea48769b1b8a1bd))

* Produce expected output during tests

pkg_req.extras and pkg_req.specs are stored in Sets and thus ordering
can&#39;t be predicted. ([`44812d9`](https://github.com/madpah/requirements-parser/commit/44812d907cc499618b2718bf3acf36812d70e514))

* Produce expected output during tests

pkg_req.extras and pkg_req.specs are stored in Sets and thus ordering
can&#39;t be predicted. ([`817229e`](https://github.com/madpah/requirements-parser/commit/817229ea4c8837995fcaab09c7c25691e764fde2))

* Merge pull request #29 from ticosax/drop-python-3.2

Drop python 3.2 as it is not maintained since February 2016 ([`659c4af`](https://github.com/madpah/requirements-parser/commit/659c4af2c3c3b365e35b0462c2797ffd88f3761c))

* Drop python 3.2 as it is not maintained since February 2016

https://docs.python.org/devguide/devcycle.html#summary ([`bf11658`](https://github.com/madpah/requirements-parser/commit/bf116582b6d737a6971445823b812b326d58f99f))

* Drop Python2.6 support; Add 3.6 support ([`e35b9f7`](https://github.com/madpah/requirements-parser/commit/e35b9f70de74251e16f76305d006eca63abcb086))

* Merge pull request #24 from mshenfield/issue-22-add-hash-information-to-requirements

Add hash and hash_name fragment ([`af136a1`](https://github.com/madpah/requirements-parser/commit/af136a11123ebf3acc8eac983a3ef2c3586193a9))

* Fix parsing lines using -e and end of line comments ([`95006a3`](https://github.com/madpah/requirements-parser/commit/95006a3dd1343fee721ae479deb53083530edac8))

* Flake8 3.0 dropped support for Python26 ([`4a43544`](https://github.com/madpah/requirements-parser/commit/4a43544dfc22cd08835ddbf8b920b7e5a3e3b283))

* Add setup.py notes about 3.4-3.5 ([`9e85381`](https://github.com/madpah/requirements-parser/commit/9e85381a57913d2d8b79c119127363ebbcfc5bbd))

* Travis CI updates

- Add Python 3.4-3.5
- fix an issue with old pip ([`93428bb`](https://github.com/madpah/requirements-parser/commit/93428bbc48637d00269651ae07d0977d4cae5a97))

* Add hash and hash_name from fragment

This supports retreiving hashing algorithms [supported by pip](https://github.com/pypa/pip/blob/281eb61b09d87765d7c2b92f6982b3fe76ccb0af/pip/index.py#L947). If multiple algorithms are present in the fragemnt portion of a url, the hashes included in the requirement will be non-deterministic. ([`86c46b3`](https://github.com/madpah/requirements-parser/commit/86c46b32debb50f57284a06f010c27a30d646efd))

* Merge pull request #23 from mshenfield/issue-22-support-hashlib-hashes-in-uri-fragment

Parsing fragment supports arbitrary keys ([`b05c2ff`](https://github.com/madpah/requirements-parser/commit/b05c2ffa806f72b1d4248a20423711bbe458fb5c))

* Bump coverage for testing to &lt; 4 to fix Travis 3.2 build

More information on the travis-ci issue tracker [here](https://github.com/travis-ci/travis-ci/issues/4866) ([`09379dc`](https://github.com/madpah/requirements-parser/commit/09379dc16995b6cf2b88381a2830b1aa695cd08e))

* Added test for editable local files

This satisfies coveralls. Because I added lines of code to an untested portion of the codebase, the overall coverage went down. ([`5db4fde`](https://github.com/madpah/requirements-parser/commit/5db4fde6d387c276f0d87c4e06bef309acedfd21))

* Parsing fragment supports arbitrary keys

This switches parsing the fragment (string following &#39;#&#39; at the end of a requirement) from looking for &#39;egg&#39; at the beginning of the fragment to allowing any key value pair. These can be extracted as needed - right now only the &#39;egg&#39; key is used to get the name of the package.

Tests include URI with a single fragment, and multiple fragments. ([`f9559f7`](https://github.com/madpah/requirements-parser/commit/f9559f7c364c9ea8e9e4d3a888ee33266de69e40))


## v0.1.0 (2015-05-03)

### Unknown

* Update versions ([`c84b72a`](https://github.com/madpah/requirements-parser/commit/c84b72ad3f4318832cf87f9610c2f7a49c590964))

* Update sphinx theme ([`c54532c`](https://github.com/madpah/requirements-parser/commit/c54532cf22a82e266cb4a13ca25d67c1c36156b8))

* Update the year ([`294959e`](https://github.com/madpah/requirements-parser/commit/294959ef80ad81796c4135ef7ac961c3e30c9194))

* Update the changelog ([`8efccb2`](https://github.com/madpah/requirements-parser/commit/8efccb276d950ff35dda6ce9d03a52ad19111bf3))

* Merge pull request #19 from jaysonsantos/master

add ability to parse recursive requirements ([`5b1721f`](https://github.com/madpah/requirements-parser/commit/5b1721fe82241d1f84a3c822b7d4bdc0eb12505a))

* Fix pep8 max column size ([`8fefe15`](https://github.com/madpah/requirements-parser/commit/8fefe15c24f4b1bd7017ff6f7452fc266940a153))

* add ability to parse recursive requirements ([`fa55463`](https://github.com/madpah/requirements-parser/commit/fa55463ddc3e08c652308c29dbd31dceb41564c8))

* Merge pull request #17 from saschpe/master-underscores

Properly parse underscores ([`a6af275`](https://github.com/madpah/requirements-parser/commit/a6af275c96523cd781fa6b1f6b1e1c7f697d504f))

* Properly parse underscores

pkg_resources.Requirement&#39;s constructor calls save_name() on the
project_name member which converts underscores to hyphens. Thus use
Requirement.unsafe_name (the pristine name) instead. ([`6403d51`](https://github.com/madpah/requirements-parser/commit/6403d5145f1ad7b3705a624b614900eace5433eb))


## v0.0.6 (2013-08-17)

### Unknown

* v0.0.6 :sparkles: ([`7b0cc23`](https://github.com/madpah/requirements-parser/commit/7b0cc239db30581809e081071b6945d63980173c))

* v0.0.5 :sparkles: ([`773bba5`](https://github.com/madpah/requirements-parser/commit/773bba5d8bdab0cbe674220fea0d96320204b743))


## v0.0.5 (2013-08-17)

### Unknown

* Dated the changelog ([`e2e13c4`](https://github.com/madpah/requirements-parser/commit/e2e13c4ce20963378f57959f9eb70845e4ba1be4))

* Bumped version ([`e5c22ce`](https://github.com/madpah/requirements-parser/commit/e5c22cebdcdb4bfcdf9d9014dd7333c72ca6f131))

* Added usage for common examples ([`e907e6c`](https://github.com/madpah/requirements-parser/commit/e907e6c9f65736ec45c829a8b2034b6c01e87e74))

* Added installation ([`de70666`](https://github.com/madpah/requirements-parser/commit/de706660238413b39d23cde47b09edc540f3aefa))

* Oops ([`56e2cd7`](https://github.com/madpah/requirements-parser/commit/56e2cd74120803449bc7cc0cfee17346fcd9e1ca))

* Added documentation ([`8e11fdd`](https://github.com/madpah/requirements-parser/commit/8e11fdd4e7126b98f4cb58d61c2984bd71356962))

* :sparkles: 2013 (I&#39;m late) ([`8c8131c`](https://github.com/madpah/requirements-parser/commit/8c8131c97a4f61513acd87218163053ad5e397ad))

* Added coverage badge ([`045c686`](https://github.com/madpah/requirements-parser/commit/045c686ce0d004bd33612b5034e247dfc5d15e4b))

* Merge pull request #15 from davidfischer/coveralls

Added code coverage ([`57cbe4b`](https://github.com/madpah/requirements-parser/commit/57cbe4b9f2981780b9b74b2d55eeea044fda1297))

* Added code coverage ([`c36dc51`](https://github.com/madpah/requirements-parser/commit/c36dc51ce8439139cbada3ea3e4555a10e72804d))

* Merge pull request #14 from davidfischer/parser-refactor

Big parser refactor ([`547106f`](https://github.com/madpah/requirements-parser/commit/547106f67d92c82a2f5e0ea66c5881e7685a3c8a))

* Switch to unicode literals ([`b8810af`](https://github.com/madpah/requirements-parser/commit/b8810af9e686c18e05029541ee005d3baecb7a67))

* Big parser refactor

* broke the parser into a Requirement class
* refactored the unit test suite
* better handling of VCS ([`a7a4910`](https://github.com/madpah/requirements-parser/commit/a7a4910a78cc38881c7a6559a45d274f146ca3c7))

* Merge pull request #13 from davidfischer/refactor-tests

Refactored tests into test files ([`a12ffae`](https://github.com/madpah/requirements-parser/commit/a12ffae3b8204ed4b0978e605d3f811013f066a4))

* Refactored tests into test files

Each test has a txt file and an expected file (except &#34;fails&#34;) ([`3058539`](https://github.com/madpah/requirements-parser/commit/3058539596fe8fe851aae79e396a1223996ccbd3))

* Merge pull request #9 from valmet/master

Compiled regular expressions ([`9d8af15`](https://github.com/madpah/requirements-parser/commit/9d8af15ce4dec6128aefdb793a29e85133884547))

* It should be pass tests... please. ([`a4cf621`](https://github.com/madpah/requirements-parser/commit/a4cf6213d07a9c51242bd150431c8829842b87e1))

* Oh, shi~... autopep8. ([`28d483e`](https://github.com/madpah/requirements-parser/commit/28d483ee529beeed61efd22a8d9a39a47bde9094))

* Flags ([`78b17aa`](https://github.com/madpah/requirements-parser/commit/78b17aa3d7d73146b505fccf05c5db17d3b0b6ad))

* Compiled regular expressions ([`9adb0a5`](https://github.com/madpah/requirements-parser/commit/9adb0a574dafcb26d0157ca564b01afd93a89c25))

* Introduce code quality ([`26f1067`](https://github.com/madpah/requirements-parser/commit/26f106751400971666862306cc63dcfcd24c3c9c))


## v0.0.4 (2013-05-29)

### Unknown

* Version v0.0.4 :sparkles: ([`3d7cc24`](https://github.com/madpah/requirements-parser/commit/3d7cc24fe904223f11dc1f982fe64232d8a8f10c))

* Slight stylistic change ([`51d0369`](https://github.com/madpah/requirements-parser/commit/51d036997e961cd17b2d553b61fc2c01892d6dbd))

* Ignore file can handle multiple virtualenvs ([`0f2246a`](https://github.com/madpah/requirements-parser/commit/0f2246ad8f63cfaee399cb9a790d95b94132df88))

* Merge pull request #7 from davidfischer/pkg-resources

Use pkg_resources for parsing ([`48a8179`](https://github.com/madpah/requirements-parser/commit/48a81792130808883d30be0a6432aa5695a88c80))

* Added a couple tests ([`a0a448f`](https://github.com/madpah/requirements-parser/commit/a0a448f5d07b291eaec05ec984a9311ac3ea5147))

* Finally got this right ([`6d8200e`](https://github.com/madpah/requirements-parser/commit/6d8200ec02942abb791b2e2db3a728cd3999139b))

* Fixed typo ([`b7fbb35`](https://github.com/madpah/requirements-parser/commit/b7fbb35fbf9ff58d9ef5ab31b78a55d8be4f32f7))

* Updated readme with new example ([`de275bb`](https://github.com/madpah/requirements-parser/commit/de275bbf7502409b7971ef5c08bcc8621bedca1b))

* Using pkg_resources to parse requirements

* Backwards incompatible API change!
* Using regex for URI/file/VCS requirements ([`1e272de`](https://github.com/madpah/requirements-parser/commit/1e272de42e8b943d4d2e79b9b071a5b87dde3f20))

* Permission fix ([`cdc5b4b`](https://github.com/madpah/requirements-parser/commit/cdc5b4bece1f66923ddd7b66d211d034488cc6bf))


## v0.0.3 (2013-05-28)

### Unknown

* Version 0.0.3 :sparkles: ([`fc0a140`](https://github.com/madpah/requirements-parser/commit/fc0a1403c9a9eae5f093906fac811420f8c66c9f))

* Updated name in license ([`f7ecdab`](https://github.com/madpah/requirements-parser/commit/f7ecdaba0d13c6c7297c712f68aaa488626f23bc))

* Name change on travis ([`ef38eb6`](https://github.com/madpah/requirements-parser/commit/ef38eb6384080a1de38d6781dfebc2c848cdbf41))

* Merge pull request #6 from davidfischer/name-change

Changed name to requirements parser ([`2c56a6b`](https://github.com/madpah/requirements-parser/commit/2c56a6b66dfd7904debdc13a1b64fcb2c0455bc3))

* Changed name to requirements parser

Changed module name to requirements ([`d995b0c`](https://github.com/madpah/requirements-parser/commit/d995b0cf6d5c1c852b5cf85a65bc2d03875a82aa))


## v0.0.2 (2013-05-27)

### Unknown

* Version v0.0.2 :sparkles: ([`772bda4`](https://github.com/madpah/requirements-parser/commit/772bda498571f7d3ff00d08834bf7f42e3556bc7))

* Formatting improvements ([`662e85e`](https://github.com/madpah/requirements-parser/commit/662e85e49f20a84a6ce03167c1f16f075f9d7539))

* No longer testing on 3.0 and 3.1

However, the wall of superpowers at least checks for
Programming Language :: Python :: 3 ([`14bc67d`](https://github.com/madpah/requirements-parser/commit/14bc67d0e1eb5144b5219a7590d2d4aa4b7561ef))

* Travis does not support Python 3.0 or Python 3.1

http://about.travis-ci.org/docs/user/ci-environment/#Python-VM-images ([`7971479`](https://github.com/madpah/requirements-parser/commit/7971479453716d4d8d67383eeeda7fafc1553ff9))

* Merge pull request #2 from treyhunner/add-manifest

Add manifest ([`d7649b6`](https://github.com/madpah/requirements-parser/commit/d7649b607799566332b239ddea6197aea0d54e69))

* Add MANIFEST file noting inclusion of rst files ([`87fe595`](https://github.com/madpah/requirements-parser/commit/87fe595679ab14d35ba50c3f44d846d792378c62))

* Bump version (between releases) ([`426e337`](https://github.com/madpah/requirements-parser/commit/426e337895fa3a9ffb9dd2c81d1d833ec3609c53))

* Merge pull request #1 from davidfischer/image-fix

Fix travis-ci link ([`85601b6`](https://github.com/madpah/requirements-parser/commit/85601b6ff1b665f18571a3986fd1d5eeff3a1b05))

* Fix travis-ci link ([`944ae07`](https://github.com/madpah/requirements-parser/commit/944ae07dc1967b32ef61d1357a4e323d2a9e9290))

* Fixed copy/paste issues ([`015058d`](https://github.com/madpah/requirements-parser/commit/015058da1c86ee92fca281b8ee4bfe12d51507dc))

* Added classifiers for 3.x ([`866a887`](https://github.com/madpah/requirements-parser/commit/866a88740d822d2bc4bed2b789407713f73b8651))

* Added unit testing for Python3 ([`47c6742`](https://github.com/madpah/requirements-parser/commit/47c67429c6417b1a097910aac6fec4b2052dd269))

* Added 3.x compatibility ([`fe6789f`](https://github.com/madpah/requirements-parser/commit/fe6789fe6aecc0e84a850d695813aea0d87ccb48))

* Added travis-ci image ([`e4b612e`](https://github.com/madpah/requirements-parser/commit/e4b612e5949b4115e71157b3b84c46933a729746))

* Added continuous integration ([`8aa6e53`](https://github.com/madpah/requirements-parser/commit/8aa6e532ddf18c9421b15282af9b65a0cb3ab8b8))

* Added additional test from crate.io reqs ([`ad1ae22`](https://github.com/madpah/requirements-parser/commit/ad1ae222070aaec860ed1199d0122b69da88b91d))


## v0.0.1 (2012-11-25)

### Unknown

* Added license file ([`f243bc5`](https://github.com/madpah/requirements-parser/commit/f243bc58d172e1ac0d6e453782c6b61cba879f4d))

* Added tests and fixed corresponding issues

- added RTFD req files as tests
- added tests for warnings and other tests
- updated parser to handle more edge cases ([`8434fd2`](https://github.com/madpah/requirements-parser/commit/8434fd25f928fe0f9de48e7ad4a71407fd388e76))

* Added the first cut

- parse editables (svn+http...)
- parse file URIs
- parse &#34;normal&#34;
- parse extras ([`d04253a`](https://github.com/madpah/requirements-parser/commit/d04253a61e85faee3b6000f8620af05114b8ba48))

* Added test for file-like obj ([`819de98`](https://github.com/madpah/requirements-parser/commit/819de98a18d87018aee905bf1e6afab6d3f8197c))

* Added trivial version

- Added test for empty parse
- Added version info
- Added setup.py
- Added parser that always returns empty ([`168d8c1`](https://github.com/madpah/requirements-parser/commit/168d8c1cebd956cf8f5fba708bb1eab3725315c2))

* Added README with proposed functionality

- Parse function accepts file or string
- CONSIDER: list of dicts instead of tuples ([`0a0e4d7`](https://github.com/madpah/requirements-parser/commit/0a0e4d70af7a3b9766b223a809e51fb2dedf224b))

* Added ignorefile ([`e25c719`](https://github.com/madpah/requirements-parser/commit/e25c719360406409f819a03b620d527b3aa2a835))
