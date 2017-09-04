#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x59fa947a

# Compiled with Coconut version 1.3.0-post_dev1 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

def py3_test():
    """Performs Python-3-specific tests."""
    x = 5
    assert x == 5
    def set_x(y):
        nonlocal x
        x = y
    set_x(3)
    assert x == 3
    def set_x_again(y):
        nonlocal x
        x = y
    set_x_again(10)
    assert x == 10
    assert {x: x for x in range(5)} == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    def head_tail(l):
        head, *tail = l
        return head, tail
    assert head_tail((f() for f in (lambda: 1, lambda: 2, lambda: 3))) == (1, [2, 3])
    class metaA(type):
        def __instancecheck__(cls, inst):
            return True
    class A(metaclass=metaA):
        pass
    assert isinstance(A(), A)
    assert isinstance("", A)
    assert isinstance(5, A)
    assert (tuple)(py_map(lambda x: x + 1, range(4))) == (1, 2, 3, 4)
    assert (tuple)(py_zip(range(3), range(3))) == ((0, 0), (1, 1), (2, 2))
    class B(*()):
        pass
    assert isinstance(B(), B)
    e = exec
    test = {}
    e("a=1", test)
    assert test["a"] == 1
    def keyword_only(*, a):
        return a
    assert keyword_only(a=10) == 10
    return True
