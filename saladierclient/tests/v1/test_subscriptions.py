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
import saladierclient.v1.subscriptions


fake_responses = {
    '/v1/subscriptions':
    {
        'POST': (
            {},
            None,
        ),
    },
}


class SubscriptionsTest(testtools.TestCase):

    def setUp(self):
        super(SubscriptionsTest, self).setUp()
        self.api = utils.FakeAPI(fake_responses)
        self.mgr = saladierclient.v1.subscriptions.SubscriptionsManager(
            self.api)

    def test_create(self):
        subscription = self.mgr.create(**fakes.CREATE_SUBSCRIPTION)
        expect = [
            ('POST',
             '/v1/subscriptions',
             {},
             fakes.CREATE_SUBSCRIPTION),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertIsNone(subscription)

    def test_create_invalid(self):
        self.assertRaises(exc.InvalidAttribute, self.mgr.create, foo='bar')
