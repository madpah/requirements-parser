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

from typing import Tuple
from unittest import TestCase

from requirements.requirement import Requirement


class TestRequirement(TestCase):

    @staticmethod
    def get_reqs(requirement_1: str, requirement_2: str) -> Tuple[Requirement, Requirement]:
        return (Requirement.parse(requirement_1),
                Requirement.parse(requirement_2))

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

    def test_with_hash(self) -> None:
        a, b = TestRequirement.get_reqs(
            "http://pypi.python.org/packages/source/p/pytz/pytz-2016.4.tar.gz#md5=a3316cf3842ed0375ba5931914239d97",
            "http://pypi.python.org/packages/source/p/pytz/pytz-2016.4.tar.gz#md5=a3316cf3842ed0375ba5931914239d97"
        )
        self.assertEqual('a3316cf3842ed0375ba5931914239d97', a.hash_)
        self.assertEqual(a, b)
