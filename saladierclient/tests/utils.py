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

import copy
import datetime

import fixtures
import six
import testtools

from saladierclient.common import http


class BaseTestCase(testtools.TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.useFixture(fixtures.FakeLogger())


class FakeAPI(object):
    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def _request(self, method, url, headers=None, body=None):
        call = (method, url, headers or {}, body)
        self.calls.append(call)
        return self.responses[url][method]

    def raw_request(self, *args, **kwargs):
        response = self._request(*args, **kwargs)
        body_iter = http.ResponseBodyIterator(six.StringIO(response[1]))
        return FakeResponse(response[0]), body_iter

    def json_request(self, *args, **kwargs):
        response = self._request(*args, **kwargs)
        return FakeResponse(response[0]), response[1]


class FakeConnection(object):
    def __init__(self, response=None):
        self._response = response
        self._last_request = None

    def request(self, method, conn_url, **kwargs):
        self._last_request = (method, conn_url, kwargs)

    def setresponse(self, response):
        self._response = response

    def getresponse(self):
        return self._response


class FakeResponse(object):
    def __init__(self, headers, body=None, version=None, status=None,
                 reason=None):
        """Fake object to help testing.

        :param headers: dict representing HTTP response headers
        :param body: file-like object
        """
        self.headers = headers
        self.body = body
        self.version = version
        self.status = status
        self.reason = reason

    def getheaders(self):
        return copy.deepcopy(self.headers).items()

    def getheader(self, key, default):
        return self.headers.get(key, default)

    def read(self, amt):
        return self.body.read(amt)


class FakeServiceCatalog():
    def url_for(self, endpoint_type, service_type, attr=None,
                filter_value=None):
        if attr == 'region' and filter_value:
            return 'http://regionhost:6385/v1/f14b41234'
        else:
            return 'http://localhost:6385/v1/f14b41234'


class FakeKeystone():
    service_catalog = FakeServiceCatalog()
    timestamp = datetime.datetime.utcnow() + datetime.timedelta(days=5)

    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.auth_ref = {
            'token': {'expires': FakeKeystone.timestamp.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
                'id': 'd1a541311782870742235'}
        }
