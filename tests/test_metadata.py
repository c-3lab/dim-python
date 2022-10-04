#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dim


def test_version():
    assert isinstance(dim.__version__, str)
