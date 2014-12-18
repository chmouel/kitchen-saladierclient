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
import saladierclient.v1.platforms

fake_responses = {
    '/v1/platforms':
    {
        'GET': (
            {},
            {"platforms": [fakes.CREATE_PLATFORM]},
        ),
        'POST': (
            {},
            fakes.CREATE_PLATFORM,
        ),
    },
    '/v1/platforms/PLATFORM_ID':
    {
        'DELETE': (
            {},
            None,
        ),
    },
}


class PlatformsTest(testtools.TestCase):

    def setUp(self):
        super(PlatformsTest, self).setUp()
        self.api = utils.FakeAPI(fake_responses)
        self.mgr = saladierclient.v1.platforms.PlatformsManager(self.api)

    def test_list(self):
        platforms = self.mgr.list()
        expect = [
            ('GET', '/v1/platforms', {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertEqual(1, len(platforms))
        self.assertIs(saladierclient.v1.platforms.Platform,
                      type(platforms[0]))
        self.assertDictEqual(fakes.CREATE_PLATFORM,
                             platforms[0].to_dict())
        self.assertRegexpMatches(repr(platforms[0]), "Platform1")

    def test_create(self):
        platform = self.mgr.create(**fakes.CREATE_PLATFORM)
        expect = [
            ('POST', '/v1/platforms', {}, fakes.CREATE_PLATFORM),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertTrue(platform)
        self.assertDictEqual(fakes.CREATE_PLATFORM, platform.to_dict())

    def test_create_invalid(self):
        self.assertRaises(exc.InvalidAttribute, self.mgr.create, foo='bar')

    def test_delete(self):
        url = '/v1/platforms/%s' % (fakes.PLATFORM1_DETAIL['id'])
        fake_responses[url] = (
            fake_responses['/v1/platforms/PLATFORM_ID'])
        delete = self.mgr.delete(fakes.PLATFORM1_DETAIL['id'])
        expect = [
            ('DELETE', url, {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertIsNone(delete)
