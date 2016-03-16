#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xa32be0ca

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------

import sys as _coconut_sys
py3_map, py3_zip = map, zip

class __coconut__(object):
    version = "0.3.6-post_dev"
    import collections, functools, imp, itertools, operator, types
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    IndexError, NameError, _map, _zip, ascii, bytearray, dict, frozenset, getattr, hasattr, isinstance, iter, len, list, min, next, object, range, repr, reversed, set, slice, super, tuple = IndexError, NameError, map, zip, ascii, bytearray, dict, frozenset, getattr, hasattr, isinstance, iter, len, list, min, next, object, range, repr, reversed, set, slice, super, tuple
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
        """Parallel implementation of map using concurrent.futures; requires arguments to be pickleable."""
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

__coconut_version__, MatchError, map, parallel_map, zip, reduce, takewhile, dropwhile, tee, count, consume, recursive, datamaker = __coconut__.version, __coconut__.MatchError, __coconut__.map, __coconut__.parallel_map, __coconut__.zip, __coconut__.functools.reduce, __coconut__.itertools.takewhile, __coconut__.itertools.dropwhile, __coconut__.itertools.tee, __coconut__.count, __coconut__.consume, __coconut__.recursive, __coconut__.datamaker

# Compiled Coconut: ------------------------------------------------------------

import sys

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
