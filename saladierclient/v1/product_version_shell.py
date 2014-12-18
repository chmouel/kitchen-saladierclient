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


@cliutils.arg('product', metavar='<id>',
              help="Product ID")
@cliutils.arg(
    'url',
    metavar='<url>',
    help='Product version URL.')
@cliutils.arg(
    'version',
    metavar='<version>',
    help='Version number.')
def do_product_versions_create(cc, args):
    """Create a product version association."""
    cc.product_versions.create(
        product_id=args.product,
        url=args.url,
        version=args.version)
    # TODO(chmou): We'l need something better than that in the future
    print("CREATED")


@cliutils.arg('product_id', metavar='<product_id>',
              help="Product ID")
@cliutils.arg('version', metavar='<version>',
              help="Version string")
def do_product_versions_delete(cc, args):
    """Delete a product version association."""
    cc.product_versions.delete(
        product_id=args.product_id,
        version=args.version)
    print ("Product version product_id: %s version: %s"
           " has been deleted" % (
               args.product_id,
               args.version))
