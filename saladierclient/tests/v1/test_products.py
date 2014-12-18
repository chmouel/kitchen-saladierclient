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
import saladierclient.v1.products


fake_responses = {
    '/v1/products':
    {
        'GET': (
            {},
            fakes.PRODUCTS_LIST,
        ),
        'POST': (
            {},
            fakes.CREATE_PRODUCT,
        ),
    },
    '/v1/products/product1':
    {
        'GET': (
            {},
            fakes.PRODUCT1_DETAIL,
        ),
        'DELETE': (
            {},
            None,
        ),
    },
    '/v1/products/product1/1.0':
    {
        'GET': (
            {},
            fakes.VERSION1_DETAIL,
        ),
    },
    '/v1/products/none':
    {
        'GET': (
            {},
            {},
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

    def test_products_get(self):
        name = 'product1'
        product = self.mgr.get(name)
        expect = [
            ('GET', '/v1/products/' + name, {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertDictEqual(fakes.PRODUCT1_DETAIL, product.to_dict())

    def test_products_get_version(self):
        name = 'product1'
        version = '1.0'
        product = self.mgr.get(name, version)
        expect = [
            ('GET', '/v1/products/' + name + "/" + version, {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertDictEqual(fakes.VERSION1_DETAIL,
                             product.to_dict())

    def test_products_get_none(self):
        name = 'none'
        product = self.mgr.get(name)
        expect = [
            ('GET', '/v1/products/' + name, {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertIsNone(product)

    def test_create(self):
        product = self.mgr.create(**fakes.CREATE_PRODUCT)
        expect = [
            ('POST', '/v1/products', {}, fakes.CREATE_PRODUCT),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertTrue(product)
        self.assertEqual(product.name, fakes.CREATE_PRODUCT['name'])

    def test_create_invalid(self):
        self.assertRaises(exc.InvalidAttribute, self.mgr.create, foo='bar')

    def test_delete(self):
        url = '/v1/products/' + fakes.PRODUCT1_NAME

        delete = self.mgr.delete(fakes.PRODUCT1_NAME)
        expect = [
            ('DELETE', url, {}, None),
        ]
        self.assertEqual(expect, self.api.calls)
        self.assertIsNone(delete)
