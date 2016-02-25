#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

"""Built-in Coconut functions."""

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    import os as _coconut_os
    py2_filter, py2_hex, py2_map, py2_oct, py2_zip, py2_open, py2_range, py2_xrange, py2_int, py2_chr, py2_str, py2_print, py2_input, py2_raw_input = filter, hex, map, oct, zip, open, range, xrange, int, chr, str, print, input, raw_input
    _coconut_NameError, _coconut_int, _coconut_long, _coconut_str, _coconut_unicode, _coconut_bytearray, _coconut_slice, _coconut_reversed, _coconut_isinstance, _coconut_iter, _coconut_len, _coconut_repr, _coconut_print, _coconut_xrange, _coconut_raw_input = NameError, int, long, str, unicode, bytearray, slice, reversed, isinstance, iter, len, repr, print, xrange, raw_input
    chr, str = unichr, unicode
    from future_builtins import *
    from io import open
    class range(object):
        __doc__ = _coconut_xrange.__doc__
        __slots__ = ("_xrange",)
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
        return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
    def input(*args, **kwargs):
        return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
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
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    IndexError, object, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii, next, range, hasattr = IndexError, object, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii, next, range, hasattr
    class MatchError(Exception):
        """Pattern-matching error."""
    class map(map):
        __doc__ = map.__doc__
        __slots__ = ("_func", "_iters")
        def __new__(cls, function, *iterables):
            m = super(cls, cls).__new__(cls, function, *iterables)
            m._func, m._iters = function, iterables
            return m
    class zip(zip):
        __doc__ = zip.__doc__
        __slots__ = ("_iters",)
        def __new__(cls, *iterables):
            z = super(cls, cls).__new__(cls, *iterables)
            z._iters = iterables
            return z
    class count(object):
        """count(start, step) returns an infinite iterator starting at start and increasing by step."""
        __slots__ = ("_start", "_step")
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
            return (count, (self._start, self._step))
    @staticmethod
    def igetitem(iterable, index):
        if __coconut__.isinstance(iterable, __coconut__.map):
            if __coconut__.isinstance(index, __coconut__.slice):
                return __coconut__.map(iterable._func, *(__coconut__.igetitem(i, index) for i in iterable._iters))
            else:
                return iterable._func(*(__coconut__.igetitem(i, index) for i in iterable._iters))
        elif __coconut__.isinstance(iterable, __coconut__.zip):
            if __coconut__.isinstance(index, __coconut__.slice):
                return __coconut__.zip(*(__coconut__.igetitem(i, index) for i in iterable._iters))
            else:
                return (__coconut__.igetitem(i, index) for i in iterable._iters)
        elif __coconut__.isinstance(iterable, (__coconut__.range, __coconut__.count)):
            return iterable[index]
        elif __coconut__.hasattr(iterable, "__getitem__"):
            if __coconut__.isinstance(index, __coconut__.slice):
                return (x for x in iterable[index])
            else:
                return iterable[index]
        elif __coconut__.isinstance(index, __coconut__.slice):
            if (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0):
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
        return __coconut__.functools.partial(super(data_type, data_type).__new__, data_type)

__coconut_version__, MatchError, map, zip, reduce, takewhile, dropwhile, tee, count, consume, recursive, datamaker = __coconut__.version, __coconut__.MatchError, __coconut__.map, __coconut__.zip, __coconut__.functools.reduce, __coconut__.itertools.takewhile, __coconut__.itertools.dropwhile, __coconut__.itertools.tee, __coconut__.count, __coconut__.consume, __coconut__.recursive, __coconut__.datamaker
