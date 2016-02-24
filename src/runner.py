#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xab75863b

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys, os.path as _coconut_sys, _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
if _coconut_sys.version_info() < (3,):
    from __coconut__ import py2_filter, py2_hex, py2_map, py2_oct, py2_zip, py2_open, py2_range, py2_xrange, py2_int, py2_chr, py2_str, py2_print, py2_input, py2_raw_input, ascii, filter, hex, oct, open, range, int, chr, str, print, input, bytes
from __coconut__ import __coconut__, __coconut_version__, map, zip, reduce, takewhile, dropwhile, tee, count, recursive, datamaker, consume, MatchError
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------------

import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import cocotest
from cocotest.main import main

main(cocotest.__doc__)
