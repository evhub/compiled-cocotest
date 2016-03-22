#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

"""Built-in Coconut functions."""

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    import os as _coconut_os
    py2_chr, py2_filter, py2_hex, py2_input, py2_int, py2_map, py2_oct, py2_open, py2_print, py2_range, py2_raw_input, py2_str, py2_xrange, py2_zip = chr, filter, hex, input, int, map, oct, open, print, range, raw_input, str, xrange, zip
    _coconut_int, _coconut_long, _coconut_print, _coconut_raw_input, _coconut_str, _coconut_unicode, _coconut_xrange = int, long, print, raw_input, str, unicode, xrange
    from future_builtins import *
    chr, str = unichr, unicode
    from io import open
    class range(object):
        __slots__ = ("_xrange",)
        __doc__ = _coconut_xrange.__doc__
        __coconut_is_lazy__ = True
        def __init__(self, *args):
            self._xrange = _coconut_xrange(*args)
        def __iter__(self):
            return __coconut__.iter(self._xrange)
        def __reversed__(self):
            return __coconut__.reversed(self._xrange)
        def __len__(self):
            return __coconut__.len(self._xrange)
        def __getitem__(self, index):
            if __coconut__.isinstance(index, __coconut__.slice):
                start, stop, step = index.start, index.stop, index.step
                if start is None:
                    start = 0
                elif start < 0:
                    start += __coconut__.len(self._xrange)
                if stop is None:
                    stop = __coconut__.len(self._xrange)
                elif stop is not None and stop < 0:
                    stop += __coconut__.len(self._xrange)
                if step is None:
                    step = 1
                return __coconut__.map(self._xrange.__getitem__, self.__class__(start, stop, step))
            else:
                return self._xrange[index]
        def __repr__(self):
            return __coconut__.repr(self._xrange)[1:]
        def __reduce_ex__(self, protocol):
            return (self.__class__,) + self._xrange.__reduce_ex__(protocol)[1:]
    class int(_coconut_int):
        __slots__ = ()
        __doc__ = _coconut_int.__doc__
        class __metaclass__(type):
            def __instancecheck__(cls, inst):
                return __coconut__.isinstance(inst, (_coconut_int, _coconut_long))
    class bytes(_coconut_str):
        __slots__ = ()
        __doc__ = _coconut_str.__doc__
        class __metaclass__(type):
            def __instancecheck__(cls, inst):
                return __coconut__.isinstance(inst, _coconut_str)
        def __new__(cls, *args, **kwargs):
            return _coconut_str.__new__(cls, __coconut__.bytearray(*args, **kwargs))
    def print(*args, **kwargs):
        if __coconut__.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
            return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
        else:
            return _coconut_print(*(_coconut_unicode(x).encode() for x in args), **kwargs)
    def input(*args, **kwargs):
        if __coconut__.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
            return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
        else:
            return _coconut_raw_input(*args, **kwargs).decode()
    print.__doc__, input.__doc__ = _coconut_print.__doc__, _coconut_raw_input.__doc__
    def raw_input(*args):
        """Raises NameError."""
        raise __coconut__.NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')
    def xrange(*args):
        """Raises NameError."""
        raise __coconut__.NameError('Coconut uses Python 3 "range" instead of Python 2 "xrange"')
    if _coconut_sys.version_info < (2, 7):
        import functools as _coconut_functools, copy_reg as _coconut_copy_reg
        def _coconut_new_partial(func, args, keywords):
            return _coconut_functools.partial(func, *(args if args is not None else ()), **(keywords if keywords is not None else {}))
        _coconut_copy_reg.constructor(_coconut_new_partial)
        def _coconut_reduce_partial(self):
            return (_coconut_new_partial, (self.func, self.args, self.keywords))
        _coconut_copy_reg.pickle(_coconut_functools.partial, _coconut_reduce_partial)
else:
    py3_map, py3_zip = map, zip

class __coconut__(object):
    version = "0.3.6-post_dev"
    import collections, functools, imp, itertools, operator, types
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    IndexError, NameError, _map, _zip, bytearray, dict, frozenset, getattr, hasattr, isinstance, iter, len, list, min, next, object, range, repr, reversed, set, slice, super, tuple = IndexError, NameError, map, zip, bytearray, dict, frozenset, getattr, hasattr, isinstance, iter, len, list, min, next, object, range, repr, reversed, set, slice, super, tuple
    class MatchError(Exception):
        """Pattern-matching error."""
    class zip(_zip):
        __doc__ = zip.__doc__
        __slots__ = ("_iters",)
        __coconut_is_lazy__ = True
        def __new__(cls, *iterables):
            new_zip = __coconut__._zip.__new__(cls, *iterables)
            new_zip._iters = iterables
            return new_zip
        def __getitem__(self, index):
            if __coconut__.isinstance(index, __coconut__.slice):
                return self.__class__(*(__coconut__.igetitem(i, index) for i in self._iters))
            else:
                return (__coconut__.igetitem(i, index) for i in self._iters)
        def __reversed__(self):
            return self.__class__(*(__coconut__.reversed(i) for i in self._iters))
        def __len__(self):
            return __coconut__.min(*(__coconut__.len(i) for i in self._iters))
        def __repr__(self):
            return "zip(" + ", ".join((__coconut__.repr(i) for i in self._iters)) + ")"
        def __reduce_ex__(self, _):
            return (self.__class__, self._iters)
    class map(_map):
        __doc__ = map.__doc__
        __slots__ = ("_func", "_iters")
        __coconut_is_lazy__ = True
        def __new__(cls, function, *iterables):
            new_map = __coconut__._map.__new__(cls, function, *iterables)
            new_map._func, new_map._iters = function, iterables
            return new_map
        def __getitem__(self, index):
            if __coconut__.isinstance(index, __coconut__.slice):
                return self.__class__(self._func, *(__coconut__.igetitem(i, index) for i in self._iters))
            else:
                return self._func(*(__coconut__.igetitem(i, index) for i in self._iters))
        def __reversed__(self):
            return self.__class__(self._func, *(__coconut__.reversed(i) for i in self._iters))
        def __len__(self):
            return __coconut__.min(*(__coconut__.len(i) for i in self._iters))
        def __repr__(self):
            return "map(" + __coconut__.repr(self._func) + ", " + ", ".join((__coconut__.repr(i) for i in self._iters)) + ")"
        def __reduce_ex__(self, _):
            return (self.__class__, (self._func,) + self._iters)
    class parallel_map(map):
        """Multiprocessing implementation of map using concurrent.futures; requires arguments to be pickleable."""
        __slots__ = ()
        def __iter__(self):
            from concurrent.futures import ProcessPoolExecutor
            with ProcessPoolExecutor() as executor:
                for x in executor.map(self._func, *self._iters):
                    yield x
        def __repr__(self):
            return "parallel_" + __coconut__.map.__repr__(self)
    class count(object):
        """count(start, step) returns an infinite iterator starting at start and increasing by step."""
        __slots__ = ("_start", "_step")
        __coconut_is_lazy__ = True
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
            return (self.__class__, (self._start, self._step))
    @staticmethod
    def igetitem(iterable, index):
        if isinstance(iterable, __coconut__.range) or (__coconut__.hasattr(iterable, "__coconut_is_lazy__") and iterable.__coconut_is_lazy__):
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

__coconut_version__, MatchError, map, parallel_map, zip, reduce, takewhile, dropwhile, tee, count, recursive, datamaker, consume = __coconut__.version, __coconut__.MatchError, __coconut__.map, __coconut__.parallel_map, __coconut__.zip, __coconut__.functools.reduce, __coconut__.itertools.takewhile, __coconut__.itertools.dropwhile, __coconut__.itertools.tee, __coconut__.count, __coconut__.recursive, __coconut__.datamaker, __coconut__.consume
