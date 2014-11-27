# -*- coding: utf-8 -*-
#
# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
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

from saladierclient.common import http
from saladierclient.v1 import platforms
from saladierclient.v1 import product_version
from saladierclient.v1 import products
from saladierclient.v1 import subscriptions
from saladierclient.v1 import version


class Client(object):
    """Client for the Saladier v1 API.

    :param string endpoint: A user-supplied endpoint URL for the ironic
                            service.
    :param function token: Provides token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the Saladier v1 API."""
        self.http_client = http._construct_http_client(*args, **kwargs)
        self.version = version.VersionManager(self.http_client)

        self.products = products.ProductsManager(self.http_client)
        self.product_versions = product_version.ProductVersionManager(
            self.http_client)
        self.platforms = platforms.PlatformsManager(self.http_client)
        self.subscriptions = subscriptions.SubscriptionsManager(
            self.http_client)
