#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xda5adc4f

# Compiled with Coconut version 1.2.3-post_dev12 [Colonel]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_back_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------------

def py2_test():
    """Performs Python2-specific tests."""
    assert py_filter(_coconut.functools.partial(_coconut.operator.gt, 3), range(10)) == [0, 1, 2]
    assert py_map(_coconut.functools.partial(_coconut.operator.add, 2), range(5)) == [2, 3, 4, 5, 6]
    assert py_range(5) == [0, 1, 2, 3, 4]
    assert not isinstance(long(1), py_int)
    assert py_str(3) == b"3" == unicode(b"3")
    return True
