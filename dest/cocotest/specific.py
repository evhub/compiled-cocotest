#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x989dfc94

# Compiled with Coconut version 1.4.1 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

if _coconut_sys.version_info < (2, 7):  # type: ignore
    from StringIO import StringIO  # type: ignore
else:  # type: ignore
    from io import StringIO  # type: ignore

from .util import mod  # NOQA

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
    assert 5 .bit_length() == 3
    return True

def non_py32_test():
    """Tests for any non-py32 version."""
    assert {range(8): True}[range(8)]
    assert range(1, 2) == range(1, 2)
    assert range(1, 2) != range(3, 4)
    fakefile = StringIO()
    print("herpaderp", file=fakefile, flush=True)
    assert fakefile.getvalue() == "herpaderp\n"
