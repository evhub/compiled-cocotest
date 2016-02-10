#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xc3c3c95f

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------
import sys as _coconut_sys

class __coconut__(object):
    """Built-in Coconut functions."""
    version = "0.3.6-post_dev"
    import imp, functools, operator, itertools, collections
    if _coconut_sys.version_info < (3,3):
        abc = collections
    else:
        import collections.abc as abc
    object, int, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii = object, int, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii
    @staticmethod
    def recursive(func):
        """Returns tail-call-optimized function."""
        state = [True, None] # toplevel, (args, kwargs)
        recurse = object()
        @__coconut__.functools.wraps(func)
        def tailed_func(*args, **kwargs):
            """Tail Recursion Wrapper."""
            if state[0]:
                state[0] = False
                try:
                    while True:
                        result = func(*args, **kwargs)
                        if result is recurse:
                            args, kwargs = state[1]
                            state[1] = None
                        else:
                            return result
                finally:
                    state[0] = True
            else:
                state[1] = args, kwargs
                return recurse
        return tailed_func
    @staticmethod
    def datamaker(data_type):
        """Returns base data constructor of data_type."""
        return __coconut__.functools.partial(super(data_type, data_type).__new__, data_type)
    @staticmethod
    def consume(iterable, keep_last=0):
        """Fully exhaust iterable and return the last keep_last elements."""
        return __coconut__.collections.deque(iterable, maxlen=keep_last)
    class MatchError(Exception):
        """Pattern-matching error."""

__coconut_version__ = __coconut__.version
reduce = __coconut__.functools.reduce
takewhile = __coconut__.itertools.takewhile
dropwhile = __coconut__.itertools.dropwhile
tee = __coconut__.itertools.tee
recursive = __coconut__.recursive
datamaker = __coconut__.datamaker
consume = __coconut__.consume
MatchError = __coconut__.MatchError

# Compiled Coconut: ------------------------------------------------------------

import sys

def py3_test():
    """Performs Python-3-specific tests."""
    def p1(x:int) -> int:
        return x + 1
    assert p1(2) == 3
    x = 5
    assert x == 5
    def set_x(y):
        nonlocal x
        x = y
    set_x(3)
    assert x == 3
    assert {x: x for x in range(5)} == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    def head_tail(l):
        head, *tail = l
        return head, tail
    assert head_tail((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2, lambda: 3))) == (1, [2, 3])
    class metaA(type):
        def __instancecheck__(cls, inst):
            return True
    class A(metaclass=metaA): pass
    assert isinstance(A(), A)
    assert isinstance("", A)
    assert isinstance(5, A)
