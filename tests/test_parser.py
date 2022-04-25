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

import builtins
import json
import warnings
from os import listdir
from os.path import dirname, isfile, join
from types import GeneratorType
from typing import Any
from unittest import TestCase

from requirements import parse
from requirements.requirement import Requirement


class TestParser(TestCase):
    _requirements_files_dir: str

    @classmethod
    def setUpClass(cls) -> None:
        cls._requirements_files_dir = join(dirname(__file__), 'reqfiles')

    def test_requirement_files(self) -> None:
        for fn in listdir(TestParser._requirements_files_dir):
            fp = join(TestParser._requirements_files_dir, fn)

            # skip ".expected" files
            if not isfile(fp) or not fp.endswith('.txt'):
                continue

            self._test_req_file(req_file=fn)

    def _test_req_file(self, req_file: str) -> None:
        fp = join(TestParser._requirements_files_dir, req_file)
        with open(fp) as req_fh:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                parsed = parse(req_fh)
                if 'fail' in req_file:
                    with self.assertRaises(ValueError):
                        list(map(lambda r: _requirement_dict(r=r), parsed))
                else:
                    with open(fp[:-4] + '.expected', 'r') as f2:
                        self.assertIsInstance(parsed, GeneratorType)
                        self.assertEqual(json.loads(f2.read()), list(map(lambda r: _requirement_dict(r=r), parsed)),
                                         msg=f'Failed on {fp}')


def _requirement_dict(r: Requirement) -> dict[str, Any]:
    d: dict[str, Any] = {}
    for k in r.__dict__:
        a = getattr(r, k)

        # Ignore any properties that don't being with _
        if not k.startswith('_'):
            continue

        # Strip off leading _
        new_k = k[1:]

        # If key would match a built-in name, remove the trailing _
        if new_k[:-1] in dir(builtins):
            new_k = new_k[:-1]

        if isinstance(a, (list, set)):
            # Enforce predictability
            a = sorted(a)
            d.update({
                new_k: list(map(lambda i: list(i) if isinstance(i, tuple) else i, a))  # type: ignore
            })
        else:
            d.update({
                new_k: a
            })
    return d
