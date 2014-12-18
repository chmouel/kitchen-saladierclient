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


def do_platforms_list(cc, args):
    """List registered platforms."""
    fields = res_fields.PLATFORMS_FIELDS
    field_labels = res_fields.PLATFORMS_FIELDS_LABELS
    platforms = cc.platforms.list()

    cliutils.print_list(platforms, fields,
                        field_labels=field_labels)


@cliutils.arg('name',
              metavar='<name>',
              help="Platform Name")
@cliutils.arg(
    'tenant_id',
    metavar='<tenant_id>',
    help='Tenant ID owner of that platform.')
@cliutils.arg(
    'contact',
    metavar='<contact>',
    help='Email contact of the team.')
@cliutils.arg(
    'location',
    metavar='<location>',
    help='Platform Location.')
def do_platform_create(cc, args):
    cc.platforms.create(
        contact=args.contact,
        name=args.name,
        tenant_id=args.tenant_id,
        location=args.location)
    # TODO(chmou): We'l need something better than that in the future
    print("CREATED")


@cliutils.arg('platform_id', metavar='<platform_id>',
              help="Platform ID")
def do_platform_delete(cc, args):
    """Delete a status."""
    cc.platforms.delete(args.platform_id)
    print("Platform ID %s has been deleted" % args.platform_id)
