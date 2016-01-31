#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

"""Built-in Coconut functions."""

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    import os as _coconut_os    
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

version = "0.3.6-post_dev"

import imp, functools, operator, itertools, collections
try:
    import collections.abc as abc
except ImportError:
    abc = collections

object, int, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii = object, int, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii

def recursive(func):
    """Returns tail-call-optimized function."""
    state = [True, None] # toplevel, (args, kwargs)
    recurse = object()
    @functools.wraps(func)
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

def datamaker(data_type):
    """Returns base data constructor of data_type."""
    return functools.partial(super(data_type, data_type).__new__, data_type)

def consume(iterable, keep_last=0):
    """Fully exhaust iterable and return the last keep_last elements."""
    return collections.deque(iterable, maxlen=keep_last)

class MatchError(Exception):
    """Pattern-matching error."""
