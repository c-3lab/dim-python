#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import raises
from dim import Locker
from dim.locker._dim_json import _DimJson


def test_start_with_empty(tmpdir):
    with raises(FileNotFoundError):
        Locker(directory=tmpdir, create_if_missing=False)
    # Write dim.json
    locker_empty = Locker(directory=tmpdir, create_if_missing=True)
    assert locker_empty.defined == _DimJson().to_dict()
    # Read exist dim.json
    locker = Locker(directory=tmpdir, create_if_missing=False)
    assert locker == locker_empty
