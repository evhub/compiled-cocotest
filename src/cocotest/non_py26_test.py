#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x45b2c590

# Compiled with Coconut version 1.1.1-post_dev [Brontosaurus]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
import __coconut__
_coconut_sys.path.remove(_coconut_file_path)
for name in dir(__coconut__):
    if not name.startswith("__"):
        globals()[name] = getattr(__coconut__, name)

# Compiled Coconut: ------------------------------------------------------

def non_py26_test():
    """Tests for any non-py26 version."""
    test = {}
    exec("a = 1", test)
    assert test["a"] == 1
    exec("a = 2", globals(), test)
    assert test["a"] == 2
