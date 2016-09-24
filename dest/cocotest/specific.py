#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfc192df4

# Compiled with Coconut version 1.2.0 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
import __coconut__
_coconut_sys.path.remove(_coconut_file_path)
for name in dir(__coconut__):
    if name.startswith("_") and not name.startswith("__"):
        globals()[name] = getattr(__coconut__, name)

# Compiled Coconut: ------------------------------------------------------

from .util import mod

def non_py26_test():
    """Tests for any non-py26 version."""
    test = {}
    exec("a = 1", test)
    assert test["a"] == 1
    exec("a = 2", globals(), test)
    assert test["a"] == 2
    test = {}
    exec("b = mod(5, 3)", globals(), test)
    assert test["b"] == 2
    return True

def non_py32_test():
    """Tests for any non-py32 version."""
    assert {range(8): True}[range(8)]
    assert range(1, 2) == range(1, 2)
    assert range(1, 2) != range(3, 4)
