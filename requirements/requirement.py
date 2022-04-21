# encoding: utf-8

# This file is part of requirements-parser library.
#
# Licensed under the Apache License, Version 2.0 (the "License");
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

from __future__ import unicode_literals

import re
from typing import Any, cast, Dict, Iterable, List, Match, Optional, Set

from pkg_resources import Requirement as Req

from .fragment import get_hash_info, parse_fragment, parse_extras_require
from .vcs import VCS, VCS_SCHEMES

URI_REGEX = re.compile(
    r'^(?P<scheme>https?|file|ftps?)://(?P<path>[^#]+)'
    r'(#(?P<fragment>\S+))?'
)

VCS_SCHEMES_REGEX = r'|'.join([scheme.replace('+', r'\+') for scheme in VCS_SCHEMES])
VCS_REGEX = re.compile(
    rf'^(?P<scheme>{VCS_SCHEMES_REGEX})://((?P<login>[^/@]+)@)?'
    r'(?P<path>[^#@]+)(@(?P<revision>[^#]+))?(#(?P<fragment>\S+))?'
)

# This matches just about everything
LOCAL_REGEX = re.compile(r'^((?P<scheme>file)://)?(?P<path>[^#]+)#(?P<fragment>\S+)?')


class Requirement:
    """
    Represents a single requirement

    Typically, instances of this class are created with ``Requirement.parse``.
    For local file requirements, there's no verification that the file
    exists. This class attempts to be *dict-like*.

    See: http://www.pip-installer.org/en/latest/logic.html

    **Members**:

    * ``line`` - the actual requirement line being parsed
    * ``editable`` - a boolean whether this requirement is "editable"
    * ``local_file`` - a boolean whether this requirement is a local file/path
    * ``specifier`` - a boolean whether this requirement used a requirement
      specifier (eg. "django>=1.5" or "requirements")
    * ``vcs`` - a string specifying the version control system
    * ``revision`` - a version control system specifier
    * ``name`` - the name of the requirement
    * ``uri`` - the URI if this requirement was specified by URI
    * ``subdirectory`` - the subdirectory fragment of the URI
    * ``path`` - the local path to the requirement
    * ``hash_name`` - the type of hashing algorithm indicated in the line
    * ``hash`` - the hash value indicated by the requirement line
    * ``extras`` - a list of extras for this requirement
      (eg. "mymodule[extra1, extra2]")
    * ``specs`` - a list of specs for this requirement
      (eg. "mymodule>1.5,<1.6" => [('>', '1.5'), ('<', '1.6')])
    """

    def __init__(self, *, line: str, editable: bool = False, local_file: bool = False, specifier: bool = False,
                 vcs: Optional[str] = None, revision: Optional[str] = None, name: Optional[str] = None,
                 uri: Optional[str] = None, subdirectory: Optional[str] = None, path: Optional[str] = None,
                 hash_name: Optional[str] = None, hash_: Optional[str] = None, extras: Optional[Iterable[str]] = None,
                 specs: Optional[Iterable[tuple[str, str]]] = None) -> None:
        # Do not call this private method
        self.line = line
        self.editable = editable
        self.local_file = local_file
        self.specifier = specifier
        self.vcs = vcs
        self.revision = revision
        self.name = name
        self.uri = uri
        self.subdirectory = subdirectory
        self.path = path
        self.hash_name = hash_name
        self.hash_ = hash_
        self.extras = set(extras or [])
        self.specs = set(specs or [])

    @property
    def line(self) -> str:
        """
        The actual requirement line being parsed.

        Returns:
            `str`
        """
        return self._line

    @line.setter
    def line(self, line: str) -> None:
        self._line = line

    @property
    def editable(self) -> bool:
        """
        Whether this requirement is "editable".

        Returns:
            `bool`
        """
        return self._editable

    @editable.setter
    def editable(self, editable: bool) -> None:
        self._editable = editable

    @property
    def local_file(self) -> bool:
        """
        Whether this requirement is a local file/path.

        Returns:
             `bool`
        """
        return self._local_file

    @local_file.setter
    def local_file(self, local_file: bool) -> None:
        self._local_file = local_file

    @property
    def specifier(self) -> bool:
        """
        Whether this requirement used a requirement specifier (eg. "django>=1.5" or "requirements").

        Returns:
             `bool`
        """
        return self._specifier

    @specifier.setter
    def specifier(self, specifier: bool) -> None:
        self._specifier = specifier

    @property
    def vcs(self) -> Optional[str]:
        return self._vcs

    @vcs.setter
    def vcs(self, vcs: Optional[str]) -> None:
        self._vcs = vcs

    @property
    def revision(self) -> Optional[str]:
        """
        Version control system specifier.

        Returns:
             `str` or `None`
        """
        return self._revision

    @revision.setter
    def revision(self, revision: Optional[str]) -> None:
        self._revision = revision

    @property
    def name(self) -> Optional[str]:
        """
        Name of the requirement.

        Returns:
             `str` or `None`
        """
        return self._name

    @name.setter
    def name(self, name: Optional[str]) -> None:
        self._name = name

    @property
    def uri(self) -> Optional[str]:
        """
        The URI if this requirement was specified by URI.

        Returns:
             `str` or `None`
        """
        return self._uri

    @uri.setter
    def uri(self, uri: Optional[str]) -> None:
        self._uri = uri

    @property
    def subdirectory(self) -> Optional[str]:
        """
        The subdirectory fragment of the URI.

        Returns:
             `str` or `None`
        """
        return self._subdirectory

    @subdirectory.setter
    def subdirectory(self, subdirectory: Optional[str]) -> None:
        self._subdirectory = subdirectory

    @property
    def path(self) -> Optional[str]:
        """
        The local path to the requirement.

        Returns:
             `str` or `None`
        """
        return self._path

    @path.setter
    def path(self, path: Optional[str]) -> None:
        self._path = path

    @property
    def hash_name(self) -> Optional[str]:
        """
        The type of hashing algorithm indicated in the line.

        Returns:
             `str` or `None`
        """
        return self._hash_name

    @hash_name.setter
    def hash_name(self, hash_name: Optional[str]) -> None:
        self._hash_name = hash_name

    @property
    def hash_(self) -> Optional[str]:
        """
        The hash value indicated by the requirement line.

        Returns:
            `str` or `None`
        """
        return self._hash_

    @hash_.setter
    def hash_(self, hash_: Optional[str]) -> None:
        self._hash_ = hash_

    @property
    def extras(self) -> Set[str]:
        """
        A set of extras for this requirement.

        Returns:
             `Set[str]`
        """
        return self._extras

    @extras.setter
    def extras(self, extras: Iterable[str]) -> None:
        self._extras = set(extras)

    @property
    def specs(self) -> Set[tuple[str, str]]:
        """
        A set of specs for this requirement.

        Returns:
             Set of `Tuple[str, str]`
        """
        return self._specs

    @specs.setter
    def specs(self, specs: Iterable[tuple[str, str]]) -> None:
        self._specs = set(specs)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Requirement):
            return hash(self) == hash(other)
        return False

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def __hash__(self) -> int:
        return hash(
            (self.editable, self.local_file, self.specifier, self.vcs, self.revision, self.name, self.uri,
             self.subdirectory, self.path, self.hash_name, self.hash_, *sorted(list(self.extras)),
             *sorted(list(self.specs)))
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __repr__(self) -> str:
        print(self.__dict__)
        return f'<Requirement: "{self.line}">'

    def keys(self) -> Iterable[str]:
        return self.__dict__.keys()

    @classmethod
    def parse_editable(cls, line: str) -> 'Requirement':
        """
        Parses a Requirement from an "editable" requirement which is either
        a local project path or a VCS project URI.

        See: pip/req.py:from_editable()

        :param line: an "editable" requirement
        :returns: a Requirement instance for the given line
        :raises: ValueError on an invalid requirement
        """

        req = cls(line='-e {0}'.format(line))
        req.editable = True

        if ' #' in line:
            line = line[:line.find(' #')]

        vcs_match: Optional[Match[str]] = VCS_REGEX.match(line)
        local_match: Optional[Match[str]] = LOCAL_REGEX.match(line)

        if vcs_match is not None:
            groups: Dict[str, str] = vcs_match.groupdict()
            if groups.get('login'):
                req.uri = '{scheme}://{login}@{path}'.format(**groups)
            else:
                req.uri = '{scheme}://{path}'.format(**groups)
            req.revision = groups['revision']
            if groups['fragment']:
                fragment = parse_fragment(groups['fragment'])
                egg = cast(str, fragment.get('egg'))
                req.name, req.extras = parse_extras_require(egg)  # type: ignore
                req.hash_name, req.hash_ = get_hash_info(fragment)
                req.subdirectory = fragment.get('subdirectory')
            for vcs in VCS:
                if str(req.uri).startswith(vcs):
                    req.vcs = vcs  # type: ignore
        else:
            assert local_match is not None, 'This should match everything'
            groups = local_match.groupdict()
            req.local_file = True
            if groups['fragment']:
                fragment = parse_fragment(groups['fragment'])
                egg = cast(str, fragment.get('egg'))
                req.name, req.extras = parse_extras_require(egg)  # type: ignore
                req.hash_name, req.hash = get_hash_info(fragment)  # type: ignore
                req.subdirectory = fragment.get('subdirectory')  # type: ignore
            req.path = cast(str, groups['path'])  # type: ignore

        return req

    @classmethod
    def parse_line(cls, line: str) -> 'Requirement':
        """
        Parses a Requirement from a non-editable requirement.

        See: pip/req.py:from_line()

        :param line: a "non-editable" requirement
        :returns: a Requirement instance for the given line
        :raises: ValueError on an invalid requirement
        """

        req = cls(line=line)

        vcs_match: Optional[Match[str]] = VCS_REGEX.match(line)
        uri_match: Optional[Match[str]] = URI_REGEX.match(line)
        local_match: Optional[Match[str]] = LOCAL_REGEX.match(line)

        if vcs_match is not None:
            groups = vcs_match.groupdict()
            if groups.get('login'):
                req.uri = '{scheme}://{login}@{path}'.format(**groups)
            else:
                req.uri = '{scheme}://{path}'.format(**groups)
            req.revision = groups['revision']
            if groups['fragment']:
                fragment = parse_fragment(groups['fragment'])
                egg = fragment.get('egg')
                req.name, req.extras = parse_extras_require(egg)  # type: ignore
                req.hash_name, req.hash_ = get_hash_info(fragment)
                req.subdirectory = fragment.get('subdirectory')
            for vcs in VCS:
                if str(req.uri).startswith(vcs):
                    req.vcs = vcs  # type: ignore
        elif uri_match is not None:
            groups = uri_match.groupdict()
            req.uri = '{scheme}://{path}'.format(**groups)
            if groups['fragment']:
                fragment = parse_fragment(groups['fragment'])
                egg = fragment.get('egg')
                req.name, req.extras = parse_extras_require(egg)  # type: ignore
                req.hash_name, req.hash_ = get_hash_info(fragment)
                req.subdirectory = fragment.get('subdirectory')
            if groups['scheme'] == 'file':
                req.local_file = True
        elif '#egg=' in line:
            # Assume a local file match
            assert local_match is not None, 'This should match everything'
            groups = local_match.groupdict()
            req.local_file = True
            if groups['fragment']:
                fragment = parse_fragment(groups['fragment'])
                egg = fragment.get('egg')
                name, extras = parse_extras_require(egg)
                req.name = fragment.get('egg')
                req.hash_name, req.hash_ = get_hash_info(fragment)
                req.subdirectory = fragment.get('subdirectory')
            req.path = groups['path']
        else:
            # This is a requirement specifier.
            # Delegate to pkg_resources and hope for the best
            req.specifier = True
            pkg_req = Req.parse(line)
            req.name = pkg_req.unsafe_name
            req.extras = set(pkg_req.extras)
            req.specs = set(pkg_req.specs)
        return req

    @classmethod
    def parse(cls, line: str) -> 'Requirement':
        """
        Parses a Requirement from a line of a requirement file.

        :param line: a line of a requirement file
        :returns: a Requirement instance for the given line
        :raises: ValueError on an invalid requirement
        """

        if line.startswith('-e') or line.startswith('--editable'):
            # Editable installs are either a local project path
            # or a VCS project URI
            return cls.parse_editable(
                re.sub(r'^(-e|--editable=?)\s*', '', line))

        return cls.parse_line(line)
