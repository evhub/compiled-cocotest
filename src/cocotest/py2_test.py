#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x6778b097

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
py2_filter, py2_hex, py2_map, py2_oct, py2_zip, py2_open, py2_range, py2_xrange, py2_int, py2_chr, py2_str, py2_print, py2_input, py2_raw_input = filter, hex, map, oct, zip, open, range, xrange, int, chr, str, print, input, raw_input
_coconut_NameError, _coconut_int, _coconut_long, _coconut_str, _coconut_unicode, _coconut_bytearray, _coconut_slice, _coconut_reversed, _coconut_isinstance, _coconut_iter, _coconut_len, _coconut_repr, _coconut_print, _coconut_xrange, _coconut_raw_input, _coconut_hasattr = NameError, int, long, str, unicode, bytearray, slice, reversed, isinstance, iter, len, repr, print, xrange, raw_input, hasattr
chr, str = unichr, unicode
from future_builtins import *
from io import open
class range(object):
    __doc__ = _coconut_xrange.__doc__
    __slots__ = ("_xrange",)
    __coconut_is_sliceable_iter__ = True
    def __init__(self, *args):
        self._xrange = _coconut_xrange(*args)
    def __iter__(self):
        return _coconut_iter(self._xrange)
    def __reversed__(self):
        return _coconut_reversed(self._xrange)
    def __len__(self):
        return _coconut_len(self._xrange)
    def __getitem__(self, index):
        if _coconut_isinstance(index, _coconut_slice):
            start, stop, step = index.start, index.stop, index.step
            if start is None:
                start = 0
            elif start < 0:
                start += _coconut_len(self._xrange)
            if stop is None:
                stop = _coconut_len(self._xrange)
            elif stop is not None and stop < 0:
                stop += _coconut_len(self._xrange)
            if step is None:
                step = 1
            return map(self._xrange.__getitem__, range(start, stop, step))
        else:
            return self._xrange[index]
    def __repr__(self):
        return _coconut_repr(self._xrange)[1:]
    def __reduce__(self):
        return (range, self._xrange.__reduce__()[1])
class _coconut_metaint(type):
    def __instancecheck__(cls, inst):
        return _coconut_isinstance(inst, (_coconut_int, _coconut_long))
class int(_coconut_int):
    __doc__ = _coconut_int.__doc__
    __metaclass__ = _coconut_metaint
    __slots__ = ()
class _coconut_metabytes(type):
    def __instancecheck__(cls, inst):
        return _coconut_isinstance(inst, _coconut_str)
class bytes(_coconut_str):
    __doc__ = _coconut_str.__doc__
    __metaclass__ = _coconut_metabytes
    __slots__ = ()
    def __new__(cls, *args, **kwargs):
        return _coconut_str.__new__(cls, _coconut_bytearray(*args, **kwargs))
def print(*args, **kwargs):
    if _coconut_hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
        return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
    else:
        return _coconut_print(*(_coconut_unicode(x).encode() for x in args), **kwargs)
def input(*args, **kwargs):
    if _coconut_hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
        return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
    else:
        return _coconut_raw_input(*args, **kwargs).decode()
print.__doc__, input.__doc__ = _coconut_print.__doc__, _coconut_raw_input.__doc__
def raw_input(*args):
    """Raises NameError."""
    raise _coconut_NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')
def xrange(*args):
    """Raises NameError."""
    raise _coconut_NameError('Coconut uses Python 3 "range" instead of Python 2 "xrange"')

class __coconut__(object):
    version = "0.3.6-post_dev"
    import imp, types, operator, functools, itertools, collections
    abc = collections
    IndexError, object, set, frozenset, tuple, list, dict, slice, len, iter, isinstance, getattr, ascii, next, range, hasattr, super, _map, _zip = IndexError, object, set, frozenset, tuple, list, dict, slice, len, iter, isinstance, getattr, ascii, next, range, hasattr, super, map, zip
    class MatchError(Exception):
        """Pattern-matching error."""
    class map(_map):
        __doc__ = map.__doc__
        __slots__ = ("_func", "_iters")
        __coconut_is_map__ = True
        def __new__(cls, function, *iterables):
            m = __coconut__._map.__new__(cls, function, *iterables)
            m._func, m._iters = function, iterables
            return m
    class zip(_zip):
        __doc__ = zip.__doc__
        __slots__ = ("_iters",)
        __coconut_is_zip__ = True
        def __new__(cls, *iterables):
            z = __coconut__._zip.__new__(cls, *iterables)
            z._iters = iterables
            return z
    class count(object):
        """count(start, step) returns an infinite iterator starting at start and increasing by step."""
        __slots__ = ("_start", "_step")
        __coconut_is_sliceable_iter__ = True
        def __init__(self, start=0, step=1):
            self._start, self._step = start, step
        def __iter__(self):
            while True:
                yield self._start
                self._start += self._step
        def __getitem__(self, index):
            if __coconut__.isinstance(index, __coconut__.slice) and (index.start is None or index.start >= 0) and (index.stop is not None and index.stop >= 0):
                return __coconut__.map(lambda x: self._start + x * self._step, __coconut__.range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
            elif index >= 0:
                return self._start + index * self._step
            else:
                raise __coconut__.IndexError("count indices must be positive")
        def __repr__(self):
            return "count(" + str(self._start) + ", " + str(self._step) + ")"
        def __reduce__(self):
            return (__coconut__.count, (self._start, self._step))
    @staticmethod
    def igetitem(iterable, index):
        if __coconut__.hasattr(iterable, "__coconut_is_map__") and iterable.__coconut_is_map__:
            if __coconut__.isinstance(index, __coconut__.slice):
                return __coconut__.map(iterable._func, *(__coconut__.igetitem(i, index) for i in iterable._iters))
            else:
                return iterable._func(*(__coconut__.igetitem(i, index) for i in iterable._iters))
        elif __coconut__.hasattr(iterable, "__coconut_is_zip__") and iterable.__coconut_is_zip__:
            if __coconut__.isinstance(index, __coconut__.slice):
                return __coconut__.zip(*(__coconut__.igetitem(i, index) for i in iterable._iters))
            else:
                return (__coconut__.igetitem(i, index) for i in iterable._iters)
        elif isinstance(iterable, __coconut__.range) or (__coconut__.hasattr(iterable, "__coconut_is_sliceable_iter__") and iterable.__coconut_is_sliceable_iter__):
            return iterable[index]
        elif __coconut__.hasattr(iterable, "__getitem__"):
            if __coconut__.isinstance(index, __coconut__.slice):
                return (x for x in iterable[index])
            else:
                return iterable[index]
        elif __coconut__.isinstance(index, __coconut__.slice):
            if (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
                return (x for x in __coconut__.tuple(iterable)[index])
            else:
                return __coconut__.itertools.islice(iterable, index.start, index.stop, index.step)
        elif index < 0:
            return __coconut__.collections.deque(iterable, maxlen=-index)[0]
        else:
            return __coconut__.next(__coconut__.itertools.islice(iterable, index, index + 1))
    @staticmethod
    def consume(iterable, keep_last=0):
        """Fully exhaust iterable and return the last keep_last elements."""
        return __coconut__.collections.deque(iterable, maxlen=keep_last)
    @staticmethod
    def recursive(func):
        """Decorates a function by optimizing it for tail recursion."""
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
        """Returns base data constructor of passed data type."""
        return __coconut__.functools.partial(__coconut__.super(data_type, data_type).__new__, data_type)

__coconut_version__, MatchError, map, zip, reduce, takewhile, dropwhile, tee, count, consume, recursive, datamaker = __coconut__.version, __coconut__.MatchError, __coconut__.map, __coconut__.zip, __coconut__.functools.reduce, __coconut__.itertools.takewhile, __coconut__.itertools.dropwhile, __coconut__.itertools.tee, __coconut__.count, __coconut__.consume, __coconut__.recursive, __coconut__.datamaker

# Compiled Coconut: ------------------------------------------------------------

def py2_test():
    """Performs Python2-specific tests."""
    assert py2_filter(__coconut__.functools.partial(__coconut__.operator.__gt__, 3), range(10)) == [0, 1, 2]
    assert py2_map(__coconut__.functools.partial(__coconut__.operator.__add__, 2), range(5)) == [2, 3, 4, 5, 6]
    assert py2_range(5) == [0, 1, 2, 3, 4]
    assert not isinstance(long(1), py2_int)
    assert py2_str(3) == b"3" == unicode(b"3")
