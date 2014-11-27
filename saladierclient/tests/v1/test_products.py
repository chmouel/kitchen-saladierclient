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
import saladierclient.v1.products

PRODUCT = {
    "product1": ["1.0"],
    "product2": ["1.1", "1.0"],
}

CREATE_PRODUCT = {'contact': "blah@blah.com",
                  'name': 'product1',
                  'team': 'thebestone'}

fake_responses = {
    '/v1/products':
    {
        'GET': (
            {},
            {"products": [PRODUCT]},
        ),
        'POST': (
            {},
            CREATE_PRODUCT,
        ),
    },
}


class ProductsTest(testtools.TestCase):

    def setUp(self):
        super(ProductsTest, self).setUp()
        self.api = utils.FakeAPI(fake_responses)
        self.mgr = saladierclient.v1.products.ProductsManager(self.api)

    def test_products_list(self):
        products = self.mgr.list()
        expect = [
            ('GET', '/v1/products', {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertEqual(2, len(products))

    def test_create(self):
        product = self.mgr.create(**CREATE_PRODUCT)
        expect = [
            ('POST', '/v1/products', {}, CREATE_PRODUCT),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertTrue(product)
        self.assertEqual(product.name, CREATE_PRODUCT['name'])

    def test_create_invalid(self):
        self.assertRaises(exc.InvalidAttribute, self.mgr.create, foo='bar')
