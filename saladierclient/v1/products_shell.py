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
from saladierclient.openstack.common import cliutils
import saladierclient.v1.res_fields as res_fields


class Product(object):
    def __init__(self, name, versions):
        self.name = name
        self.versions = versions


def do_products_list(cc, args):
    """List products which are registered with the Saladier service."""
    fields = res_fields.PRODUCTS_FIELDS
    field_labels = res_fields.PRODUCTS_FIELDS_LABELS
    products = cc.products.list()

    # NOTE(chmou): this is hack cause we don't come back with the
    # standard output expected by apiclient
    dct = products[0].to_dict()
    ret = []
    for k in dct:
        versions = ", ".join(dct[k])
        ret.append(Product(k, versions))

    cliutils.print_list(ret, fields,
                        field_labels=field_labels,
                        sortby_index=None)
