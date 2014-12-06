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
from saladierclient.v1 import res_fields


@cliutils.arg('platform_id', metavar='<platform_id>',
              help="Platform ID")
@cliutils.arg('product_version_id', metavar='<product_version_id>',
              help="Product Version ID")
@cliutils.arg('status', metavar='<status>', help="Status")
@cliutils.arg('logs_location', metavar='<logs_location>', help="Logs Location")
def do_status_create(cc, args):
    cc.status.create(
        platform_id=args.platform_id,
        product_version_id=args.product_version_id,
        logs_location=args.logs_location,
        status=args.status)
    # TODO(chmou): We'l need something better than that in the future
    print("CREATED")


@cliutils.arg('platform_id', metavar='<platform_id>',
              help="Platform ID")
@cliutils.arg('product_version_id', metavar='<product_version_id>',
              help="Product Version ID")
def do_status_show(cc, args):
    status = cc.status.get(
        platform_id=args.platform_id,
        product_version_id=args.product_version_id)
    data = dict([(f, getattr(status, f, ''))
                 for f in res_fields.STATUS_FIELDS])
    cliutils.print_dict(data, wrap=72)


@cliutils.arg('platform_id', metavar='<platform_id>',
              help="Platform ID")
@cliutils.arg('product_version_id', metavar='<product_version_id>',
              help="Product Version ID")
@cliutils.arg(
    'attributes',
    metavar='<path=value>',
    nargs='+',
    action='append',
    default=[],
    help="Attributes to add/replace or remove "
         "(only PATH is necessary on remove)")
def do_status_update(cc, args):
    """Update a status."""

    old = cc.status.get(args.platform_id, args.product_version_id)
    old_dict = old.to_dict()
    new_dict = old_dict.copy()
    new_dict.update(dict([x.split("=") for x in args.attributes[0]]))

    # TODO(chmou): detect if there was an update to do,
    cc.status.update(new_dict)

    # TODO(chmou): we need to have a redirect on PUT to show the newly changed
    # resource
    status = cc.status.get(args.platform_id, args.product_version_id)
    data = dict([(f, getattr(status, f, ''))
                 for f in res_fields.STATUS_FIELDS])
    cliutils.print_dict(data, wrap=72)
