# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02DeleteItemAPITestCase::test_case status'] = 400

snapshots['TestCase02DeleteItemAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ID',
    'response': 'Id must be positive integer and not too be zero'
}

snapshots['TestCase02DeleteItemAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '116',
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

snapshots['TestCase02DeleteItemAPITestCase::test_case is_item1_exists'] = False

snapshots['TestCase02DeleteItemAPITestCase::test_case is_item2_exists'] = True
