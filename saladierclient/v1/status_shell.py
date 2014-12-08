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
