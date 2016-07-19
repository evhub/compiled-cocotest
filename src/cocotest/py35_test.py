#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x8029814d

# Compiled with Coconut version 1.1.1-post_dev [Brontosaurus]

# Coconut Header: --------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
py3_map, py3_zip = map, zip

class _coconut:
    import collections, functools, imp, itertools, operator, types, copy
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    IndexError, NameError, ValueError, map, zip, bytearray, dict, frozenset, getattr, globals, hasattr, isinstance, iter, len, list, locals, min, next, object, range, reversed, set, slice, super, tuple, repr = IndexError, NameError, ValueError, map, zip, bytearray, dict, frozenset, getattr, globals, hasattr, isinstance, iter, len, list, locals, min, next, object, range, reversed, set, slice, super, tuple, repr

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
    elif (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
        return _coconut.tuple(iterable)[index]
    else:
        return _coconut.itertools.islice(iterable, index.start, index.stop, index.step)
class _coconut_compose:
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
class count:
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
            return _coconut.tuple(executor.map(self._func, *self._iters))
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class concurrent_map(_coconut_map):
    """Multithreading implementation of map using concurrent.futures."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor() as executor:
            return _coconut.tuple(executor.map(self._func, *self._iters))
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

import asyncio

def py35_test():
    """Performs Python-3.5-specific tests."""
    async def async_map_0(args):
        return parallel_map(args[0], *args[1:])
    async def async_map_1(args): return parallel_map(args[0], *args[1:])
    async def async_map_2 (*_coconut_match_to):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to) == 1) and (_coconut.isinstance(_coconut_match_to[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to[0]) >= 1):
            iters = _coconut.list(_coconut_match_to[0][1:])
            func = _coconut_match_to[0][0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'async def async_map_2([func] + iters) = parallel_map(func, *iters)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'async def async_map_2([func] + iters) = parallel_map(func, *iters)'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        return parallel_map(func, *iters)

    async def async_map_3 (*_coconut_match_to):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to) == 1) and (_coconut.isinstance(_coconut_match_to[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to[0]) >= 1):
            iters = _coconut.list(_coconut_match_to[0][1:])
            func = _coconut_match_to[0][0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'async match def async_map_3([func] + iters) = parallel_map(func, *iters)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'async match def async_map_3([func] + iters) = parallel_map(func, *iters)'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        return parallel_map(func, *iters)

    async def async_map_4 (*_coconut_match_to):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to) == 1) and (_coconut.isinstance(_coconut_match_to[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to[0]) >= 1):
            iters = _coconut.list(_coconut_match_to[0][1:])
            func = _coconut_match_to[0][0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match async def async_map_4([func] + iters) = parallel_map(func, *iters)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'match async def async_map_4([func] + iters) = parallel_map(func, *iters)'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        return parallel_map(func, *iters)

    async def async_map_test():
        for async_map in (async_map_0, async_map_1, async_map_2, async_map_3, async_map_4):
            assert (tuple)((await ((async_map)((_coconut.functools.partial(pow, 2), range(5)))))) == (1, 2, 4, 8, 16)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_map_test())
    loop.close()
    try:
        2 @ 3
    except TypeError:
        assert True
    else:
        assert False
    assert (1, *(2, 3), 4) == (1, 2, 3, 4)
    assert {"a": 1, **{"b": 2}, "c": 3}["b"] == {"a": 1, "b": 2, "c": 3}
