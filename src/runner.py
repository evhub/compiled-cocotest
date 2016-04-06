#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x80e0463d

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

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

import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import cocotest
from cocotest.main import main

if __name__ == "__main__":
    main(cocotest.__doc__)
