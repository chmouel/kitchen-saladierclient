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


@cliutils.arg('product_id', metavar='<id>', help="Product ID")
@cliutils.arg('tenant_id', metavar='<tenant_id>',
              help='TenantID subscribed to this product.')
def do_subscription_create(cc, args):
    cc.subscriptions.create(
        product_id=args.product_id,
        tenant_id=args.tenant_id)
    # TODO(chmou): We'l need something better than that in the future
    print("CREATED")


@cliutils.arg('product_id', metavar='<id>', help="Product ID")
@cliutils.arg('tenant_id', metavar='<tenant_id>',
              help='TenantID subscribed to this product.')
def do_subscription_delete(cc, args):
    cc.subscriptions.delete(
        product_id=args.product_id,
        tenant_id=args.tenant_id)
    print ("Status from product_id: %s tenant_id: %s"
           " has been deleted" % (
               args.product_id,
               args.tenant_id))
