# -*- coding: utf-8 -*-
#
# Copyright 2013 Hewlett-Packard Development Company, L.P.
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

from saladierclient.common import base
from saladierclient import exc

CREATION_ATTRIBUTES = ['team', 'name', 'contact']


class Products(base.Resource):
    def __repr__(self):
        return "<Products %s>" % self._info


class Product(object):
    def __init__(self, name, versions):
        self.name = name
        self.versions = versions


class ProductsManager(base.Manager):
    resource_class = Products

    @staticmethod
    def _path(product_name=None):
        return '/v1/products/%s' % id if product_name else '/v1/products'

    def list(self):
        """Retrieve a list of products."""
        ret = []
        products = self._list(self._path(''), "products")

        # NOTE(chmou): this is hack cause we don't come back with the
        # standard output expected by apiclient
        if products:
            dct = products[0].to_dict()
            for k in dct:
                ret.append(Product(k, dct[k]))
        return ret

    def create(self, **kwargs):
        new = {}
        for (key, value) in kwargs.items():
            if key in CREATION_ATTRIBUTES:
                new[key] = value
            else:
                raise exc.InvalidAttribute()
        return self._create(self._path(), new)
