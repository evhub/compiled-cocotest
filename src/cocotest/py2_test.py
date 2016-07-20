#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x6c64913d

# Compiled with Coconut version 1.1.1-post_dev [Brontosaurus]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
py2_chr, py2_filter, py2_hex, py2_input, py2_int, py2_map, py2_oct, py2_open, py2_print, py2_range, py2_raw_input, py2_str, py2_xrange, py2_zip = chr, filter, hex, input, int, map, oct, open, print, range, raw_input, str, xrange, zip
_coconut_int, _coconut_long, _coconut_print, _coconut_raw_input, _coconut_str, _coconut_unicode, _coconut_xrange, _coconut_repr = int, long, print, raw_input, str, unicode, xrange, repr
from future_builtins import *
chr, str = unichr, unicode
from io import open
class range(object):
    __slots__ = ("_xrange",)
    __doc__ = _coconut_xrange.__doc__
    def __init__(self, *args):
        self._xrange = _coconut_xrange(*args)
    def __iter__(self):
        return _coconut.iter(self._xrange)
    def __reversed__(self):
        return _coconut.reversed(self._xrange)
    def __len__(self):
        return _coconut.len(self._xrange)
    def __contains__(self, elem):
        return elem in self._xrange
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            start, stop, step = index.start, index.stop, index.step
            if start is None:
                start = 0
            elif start < 0:
                start += _coconut.len(self._xrange)
            if stop is None:
                stop = _coconut.len(self._xrange)
            elif stop is not None and stop < 0:
                stop += _coconut.len(self._xrange)
            if step is None:
                step = 1
            return _coconut_map(self._xrange.__getitem__, self.__class__(start, stop, step))
        else:
            return self._xrange[index]
    def count(self, elem):
        """Count the number of times elem appears in the range."""
        return int(elem in self._xrange)
    def index(self, elem):
        """Find the index of elem in the range."""
        if elem not in self._xrange: raise _coconut.ValueError(_coconut.repr(elem) + " is not in range")
        start, _, step = self._xrange.__reduce_ex__(2)[1]
        return (elem - start) // step
    def __repr__(self):
        return _coconut.repr(self._xrange)[1:]
    def __reduce_ex__(self, protocol):
        return (self.__class__, self._xrange.__reduce_ex__(protocol)[1])
    def __copy__(self):
        return self.__class__(*self._xrange.__reduce__()[1])
from collections import Sequence as _coconut_Sequence
_coconut_Sequence.register(range)
class int(_coconut_int):
    __slots__ = ()
    __doc__ = _coconut_int.__doc__
    class __metaclass__(type):
        def __instancecheck__(cls, inst):
            return _coconut.isinstance(inst, (_coconut_int, _coconut_long))
class bytes(_coconut_str):
    __slots__ = ()
    __doc__ = _coconut_str.__doc__
    class __metaclass__(type):
        def __instancecheck__(cls, inst):
            return _coconut.isinstance(inst, _coconut_str)
    def __new__(cls, *args, **kwargs):
        return _coconut_str.__new__(cls, _coconut.bytearray(*args, **kwargs))
def print(*args, **kwargs):
    if _coconut.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
        return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
    else:
        return _coconut_print(*(_coconut_unicode(x).encode() for x in args), **kwargs)
def input(*args, **kwargs):
    if _coconut.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
        return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
    else:
        return _coconut_raw_input(*args, **kwargs).decode()
def repr(obj):
    if isinstance(obj, _coconut_unicode):
        return _coconut_repr(obj)[1:]
    else:
        return _coconut_repr(obj)
ascii = repr
print.__doc__, input.__doc__, repr.__doc__ = _coconut_print.__doc__, _coconut_raw_input.__doc__, _coconut_repr.__doc__
def raw_input(*args):
    """Coconut uses Python 3 "input" instead of Python 2 "raw_input"."""
    raise _coconut.NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')
def xrange(*args):
    """Coconut uses Python 3 "range" instead of Python 2 "xrange"."""
    raise _coconut.NameError('Coconut uses Python 3 "range" instead of Python 2 "xrange"')
if _coconut_sys.version_info < (2, 7):
    import functools as _coconut_functools, copy_reg as _coconut_copy_reg
    def _coconut_new_partial(func, args, keywords):
        return _coconut_functools.partial(func, *(args if args is not None else ()), **(keywords if keywords is not None else {}))
    _coconut_copy_reg.constructor(_coconut_new_partial)
    def _coconut_reduce_partial(self):
        return (_coconut_new_partial, (self.func, self.args, self.keywords))
    _coconut_copy_reg.pickle(_coconut_functools.partial, _coconut_reduce_partial)

class _coconut(object):
    import collections, functools, imp, itertools, operator, types, copy
    abc = collections
    IndexError, NameError, ValueError, map, zip, bytearray, dict, frozenset, getattr, globals, hasattr, isinstance, iter, len, list, locals, min, next, object, range, reversed, set, slice, super, tuple, repr = IndexError, NameError, ValueError, map, zip, bytearray, dict, frozenset, getattr, globals, hasattr, isinstance, iter, len, list, locals, min, next, object, range, reversed, set, slice, super, tuple, staticmethod(repr)

class _coconut_MatchError(Exception):
    """Pattern-matching error."""
    __slots__ = ("pattern", "value")
def _coconut_igetitem(iterable, index):
    if isinstance(iterable, _coconut.range) or _coconut.hasattr(iterable, "__getitem__"):
        return iterable[index]
    elif not _coconut.isinstance(index, _coconut.slice):
        if index < 0:
            return _coconut.collections.deque(iterable, maxlen=-index)[0]
        else:
            return _coconut.next(_coconut.itertools.islice(iterable, index, index + 1))
    elif index.start is not None and index.start < 0 and (index.stop is None or index.stop < 0) and index.step is None:
        queue = _coconut.collections.deque(iterable, maxlen=-index.start)
        if index.stop is not None:
            queue = _coconut.tuple(queue)[:index.stop - index.start]
        return queue
    elif (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
        return _coconut.tuple(iterable)[index]
    else:
        return _coconut.itertools.islice(iterable, index.start, index.stop, index.step)
class _coconut_compose(object):
    __slots__ = ("f", "g")
    def __init__(self, f, g):
        self.f, self.g = f, g
    def __call__(self, *args, **kwargs):
        return self.f(self.g(*args, **kwargs))
    def __repr__(self):
        return _coconut.repr(self.f) + ".." + _coconut.repr(self.g)
    def __reduce__(self):
        return (_coconut_compose, (self.f, self.g))
def _coconut_pipe(x, f): return f(x)
def _coconut_starpipe(xs, f): return f(*xs)
def _coconut_backpipe(f, x): return f(x)
def _coconut_backstarpipe(f, xs): return f(*xs)
def _coconut_bool_and(a, b): return a and b
def _coconut_bool_or(a, b): return a or b
def _coconut_minus(*args): return _coconut.operator.neg(*args) if len(args) < 2 else _coconut.operator.sub(*args)
@_coconut.functools.wraps(_coconut.itertools.tee)
def _coconut_tee(iterable, n=2):
    if n > 0 and (_coconut.isinstance(iterable, _coconut.range) or _coconut.hasattr(iterable, "__copy__") or _coconut.isinstance(iterable, _coconut.abc.Sequence)):
        return (iterable,) + _coconut.tuple(_coconut.copy.copy(iterable) for i in range(n - 1))
    else:
        return _coconut.itertools.tee(iterable, n)
class _coconut_map(_coconut.map):
    __slots__ = ("_func", "_iters")
    __doc__ = _coconut.map.__doc__
    def __new__(cls, function, *iterables):
        new_map = _coconut.map.__new__(cls, function, *iterables)
        new_map._func, new_map._iters = function, iterables
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self._func, *(_coconut_igetitem(i, index) for i in self._iters))
        else:
            return self._func(*(_coconut_igetitem(i, index) for i in self._iters))
    def __reversed__(self):
        return self.__class__(self._func, *(_coconut.reversed(i) for i in self._iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self._iters)
    def __repr__(self):
        return "map(" + _coconut.repr(self._func) + ", " + ", ".join((_coconut.repr(i) for i in self._iters)) + ")"
    def __reduce_ex__(self, _):
        return (self.__class__, (self._func,) + self._iters)
    def __copy__(self):
        return self.__class__(self._func, *_coconut_map(_coconut.copy.copy, self._iters))
class zip(_coconut.zip):
    __slots__ = ("_iters",)
    __doc__ = _coconut.zip.__doc__
    def __new__(cls, *iterables):
        new_zip = _coconut.zip.__new__(cls, *iterables)
        new_zip._iters = iterables
        return new_zip
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(*(_coconut_igetitem(i, index) for i in self._iters))
        else:
            return (_coconut_igetitem(i, index) for i in self._iters)
    def __reversed__(self):
        return self.__class__(*(_coconut.reversed(i) for i in self._iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self._iters)
    def __repr__(self):
        return "zip(" + ", ".join((_coconut.repr(i) for i in self._iters)) + ")"
    def __reduce_ex__(self, _):
        return (self.__class__, self._iters)
    def __copy__(self):
        return self.__class__(*_coconut_map(_coconut.copy.copy, self._iters))
class count(object):
    """count(start, step) returns an infinite iterator starting at start and increasing by step."""
    __slots__ = ("_start", "_step")
    def __init__(self, start=0, step=1):
        self._start, self._step = start, step
    def __iter__(self):
        while True:
            yield self._start
            self._start += self._step
    def __contains__(self, elem):
        return elem >= self._start and (elem - self._start) % self._step == 0
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice) and (index.start is None or index.start >= 0) and (index.stop is not None and index.stop >= 0):
            return _coconut_map(lambda x: self._start + x * self._step, _coconut.range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
        elif index >= 0:
            return self._start + index * self._step
        else:
            raise _coconut.IndexError("count indices must be positive")
    def count(self, elem):
        """Count the number of times elem appears in the count."""
        return int(elem in self)
    def index(self, elem):
        """Find the index of elem in the count."""
        if elem not in self: raise _coconut.ValueError(_coconut.repr(elem) + " is not in count")
        return (elem - self._start) // self._step
    def __repr__(self):
        return "count(" + str(self._start) + ", " + str(self._step) + ")"
    def __reduce__(self):
        return (self.__class__, (self._start, self._step))
    def __copy__(self):
        return self.__class__(self._start, self._step)
class parallel_map(_coconut_map):
    """Multiprocessing implementation of map using concurrent.futures; requires arguments to be pickleable."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor() as executor:
            return _coconut.iter(_coconut.tuple(executor.map(self._func, *self._iters)))
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class concurrent_map(_coconut_map):
    """Multithreading implementation of map using concurrent.futures."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ThreadPoolExecutor
        from multiprocessing import cpu_count  # cpu_count() * 5 is the default Python 3 thread count
        with ThreadPoolExecutor(cpu_count() * 5) as executor:
            return _coconut.iter(_coconut.tuple(executor.map(self._func, *self._iters)))
    def __repr__(self):
        return "concurrent_" + _coconut_map.__repr__(self)
def recursive(func):
    """Decorates a function by optimizing it for tail recursion."""
    state = [True, None]  # state = [is_top_level, (args, kwargs)]
    recurse = object()
    @_coconut.functools.wraps(func)
    def recursive_func(*args, **kwargs):
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
    return recursive_func
def recursive_iterator(func):
    """Decorates a function by optimizing it for iterator recursion."""
    tee_store = {}
    @_coconut.functools.wraps(func)
    def recursive_iterator_func(*args, **kwargs):
        hashable_args_kwargs = args, _coconut.frozenset(kwargs.items())
        if hashable_args_kwargs in tee_store:
            to_tee = tee_store[hashable_args_kwargs]
        else:
            to_tee = func(*args, **kwargs)
        tee_store[hashable_args_kwargs], to_return = _coconut_tee(to_tee)
        return to_return
    return recursive_iterator_func
def addpattern(base_func):
    """Decorator to add a new case to a pattern-matching function, where the new case is checked last."""
    def pattern_adder(func):
        @_coconut.functools.wraps(func)
        def add_pattern_func(*args, **kwargs):
            try:
                return base_func(*args, **kwargs)
            except _coconut_MatchError:
                return func(*args, **kwargs)
        return add_pattern_func
    return pattern_adder
def prepattern(base_func):
    """Decorator to add a new case to a pattern-matching function, where the new case is checked first."""
    def pattern_prepender(func):
        @_coconut.functools.wraps(func)
        def pre_pattern_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except _coconut_MatchError:
                return base_func(*args, **kwargs)
        return pre_pattern_func
    return pattern_prepender
def datamaker(data_type):
    """Returns base data constructor of passed data type."""
    return _coconut.functools.partial(_coconut.super(data_type, data_type).__new__, data_type)
def consume(iterable, keep_last=0):
    """Fully exhaust iterable and return the last keep_last elements."""
    return _coconut.collections.deque(iterable, maxlen=keep_last)  # fastest way to exhaust an iterator
MatchError, map, reduce, takewhile, dropwhile, tee = _coconut_MatchError, _coconut_map, _coconut.functools.reduce, _coconut.itertools.takewhile, _coconut.itertools.dropwhile, _coconut_tee

# Compiled Coconut: ------------------------------------------------------------

def py2_test():
    """Performs Python2-specific tests."""
    assert py2_filter(_coconut.functools.partial(_coconut.operator.gt, 3), range(10)) == [0, 1, 2]
    assert py2_map(_coconut.functools.partial(_coconut.operator.add, 2), range(5)) == [2, 3, 4, 5, 6]
    assert py2_range(5) == [0, 1, 2, 3, 4]
    assert not isinstance(long(1), py2_int)
    assert py2_str(3) == b"3" == unicode(b"3")
