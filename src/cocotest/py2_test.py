#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x6778b097

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
py2_filter, py2_hex, py2_map, py2_oct, py2_zip, py2_open, py2_range, py2_int, py2_chr, py2_str, py2_print, py2_input, py2_raw_input = filter, hex, map, oct, zip, open, range, int, chr, str, print, input, raw_input
_coconut_int, _coconut_long, _coconut_str, _coconut_bytearray, _coconut_print, _coconut_unicode, _coconut_raw_input = int, long, str, bytearray, print, unicode, raw_input
range, chr, str = xrange, unichr, unicode
from future_builtins import *
from io import open
class _coconut_metaint(type):
    def __instancecheck__(cls, inst):
        return isinstance(inst, (_coconut_int, _coconut_long))
class int(_coconut_int):
    """Python 3 int."""
    __metaclass__ = _coconut_metaint
    __slots__ = ()
class _coconut_metabytes(type):
    def __instancecheck__(cls, inst):
        return isinstance(inst, _coconut_str)
class bytes(_coconut_str):
    """Python 3 bytes."""
    __metaclass__ = _coconut_metabytes
    __slots__ = ()
    def __new__(cls, *args, **kwargs):
        """Python 3 bytes constructor."""
        return _coconut_str.__new__(cls, _coconut_bytearray(*args, **kwargs))
def print(*args, **kwargs):
    """Python 3 print."""
    return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
def input(*args, **kwargs):
    """Python 3 input."""
    return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
def raw_input(*args):
    """Raises NameError."""
    raise NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')

class __coconut__(object):
    """Built-in Coconut functions."""
    version = "0.3.6-post_dev"
    import imp, types, operator, functools, itertools, collections
    abc = collections
    object, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii, next = object, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii, next
    @staticmethod
    def igetitem(iterable, index):
        """Performs slicing on any iterable."""
        if isinstance(index, __coconut__.slice):
            return __coconut__.itertools.islice(iterable, index.start, index.stop, index.step)
        else:
            return __coconut__.next(__coconut__.itertools.islice(iterable, index, index+1))
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

def py2_test():
    """Performs Python2-specific tests."""
    assert py2_filter(__coconut__.functools.partial(__coconut__.operator.__gt__, 3), range(10)) == [0, 1, 2]
    assert py2_map(__coconut__.functools.partial(__coconut__.operator.__add__, 2), range(5)) == [2, 3, 4, 5, 6]
    assert py2_range(5) == [0, 1, 2, 3, 4]
    assert not isinstance(long(1), py2_int)
    assert py2_str(3) == b"3" == unicode(b"3")
