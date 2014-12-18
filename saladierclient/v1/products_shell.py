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


def do_product_list(cc, args):
    """List products which are registered with the Saladier service."""
    fields = res_fields.PRODUCTS_FIELDS
    field_labels = res_fields.PRODUCTS_FIELDS_LABELS
    products = cc.products.list()

    cliutils.print_list(products, fields,
                        field_labels=field_labels)


@cliutils.arg('name',
              metavar='<name>',
              help="Product Name")
@cliutils.arg(
    'team',
    metavar='<team>',
    help='Team name taking care of this product.')
@cliutils.arg(
    'contact',
    metavar='<contact>',
    help='Email contact of the team.')
def do_product_create(cc, args):
    cc.products.create(
        contact=args.contact,
        name=args.name,
        team=args.team)
    # TODO(chmou): We'l need something better than that in the future
    print("CREATED")


@cliutils.arg('name',
              metavar='<product_name>',
              help="Product Name")
@cliutils.arg(
    '-v',  # TODO(chmou): rename to --version, stupid  apiclient is buggy atm
    metavar='<version>',
    help='Show only this version.')
def do_product_show(cc, args):
    """Show product information."""
    product = cc.products.get(args.name, version=args.v)

    # TODO(chmou): Separate the logic between product_show_version and
    # product_show in two different function to not have this function becoming
    # a spaghetti code.
    if args.v:
        ret = product.to_dict()
        cliutils.print_dict(ret, wrap=72)
        return

    versions = "\n".join(["%s:%s" % (v['version'], v['id'])
                         for v in product.versions])

    ret = dict(
        product_name=args.name,
        team=product.team,
        Contact=product.contact,
        versions=versions)
    cliutils.print_dict(ret, wrap=72)


@cliutils.arg('product_id', metavar='<product_id>',
              help="Product ID")
def do_product_delete(cc, args):
    """Delete a status."""
    cc.products.delete(product_id=args.product_id)
    print ("Status of product_id: %s has been deleted" %
           args.product_id)
