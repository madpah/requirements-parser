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

import json
import warnings
from os import listdir
from os.path import dirname, isfile, join
from types import GeneratorType
from unittest import TestCase

from requirements import parse


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

    def _test_req_file(self, req_file: str):
        fp = join(TestParser._requirements_files_dir, req_file)
        with open(fp) as req_fh:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                parsed = parse(req_fh)

                if 'fail' in req_file:
                    with self.assertRaises(ValueError):
                        list([dict(r) for r in parsed])
                else:
                    with open(fp[:-4] + '.expected', 'r') as f2:
                        self.assertIsInstance(parsed, GeneratorType)
                        self.assertEqual(json.loads(f2.read()), listify(dict(r) for r in parsed),
                                         msg=f'Failed on {fp}')


def listify(iterable: GeneratorType) -> list:
    out = []

    for item in iterable:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(item[key], (tuple, list)):
                    if key in ('extras', 'specs'):
                        # enforce predictability
                        item[key] = sorted(listify(value))
                        # item[key] = listify(value)
        elif isinstance(item, (tuple, list)):
            item = listify(item)
        out.append(item)
    return out
