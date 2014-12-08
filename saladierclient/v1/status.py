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

CREATION_ATTRIBUTES = ['platform_id', 'product_version_id',
                       'status', 'logs_location']


class Status(base.Resource):
    def __repr__(self):
        return "<Status %s>" % self._info


class StatusManager(base.Manager):
    resource_class = Status
    _path = '/v1/status'

    def create(self, **kwargs):
        new = {}
        for (key, value) in kwargs.items():
            if key in CREATION_ATTRIBUTES:
                new[key] = value
            else:
                raise exc.InvalidAttribute("Invalid attribute: %s" % key)
        return self._create(self._path, new)
