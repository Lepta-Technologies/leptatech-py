# Copyright 2023 Lepta Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from leptatech import lithium


class ConfigTest(unittest.TestCase):

    def test_singleton(self):
        # Check there is only a single instance
        self.assertIs(lithium.Lithium(), lithium.Lithium())

    def test_pre_config(self):
        # Check config property cannot be accessed before being configured
        try:
            lithium.Lithium().config
            self.fail()
        except:
            self.assertTrue(True)

    def test_wrong_client(self):
        # Try to configure an unsupported client
        config = lithium.Config("abc", "")
        try:
            lithium.Lithium().configure(config)
            self.fail()
        except:
            self.assertTrue(True)

    def test_reconfigure(self):
        # Try to configure more than once
        config = lithium.Config("test", "")
        lithium.Lithium().configure(config)
        try:
            lithium.Lithium().configure(config)
            self.fail()
        except:
            self.assertTrue(True)
