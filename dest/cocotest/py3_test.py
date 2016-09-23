#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2474872a

# Compiled with Coconut version 1.1.1-post_dev [Brontosaurus]

# Coconut Header: --------------------------------------------------------

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

def py3_test():
    """Performs Python-3-specific tests."""
    def p1(x: int) -> int:
        return x + 1
    assert p1(2) == 3
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
    assert head_tail((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2, lambda: 3))) == (1, [2, 3])
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
