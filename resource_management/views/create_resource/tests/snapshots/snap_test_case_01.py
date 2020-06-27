# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateResourceAPITestCase::test_case status'] = 200

snapshots['TestCase01CreateResourceAPITestCase::test_case body'] = {
    'Success Response': 'Successfully created a new resource'
}

snapshots['TestCase01CreateResourceAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '59',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01CreateResourceAPITestCase::test_case resource_id'] = 1

snapshots['TestCase01CreateResourceAPITestCase::test_case resource_name'] = 'string'

snapshots['TestCase01CreateResourceAPITestCase::test_case resource_item_name'] = 'string'

snapshots['TestCase01CreateResourceAPITestCase::test_case link'] = 'string'

snapshots['TestCase01CreateResourceAPITestCase::test_case description'] = 'string'

snapshots['TestCase01CreateResourceAPITestCase::test_case resource_image_url'] = 'string'
