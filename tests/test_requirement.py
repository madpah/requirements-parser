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
import unittest
from typing import Tuple
from unittest import TestCase

from requirements.requirement import Requirement


class TestRequirement(TestCase):

    @staticmethod
    def get_reqs(requirement_1: str, requirement_2: str) -> Tuple[Requirement, Requirement]:
        return (Requirement.parse(requirement_1),
                Requirement.parse(requirement_2))

    # Taken from https://pip.pypa.io/en/stable/cli/pip_install/#examples

    def test_somepackage_latest(self) -> None:
        a, b = TestRequirement.get_reqs('SomePackage', 'SomePackage')
        self.assertEqual(a, b)
        self.assertEqual('SomePackage', a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_somepackage_exact_version(self) -> None:
        a, b = TestRequirement.get_reqs('SomePackage==1.0', 'SomePackage==1.0')
        self.assertEqual(a, b)
        self.assertEqual('SomePackage==1.0', a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual({('==', '1.0')}, a.specs)

    def test_somepackage_minimum_version(self) -> None:
        a, b = TestRequirement.get_reqs('SomePackage>=1.0.4', 'SomePackage>=1.0.4')
        self.assertEqual(a, b)
        self.assertEqual('SomePackage>=1.0.4', a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual({('>=', '1.0.4')}, a.specs)

    def test_local_project_in_editable_mode_current_directory(self) -> None:
        a, b = TestRequirement.get_reqs('-e .', '-e .')
        self.assertEqual(a, b)
        self.assertEqual('-e .', a.line)
        self.assertTrue(a.editable)
        self.assertTrue(a.local_file)
        self.assertFalse(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertIsNone(a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertEqual('.', a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_local_project_in_editable_mode_another_directory(self) -> None:
        a, b = TestRequirement.get_reqs('-e path/to/project', '-e path/to/project')
        self.assertEqual(a, b)
        self.assertEqual('-e path/to/project', a.line)
        self.assertTrue(a.editable)
        self.assertTrue(a.local_file)
        self.assertFalse(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertIsNone(a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertEqual('path/to/project', a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    @unittest.skip('Not yest supported - see issue #74')
    def test_vcs_project_git_https_exact_version(self) -> None:
        a, b = TestRequirement.get_reqs(
            'SomeProject@git+https://git.repo/some_pkg.git@1.3.1',
            'SomeProject@git+https://git.repo/some_pkg.git@1.3.1'
        )
        self.assertEqual(a, b)
        self.assertEqual('SomeProject@git+https://git.repo/some_pkg.git@1.3.1', a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertEqual('git+https', a.vcs)
        self.assertEqual('1.3.1', a.revision)
        self.assertEqual('SomeProject', a.name)
        self.assertEqual('git+https://git.repo/some_pkg.git', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_editable_vcs_git_https(self) -> None:
        req_line: str = '-e git+https://git.repo/some_pkg.git#egg=SomePackage'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertTrue(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertEqual('git', a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertEqual('git+https://git.repo/some_pkg.git', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_editable_vcs_mercurial_https(self) -> None:
        req_line: str = '-e hg+https://hg.repo/some_pkg.git#egg=SomePackage'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertTrue(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertEqual('hg', a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertEqual('hg+https://hg.repo/some_pkg.git', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_editable_vcs_svn_https(self) -> None:
        req_line: str = '-e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackageInSVN'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertTrue(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertEqual('svn', a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackageInSVN', a.name)
        self.assertEqual('svn+svn://svn.repo/some_pkg/trunk/', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_editable_vcs_git_https_feature_branch(self) -> None:
        req_line: str = '-e git+https://git.repo/some_pkg.git@feature#egg=SomePackageInGit'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertTrue(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertEqual('git', a.vcs)
        self.assertEqual('feature', a.revision)
        self.assertEqual('SomePackageInGit', a.name)
        self.assertEqual('git+https://git.repo/some_pkg.git', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_editable_vcs_git_https_in_subdirectory(self) -> None:
        req_line: str = '-e git+https://git.repo/some_repo.git#egg=subdir&subdirectory=subdir_path'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertTrue(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertEqual('git', a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('subdir', a.name)
        self.assertEqual('git+https://git.repo/some_repo.git', a.uri)
        self.assertEqual('subdir_path', a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    @unittest.skip('Is this a valid test - would the quotes be present in requirements.txt? TBC')
    def test_editable_vcs_git_https_in_subdirectory_quoted(self) -> None:
        req_line: str = '-e "git+https://git.repo/some_repo.git#egg=subdir&subdirectory=subdir_path"'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertTrue(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertEqual('git', a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('subdir', a.name)
        self.assertEqual('git+https://git.repo/some_repo.git', a.uri)
        self.assertEqual('subdir_path', a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_package_with_extra(self) -> None:
        req_line: str = 'SomePackage[PDF]'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual({'pdf'}, a.extras)  # case issue?
        self.assertSetEqual(set(), a.specs)

    @unittest.skip('Not yet supported - see issue #75')
    def test_package_with_extra_in_vcs_git_https(self) -> None:
        req_line: str = 'SomePackage[PDF] @ git+https://git.repo/SomePackage@main#subdirectory=subdir_path"'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertEqual('git', a.vcs)
        self.assertEqual('main', a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertEqual('git+https://git.repo/SomePackage', a.uri)
        self.assertEqual('subdir_path', a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual({'pdf'}, a.extras)  # case issue?
        self.assertSetEqual(set(), a.specs)

    @unittest.skip('See issue #76 and #68')
    def test_package_current_directory_with_extra(self) -> None:
        """
        Install the current package in the current directory with the extra of 'PDF'
        """
        req_line: str = '.[PDF]'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertIsNone(a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertEqual('.', a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual({'pdf'}, a.extras)  # case issue?
        self.assertSetEqual(set(), a.specs)

    def test_package_exact_version_with_extra(self) -> None:
        req_line: str = 'SomePackage[PDF]==3.0'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual({'pdf'}, a.extras)
        self.assertSetEqual({('==', '3.0')}, a.specs)

    def test_package_with_multiple_extras(self) -> None:
        req_line: str = 'SomePackage[PDF,EPUB]'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertTrue(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomePackage', a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual({'pdf', 'epub'}, a.extras)  # case issue?
        self.assertSetEqual(set(), a.specs)

    @unittest.skip('Not yet supported - see issue #75')
    def test_local_source_archive(self) -> None:
        """
        Result of running `pip install ./downloads/SomePackage-1.0.4.tar.gz` or equivalent.
        """
        req_line: str = 'packageurl-python @ file:///path/to/dist/packageurl-python-0.9.9.tar.gz'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertTrue(a.local_file)
        self.assertFalse(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('packageurl-python', a.name)
        self.assertIsNone(a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertEqual('/path/to/dist/packageurl-python-0.9.9.tar.gz', a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    def test_remote_source_archive(self) -> None:
        """
        `http://my.package.repo/SomePackage-1.0.4.zip` in a requirements.txt followed by a
        `pip install -r requirements.txt` would result in a `pip freeze` output including:

        `pyfav @ https://files.pythonhosted.org/packages/fe/a2/
        a0281199dedf1912de75a9a631b5855ae6e86ad6f67030fad3c9e4e29804/pyfav-0.1.tar.gz`
        """
        req_line: str = 'http://my.package.repo/SomePackage-1.0.4.zip'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertIsNone(a.name)
        self.assertEqual('http://my.package.repo/SomePackage-1.0.4.zip', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual(set(), a.specs)

    @unittest.skip('Not yet supported - see issue #75')
    def test_remote_source_package_pep_440_1(self) -> None:
        req_line: str = 'SomeProject@http://my.package.repo/SomeProject-1.2.3-py33-none-any.whl'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomeProject', a.name)
        self.assertEqual('http://my.package.repo/SomeProject-1.2.3-py33-none-any.whl', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual({['==', '1.2.3']}, a.specs)

    @unittest.skip('Not yet supported - see issue #75')
    def test_remote_source_package_pep_440_2(self) -> None:
        req_line: str = '"SomeProject @ http://my.package.repo/SomeProject-1.2.4-py33-none-any.whl"'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomeProject', a.name)
        self.assertEqual('http://my.package.repo/SomeProject-1.2.4-py33-none-any.whl', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual({['==', '1.2.4']}, a.specs)

    @unittest.skip('Not yet supported - see issue #75')
    def test_remote_source_package_pep_440_3(self) -> None:
        req_line: str = 'SomeProject@http://my.package.repo/1.2.5.tar.gz'
        a, b = TestRequirement.get_reqs(req_line, req_line)
        self.assertEqual(a, b)
        self.assertEqual(req_line, a.line)
        self.assertFalse(a.editable)
        self.assertFalse(a.local_file)
        self.assertFalse(a.specifier)
        self.assertIsNone(a.vcs)
        self.assertIsNone(a.revision)
        self.assertEqual('SomeProject', a.name)
        self.assertEqual('http://my.package.repo/1.2.3.tar.gz', a.uri)
        self.assertIsNone(a.subdirectory)
        self.assertIsNone(a.path)
        self.assertIsNone(a.hash_name)
        self.assertIsNone(a.hash_)
        self.assertSetEqual(set(), a.extras)
        self.assertSetEqual({['==', '1.2.5']}, a.specs)

    def test_simple_equality(self) -> None:
        self.assertEqual(*TestRequirement.get_reqs("pylib==1.0.0", "pylib==1.0.0"))

    def test_equality_no_specifiers(self) -> None:
        self.assertEqual(*TestRequirement.get_reqs("pylib", "pylib"))

    def test_simple_inequality(self) -> None:
        self.assertNotEqual(*TestRequirement.get_reqs("pylib==1.0.0", "pylib==1.0.1"))

    def test_spec_order_equality(self) -> None:
        """
        The same specifications, in a different order, are still equal
        """
        self.assertEqual(*TestRequirement.get_reqs("pylib>=1.0,<2.0", "pylib<2.0,>=1.0"))

    def test_vcs_equality(self) -> None:
        self.assertEqual(*TestRequirement.get_reqs(
            "-e git://git.example.com/MyProject.git@da39a3ee#egg=MyProject",
            "-e git://git.example.com/MyProject.git@da39a3ee#egg=MyProject"
        ))

    def test_vcs_hash_inequality(self) -> None:
        self.assertNotEqual(*TestRequirement.get_reqs(
            "-e git://git.example.com/MyProject.git@123#egg=MyProject",
            "-e git://git.example.com/MyProject.git@abc#egg=MyProject"
        ))

    def test_editable_local_current_relative_path(self) -> None:
        a, b = TestRequirement.get_reqs('-e .', '-e .')
        self.assertEqual(a, b)

    def test_editable_local_with_path(self) -> None:
        a, b = TestRequirement.get_reqs('-e path/to/SomeProject', '-e path/to/SomeProject')
        self.assertEqual(a, b)

    def test_with_hash(self) -> None:
        a, b = TestRequirement.get_reqs(
            "http://pypi.python.org/packages/source/p/pytz/pytz-2016.4.tar.gz#md5=a3316cf3842ed0375ba5931914239d97",
            "http://pypi.python.org/packages/source/p/pytz/pytz-2016.4.tar.gz#md5=a3316cf3842ed0375ba5931914239d97"
        )
        self.assertEqual('a3316cf3842ed0375ba5931914239d97', a.hash_)
        self.assertEqual(a, b)
