#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xd11d438e

# Compiled with Coconut version 1.1.1-post_dev [Brontosaurus]

"""
Author: Evan Hubinger
License: Apache 2.0
Description: The Coconut test suite.
"""

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
