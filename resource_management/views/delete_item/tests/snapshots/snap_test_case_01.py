# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DeleteItemAPITestCase::test_case status'] = 200

snapshots['TestCase01DeleteItemAPITestCase::test_case body'] = {
    'Success Response': 'Successfully deletes the item_id'
}

snapshots['TestCase01DeleteItemAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '56',
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

snapshots['TestCase01DeleteItemAPITestCase::test_case is_item1_exists'] = False

snapshots['TestCase01DeleteItemAPITestCase::test_case is_item2_exists'] = False
