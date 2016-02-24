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
    _coconut_isinstance, _coconut_int, _coconut_long, _coconut_str, _coconut_bytearray, _coconut_print, _coconut_unicode, _coconut_raw_input, _coconut_xrange, _coconut_slice, _coconut_reversed = isinstance, int, long, str, bytearray, print, unicode, raw_input, xrange, slice, reversed
    chr, str = unichr, unicode
    from future_builtins import *
    from io import open
    class range(object):
        """Python 3 range."""
        def __init__(self, *args):
            self._xrange = _coconut_xrange(*args)
        def __iter__(self):
            return iter(self._xrange)
        def __reversed__(self):
            return _coconut_reversed(self._xrange)
        def __len__(self):
            return len(self._xrange)
        def _slice(self, index):
            start, stop, step = index.start, index.stop, index.step
            if start is None:
                start = 0
            elif start < 0:
                start += len(self._xrange)
            if stop is None:
                stop = len(self._xrange)
            elif stop is not None and stop < 0:
                stop += len(self._xrange)
            if step is None:
                step = 1
            for i in _coconut_xrange(start, stop, step):
                yield self._xrange[i]
        def __getitem__(self, index):
            if _coconut_isinstance(index, _coconut_slice):
                return self._slice(index)
            else:
                return self._xrange[index]
    class _coconut_metaint(type):
        def __instancecheck__(cls, inst):
            return _coconut_isinstance(inst, (_coconut_int, _coconut_long))
    class int(_coconut_int):
        """Python 3 int."""
        __metaclass__ = _coconut_metaint
        __slots__ = ()
    class _coconut_metabytes(type):
        def __instancecheck__(cls, inst):
            return _coconut_isinstance(inst, _coconut_str)
    class bytes(_coconut_str):
        """Python 3 bytes."""
        __metaclass__ = _coconut_metabytes
        __slots__ = ()
        def __new__(cls, *args, **kwargs):
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

import imp, types, operator, functools, itertools, collections
if _coconut_sys.version_info < (3, 3):
    abc = collections
else:
    import collections.abc as abc

IndexError, object, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii, next, map, zip, range, hasattr = IndexError, object, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii, next, map, zip, range, hasattr

class imap(map):
    """Optimized iterator map."""
    __slots__ = ("_func", "_iters")
    def __new__(cls, function, *iterables):
        m = super(cls, cls).__new__(cls, function, *iterables)
        m._func, m._iters = function, iterables
        return m

class izip(zip):
    """Optimized iterator zip."""
    __slots__ = ("_iters",)
    def __new__(cls, *iterables):
        z = super(cls, cls).__new__(cls, *iterables)
        z._iters = iterables
        return z

class icount(itertools.count):
    """Optimized count iterator."""
    __slots__ = ("_start", "_step")
    def __new__(cls, start=0, step=1):
        c = super(cls, cls).__new__(cls, start, step)
        c._start = start
        c._step = step
        return c

def igetitem(iterable, index):
    """Performs slicing on any iterable."""
    if isinstance(iterable, itertools.count):
        if isinstance(index, slice) and (index.start is None or index.start >= 0) and (index.stop is not None and index.stop >= 0):
            return imap(lambda x: iterable._start + x * iterable._step, range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
        elif index >= 0:
            return iterable._start + index * iterable._step
        else:
            raise IndexError("count indices must be greater than 0")
    elif isinstance(iterable, imap):
        if isinstance(index, slice):
            return imap(iterable._func, *(igetitem(i, index) for i in iterable._iters))
        else:
            return iterable._func(*(igetitem(i, index) for i in iterable._iters))
    elif isinstance(iterable, izip):
        if isinstance(index, slice):
            return izip(*(igetitem(i, index) for i in iterable._iters))
        else:
            return (igetitem(i, index) for i in iterable._iters)
    elif isinstance(iterable, range):
        return iterable[index]
    elif hasattr(iterable, "__getitem__"):
        return (x for x in iterable[index])
    elif isinstance(index, slice):
        if (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0):
            return (x for x in tuple(iterable)[index])
        else:
            return itertools.islice(iterable, index.start, index.stop, index.step)
    elif index < 0:
        return collections.deque(iterable, maxlen=-index)[0]
    else:
        return next(itertools.islice(iterable, index, index + 1))

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
