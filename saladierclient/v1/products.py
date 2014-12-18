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

from saladierclient.common import base
from saladierclient import exc

CREATION_ATTRIBUTES = ['team', 'name', 'contact']


class Products(base.Resource):
    def __repr__(self):
        return "<Products %s>" % self._info


class ProductsManager(base.Manager):
    resource_class = Products

    @staticmethod
    def _path(path=None):
        return '/v1/products/' + path if path else '/v1/products'

    def create(self, **kwargs):
        new = {}
        for (key, value) in kwargs.items():
            if key in CREATION_ATTRIBUTES:
                new[key] = value
            else:
                raise exc.InvalidAttribute()
        return self._create(self._path(), new)

    def get(self, product_id, version=None):
        """Retrieve a specific product or a version."""
        path = product_id

        if version:
            path += "/%s" % version

        product = self._list(self._path(path))
        if product:
            return product[0]

    def list(self):
        """Retrieve a list of products."""
        products = self._list(self._path(), "products")
        return products

    def delete(self, product_id):
        return self._delete(
            self._path(product_id))
