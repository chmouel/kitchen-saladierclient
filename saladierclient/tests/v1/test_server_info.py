# -*- coding: utf-8 -*-
# Copyright (C) 2014 eNovance SAS <licensing@enovance.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import testtools

from saladierclient.tests import utils
from saladierclient.tests.v1 import fakes
import saladierclient.v1.products
import saladierclient.v1.server_info

fake_responses = {
    '/':
    {
        'GET': (
            {},
            fakes.SERVER_INFO,
        ),
    },
}


class ServerInfoTest(testtools.TestCase):

    def setUp(self):
        super(ServerInfoTest, self).setUp()
        self.api = utils.FakeAPI(fake_responses)
        self.mgr = saladierclient.v1.server_info.ServerInfoManager(self.api)

    def test_server_info_show(self):
        version = self.mgr.list()
        expect = [
            ('GET', '/', {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertDictEqual(fakes.SERVER_INFO,
                             version.to_dict())
        self.assertIs(saladierclient.v1.server_info.ServerInfo,
                      type(version))
