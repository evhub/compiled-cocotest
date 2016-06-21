#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xb850d9f

# Compiled with Coconut version 1.0.0-post_dev [Albatross]

"""
Author: Evan Hubinger
License: Apache 2.0
Description: The Coconut test suite.
"""

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
import __coconut__
_coconut_sys.path.remove(_coconut_file_path)
for name in dir(__coconut__):
    if not name.startswith("__"):
        globals()[name] = getattr(__coconut__, name)

# Compiled Coconut: ------------------------------------------------------------
