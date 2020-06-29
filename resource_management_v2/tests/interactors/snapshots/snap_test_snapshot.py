# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_mything gpg_response'] = 2

snapshots['test_sum summation'] = 3

snapshots['test_sum_with_floats floats_summation'] = 3.5

snapshots['test_sum_with_negative_nums negative_summation'] = -1

snapshots['test_sum_with3_possibilities summation'] = 3

snapshots['test_sum_with3_possibilities floats_summation'] = 3.5

snapshots['test_sum_with3_possibilities negative_summation'] = -1
