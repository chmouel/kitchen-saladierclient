# -*- coding: utf-8 -*-
#
# Copyright 2013 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from saladierclient.common import utils
from saladierclient import exc
from saladierclient.tests import utils as test_utils


class CommonParamsForListTest(test_utils.BaseTestCase):
    def setUp(self):
        super(CommonParamsForListTest, self).setUp()
        self.args = mock.Mock(marker=None, limit=None,
                              sort_key=None, sort_dir=None)
        self.args.detail = False
        self.expected_params = {'detail': False}

    def test_nothing_set(self):
        self.assertEqual(self.expected_params,
                         utils.common_params_for_list(self.args, [], []))

    def test_marker_and_limit(self):
        self.args.marker = 'foo'
        self.args.limit = 42
        self.expected_params.update({'marker': 'foo', 'limit': 42})
        self.assertEqual(self.expected_params,
                         utils.common_params_for_list(self.args, [], []))

    def test_invalid_limit(self):
        self.args.limit = -42
        self.assertRaises(exc.CommandError,
                          utils.common_params_for_list,
                          self.args, [], [])

    def test_sort_key_and_sort_dir(self):
        self.args.sort_key = 'field'
        self.args.sort_dir = 'desc'
        self.expected_params.update({'sort_key': 'field', 'sort_dir': 'desc'})
        self.assertEqual(self.expected_params,
                         utils.common_params_for_list(self.args,
                                                      ['field'],
                                                      []))

    def test_sort_key_allows_label(self):
        self.args.sort_key = 'Label'
        self.expected_params.update({'sort_key': 'field'})
        self.assertEqual(self.expected_params,
                         utils.common_params_for_list(self.args,
                                                      ['field', 'field2'],
                                                      ['Label', 'Label2']))

    def test_sort_key_invalid(self):
        self.args.sort_key = 'something'
        self.assertRaises(exc.CommandError,
                          utils.common_params_for_list,
                          self.args,
                          ['field', 'field2'],
                          [])

    def test_sort_dir_invalid(self):
        self.args.sort_dir = 'something'
        self.assertRaises(exc.CommandError,
                          utils.common_params_for_list,
                          self.args,
                          [],
                          [])

    def test_detail(self):
        self.args.detail = True
        self.expected_params['detail'] = True
        self.assertEqual(self.expected_params,
                         utils.common_params_for_list(self.args, [], []))


class CommonFiltersTest(test_utils.BaseTestCase):
    def test_limit(self):
        result = utils.common_filters(limit=42)
        self.assertEqual(['limit=42'], result)

    def test_limit_0(self):
        result = utils.common_filters(limit=0)
        self.assertEqual([], result)

    def test_other(self):
        for key in ('marker', 'sort_key', 'sort_dir'):
            result = utils.common_filters(**{key: 'test'})
            self.assertEqual(['%s=test' % key], result)
