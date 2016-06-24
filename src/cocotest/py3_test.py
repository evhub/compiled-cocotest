#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x6068d54e

# Compiled with Coconut version 1.0.0-post_dev [Albatross]

# Coconut Header: --------------------------------------------------------------

import sys as _coconut_sys
py3_map, py3_zip = map, zip

class _coconut:
    import collections, functools, imp, itertools, operator, types
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    IndexError, NameError, ValueError, map, zip, bytearray, dict, frozenset, getattr, hasattr, isinstance, iter, len, list, min, next, object, range, reversed, set, slice, super, tuple, repr = IndexError, NameError, ValueError, map, zip, bytearray, dict, frozenset, getattr, hasattr, isinstance, iter, len, list, min, next, object, range, reversed, set, slice, super, tuple, repr

class _coconut_MatchError(Exception):
    """Pattern-matching error."""
    __slots__ = ("pattern", "value")
class _coconut_zip(_coconut.zip):
    __slots__ = ("_iters",)
    __doc__ = _coconut.zip.__doc__
    __coconut_is_lazy__ = True # tells $[] to use .__getitem__
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
class _coconut_map(_coconut.map):
    __slots__ = ("_func", "_iters")
    __doc__ = _coconut.map.__doc__
    __coconut_is_lazy__ = True # tells $[] to use .__getitem__
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
class _coconut_parallel_map(_coconut_map):
    """Multiprocessing implementation of map using concurrent.futures; requires arguments to be pickleable."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor() as executor:
            for x in executor.map(self._func, *self._iters):
                yield x
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class _coconut_count:
    """count(start, step) returns an infinite iterator starting at start and increasing by step."""
    __slots__ = ("_start", "_step")
    __coconut_is_lazy__ = True # tells $[] to use .__getitem__
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
def _coconut_igetitem(iterable, index):
    if isinstance(iterable, _coconut.range) or (_coconut.hasattr(iterable, "__coconut_is_lazy__") and iterable.__coconut_is_lazy__):
        return iterable[index]
    elif _coconut.hasattr(iterable, "__getitem__"):
        if _coconut.isinstance(index, _coconut.slice):
            return (x for x in iterable[index])
        else:
            return iterable[index]
    elif _coconut.isinstance(index, _coconut.slice):
        if (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
            return (x for x in _coconut.tuple(iterable)[index])
        else:
            return _coconut.itertools.islice(iterable, index.start, index.stop, index.step)
    elif index < 0:
        return _coconut.collections.deque(iterable, maxlen=-index)[0]
    else:
        return _coconut.next(_coconut.itertools.islice(iterable, index, index + 1))
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
def _coconut_minus(*args): return _coconut.operator.__neg__(*args) if len(args) < 2 else _coconut.operator.__sub__(*args)
def recursive(func):
    """Decorates a function by optimizing it for tail recursion."""
    state = [True, None] # state = [is_top_level, (args, kwargs)]
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
    return _coconut.collections.deque(iterable, maxlen=keep_last) # fastest way to exhaust an iterator
MatchError, map, parallel_map, zip, count, reduce, takewhile, dropwhile, tee = _coconut_MatchError, _coconut_map, _coconut_parallel_map, _coconut_zip, _coconut_count, _coconut.functools.reduce, _coconut.itertools.takewhile, _coconut.itertools.dropwhile, _coconut.itertools.tee

# Compiled Coconut: ------------------------------------------------------------

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
    assert (tuple)(py3_map(lambda x: x + 1, range(4))) == (1, 2, 3, 4)
    assert (tuple)(py3_zip(range(3), range(3))) == ((0, 0), (1, 1), (2, 2))
    class B(*()): pass
    assert isinstance(B(), B)
