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

from saladierclient import exc
from saladierclient.tests import utils
from saladierclient.tests.v1 import fakes
import saladierclient.v1.status

fake_responses = {
    '/v1/status':
    {
        'POST': (
            {},
            fakes.CREATE_STATUS_PRODUCT1,
        ),
    },
    '/v1/status/PLATFORM_ID/PRODUCT_ID':
    {
        'GET': (
            {},
            fakes.CREATE_STATUS_PRODUCT1,
        )
    }
}


class StatusTest(testtools.TestCase):

    def setUp(self):
        super(StatusTest, self).setUp()
        self.api = utils.FakeAPI(fake_responses)
        self.mgr = saladierclient.v1.status.StatusManager(self.api)

    def test_create(self):
        status = self.mgr.create(**fakes.CREATE_STATUS_PRODUCT1)
        expect = [
            ('POST', '/v1/status', {}, fakes.CREATE_STATUS_PRODUCT1),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertTrue(status)
        self.assertDictEqual(fakes.CREATE_STATUS_PRODUCT1, status.to_dict())

    def test_get(self):
        url = '/v1/status/%s/%s' % (
            fakes.CREATE_STATUS_PRODUCT1['platform_id'],
            fakes.CREATE_STATUS_PRODUCT1['product_version_id'])

        fake_responses[url] = (
            fake_responses['/v1/status/PLATFORM_ID/PRODUCT_ID'])

        status = self.mgr.get(
            fakes.CREATE_STATUS_PRODUCT1['platform_id'],
            fakes.CREATE_STATUS_PRODUCT1['product_version_id'])
        expect = [
            ('GET', url, {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertDictEqual(fakes.CREATE_STATUS_PRODUCT1, status.to_dict())

    def test_create_invalid(self):
        self.assertRaises(exc.InvalidAttribute, self.mgr.create, foo='bar')
