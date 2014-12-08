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

VERSION1_ID = "version1.0-xx-xx-xx"
VERSION1_NAME = "1.0"
VERSION1_DETAIL = {
    "ready_for_deploy": False,
    "version": VERSION1_NAME,
    "id": VERSION1_ID,
    "validated_on": []
}

VERSION2_ID = "version1.1-xx-xx-xx"
VERSION2_NAME = "1.1"
VERSION2_DETAIL = {
    "ready_for_deploy": False,
    "version": VERSION2_NAME,
    "id": VERSION2_ID,
    "validated_on": []
}

PRODUCT1_NAME = "product1"
PRODUCT1_ID = "product1-id-id-id"
PRODUCT1_TEAM = "team1"
PRODUCT1_CONTACT = "team@xx.org"
PRODUCT1_DETAIL = {
    "team": PRODUCT1_TEAM,
    "contact": PRODUCT1_CONTACT,
    "name": PRODUCT1_NAME,
    "id": PRODUCT1_ID,
    "versions": [VERSION1_DETAIL, VERSION2_DETAIL],
}

PRODUCT2_NAME = "product2"
PRODUCT2_ID = "product2-id-id-id"
PRODUCT2_TEAM = "team2"
PRODUCT2_CONTACT = "team2@xx.org"
PRODUCT2_DETAIL = {
    "team": PRODUCT2_TEAM,
    "contact": PRODUCT2_CONTACT,
    "name": PRODUCT2_NAME,
    "id": PRODUCT2_ID,
    "versions": [VERSION1_DETAIL]
}

PRODUCTS_LIST = {'products':
                 [PRODUCT1_DETAIL,
                  PRODUCT2_DETAIL]}

PLATFORM1_DETAIL = {'tenant_id': '0123456789',
                    'location': 'nowhere',
                    'contact': 'platform@contact.org',
                    'name': 'platform1',
                    'id': 'platform1-id-id-id'}
PLATFORMS_LIST = {'platforms': [PLATFORM1_DETAIL]}

SERVER_INFO = {
    'version': '0.0.1',
    'location': 'Paris',
    'provider': 'Tinrlopopin'
}

#
CREATE_PRODUCT = {'contact': "blah@blah.com",
                  'name': 'product1',
                  'team': 'thebestone'}

CREATE_SUBSCRIPTION = {'product_id': 'id-id-id-id',
                       'tenant_id': '100101'}

CREATE_PLATFORM = {'location': "Kurzistan",
                   'tenant_id': '0123456789',
                   'name': 'Platform1',
                   'contact': 'thebest@contactever'}

CREATE_PRODUCT_VERSIONS = {'product_id': '101010101-101001010',
                           'url': 'http://somewhereoutthere',
                           'version': '1.0'}
