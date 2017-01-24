#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x6a5316e4

# Compiled with Coconut version 1.2.0-post_dev26 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_tee, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

# Imports:
import random

# Random Number Helper:
def rand_list(n):
    '''Generates A Random List Of Length n.'''
    return [random.randrange(10) for x in range(0, n)]

# Infix Functions:
plus = _coconut.operator.add
mod = _coconut.operator.mod
def mod_(a,  # type: int
    b,  # type: int
    ):
# type: (...) -> int
    return a % b
base = int
@_coconut_tco
def join_with(a, b=""):
    raise _coconut_tail_call(b.join, a)

# Basic Functions:
prod = _coconut.functools.partial(reduce, _coconut.operator.mul)
@_coconut_tco
def zipwith(f, *args):
    raise _coconut_tail_call(map, lambda items: f(*items), zip(*args))
zipsum = _coconut_compose(_coconut.functools.partial(map, sum), zip)
plus1 = _coconut.functools.partial(plus, 1)
ident = lambda x: x
_coconut_decorator_0 = _coconut_compose(ident, ident)
@_coconut_decorator_0
def plus1_(x  # type: int
    ):
# type: (...) -> int
    return x + 1
def sqrt(x  # type: int
    ):
# type: (...) -> float
    return x**0.5
def sqrt_(x):
    return x**0.5
square = _coconut_partial(_coconut.operator.pow, {1: 2}, 2)
plus1sq = _coconut_compose(square, plus1)
sqplus1 = plus1
sqplus1 = _coconut_compose(sqplus1, (square))
plus1sq_ = lambda x: (square)((plus1)(x))
sqplus1_ = lambda x: (plus1)((square)(x))
clean = lambda s: s.strip()
add2 = lambda x: lambda y: x + y
def swap2(f):
    return lambda x, y: f(y, x)
swap2_ = lambda f: lambda x, y: f(y, x)
@_coconut_tco
def same(iter1, iter2):
    raise _coconut_tail_call(map, _coconut.operator.eq, iter1, iter2)
def chain2(a, b):
    _coconut_yield_from = a
    for _coconut_yield_item in _coconut_yield_from:
        yield _coconut_yield_item

    _coconut_yield_from = b
    for _coconut_yield_item in _coconut_yield_from:
        yield _coconut_yield_item

def threeple(a, b, c):
    return (a, b, c)

# Partial Applications:
sum_ = _coconut.functools.partial(reduce, _coconut.operator.add)
add = _coconut.functools.partial(zipwith, _coconut.operator.add)

# Quick-Sorts:
def qsort1(l):
    '''Non-Functional Quick Sort.'''
    if len(l) == 0:
        return []
    else:
        l = list(l)
        split = l.pop()
        smalls = []
        larges = []
        for x in l:
            if x <= split:
                smalls.append(x)
            else:
                larges.append(x)
        return qsort1(smalls) + [split] + qsort1(larges)
def qsort2(l):
    """Functional Quick Sort."""
    if not l:
        return []
    else:
        head, tail = l[0], l[1:]  # Python Pattern-Matching
        return (qsort2([x for x in tail if x <= head]) + [head] + qsort2([x for x in tail if x > head]))
@_coconut_tco
def qsort3(l):
    """Iterator Quick Sort."""
    try:
        tail, tail_ = (tee)((iter)(l))
# Since only iter is ever called on l, and next on tail, l only has to be an iterator
        head = next(tail)
        return (_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: qsort3((x for x in tail if x <= head)), lambda: (head,), lambda: qsort3((x for x in tail_ if x > head))))))
    except StopIteration:
        raise _coconut_tail_call(iter, ())
def qsort4(l):
    """Match Quick Sort."""
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return l
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        tail = _coconut.list(_coconut_match_to[1:])
        head = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return (qsort4([x for x in tail if x <= head]) + [head] + qsort4([x for x in tail if x > head]))
@_coconut_tco
def qsort5(l):
    """Iterator Match Quick Sort."""
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        tail = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1):
            head = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        tail, tail_ = tee(tail)
        return (_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: qsort5((x for x in tail if x <= head)), lambda: (head,), lambda: qsort5((x for x in tail_ if x > head))))))
    else:
        raise _coconut_tail_call(iter, ())

# Infinite Iterators:
def repeat(elem):
    """Repeat Iterator."""
    while True:
        yield elem
@_coconut_tco
def repeat_(elem):
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: (elem,), lambda: repeat_(elem))))
def N(n=0):
    """Natural Numbers."""
    while True:
        yield n
        n += 1
@_coconut_tco
def N_(n=0):
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: (n,), lambda: N_(n + 1))))
def N__(n=0):
    it = n,
    _coconut_lazy_chain_0 = it
    it = _coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: _coconut_lazy_chain_0, lambda: (N__(n + 1)))))
    return it
def preN(it):
    _coconut_lazy_chain_1 = it
    it = _coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: _coconut_lazy_chain_1, lambda: (N()))))
    return it
@_coconut_tco
def map_iter(func, args):
    _coconut_match_check = False
    _coconut_match_to = args
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        xs = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1):
            x = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: func(x),)), lambda: map_iter(func, xs))))

# Recursive Functions:

@_coconut_tco
def next_mul_of(n, x):
    while True:
        if x % n == 0:
            return x
        else:
            if next_mul_of is _coconut_recursive_func_23:
                n, x = n, x + 1
                continue
            else:
                raise _coconut_tail_call(next_mul_of, n, x + 1)


        return None
_coconut_recursive_func_23 = next_mul_of
@_coconut_tco
def collatz(n):
    while True:
        if n == 1:
            return True
        elif n % 2 == 0:
            if collatz is _coconut_recursive_func_24:
                n = n / 2
                continue
            else:
                raise _coconut_tail_call(collatz, n / 2)

        else:
            if collatz is _coconut_recursive_func_24:
                n = 3 * n + 1
                continue
            else:
                raise _coconut_tail_call(collatz, 3 * n + 1)


        return None
_coconut_recursive_func_24 = collatz
@_coconut_tco
def recurse_n_times(n):
    while True:
        if not n:
            return True
        if recurse_n_times is _coconut_recursive_func_25:
            n = n - 1
            continue
        else:
            raise _coconut_tail_call(recurse_n_times, n - 1)
        return None

_coconut_recursive_func_25 = recurse_n_times
@_coconut_tco
def is_even(n):
    if not n:
        return True
    raise _coconut_tail_call(is_odd, n - 1)
@_coconut_tco
def is_odd(n):
    if not n:
        return False
    raise _coconut_tail_call(is_even, n - 1)

def is_even_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def is_even_(0) = True'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def is_even_(0) = True'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return True
@addpattern(is_even_)
@_coconut_tco
def is_even_(n):
    raise _coconut_tail_call(is_odd_, n - 1)

def is_odd_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def is_odd_(0) = False'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def is_odd_(0) = False'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return False
@addpattern(is_odd_)
@_coconut_tco
def is_odd_(n):
    raise _coconut_tail_call(is_even_, n - 1)

# Data Blocks:
class preop(_coconut.collections.namedtuple("preop", "x, y")):
    __slots__ = ()
    def add(self):
        return self.x + self.y
class vector(_coconut.collections.namedtuple("vector", "x, y")):
    __slots__ = ()
    def __new__(cls, x, y=None):
        _coconut_match_check = False
        _coconut_match_to = x
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check:
            pass
        return datamaker(cls)(x, y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5
    @_coconut_tco
    def transform(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check:
            raise _coconut_tail_call(vector, self.x + x, self.y + y)
        else:
            raise TypeError()
    def __eq__(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == self.x) and (_coconut_match_to[1] == self.y):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
class triangle(_coconut.collections.namedtuple("triangle", "a, b, c")):
    __slots__ = ()
    def is_right(self):
        return self.a**2 + self.b**2 == self.c**2
class null1(_coconut.collections.namedtuple("null1", "")):
    __slots__ = ()
class null2(_coconut.collections.namedtuple("null2", "")):
    __slots__ = ()
null = (null1, null2)
def is_null(item):
    _coconut_match_check = False
    _coconut_match_to = item
    if (_coconut.isinstance(_coconut_match_to, null)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False

# Factorial:
def factorial1(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, int)):
        n = _coconut_match_to
        _coconut_match_check = True
    if _coconut_match_check and not (n > 0):
        _coconut_match_check = False
    if _coconut_match_check:
        return n * factorial1(n - 1)
def factorial2(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    else:
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, int)):
            n = _coconut_match_to
            _coconut_match_check = True
        if _coconut_match_check and not (n > 0):
            _coconut_match_check = False
        if _coconut_match_check:
            return n * factorial2(n - 1)
        else:
            return None
    raise TypeError()
def factorial3(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, int)):
        n = _coconut_match_to
        _coconut_match_check = True
    if _coconut_match_check and not (n > 0):
        _coconut_match_check = False
    if _coconut_match_check:
        return n * factorial3(n - 1)
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return []
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        tail = _coconut.list(_coconut_match_to[1:])
        head = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return [factorial3(head)] + factorial3(tail)
def factorial4(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    if not _coconut_match_check:
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, int)):
            n = _coconut_match_to
            _coconut_match_check = True
        if _coconut_match_check and not (n > 0):
            _coconut_match_check = False
        if _coconut_match_check:
            return n * factorial4(n - 1)
def factorial5(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    if not _coconut_match_check:
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, int)):
            n = _coconut_match_to
            _coconut_match_check = True
        if _coconut_match_check and not (n > 0):
            _coconut_match_check = False
        if _coconut_match_check:
            return n * factorial5(n - 1)
    if not _coconut_match_check:
        return None
    raise TypeError()
@_coconut_tco
def fact(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    def _coconut_mock_func(*_coconut_match_to_args, **_coconut_match_to_kwargs): return _coconut_match_to_args, _coconut_match_to_kwargs
    while True:
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")
            if (not _coconut_match_to_kwargs):
                n = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match def fact(n) = fact(n, 1)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'match def fact(n) = fact(n, 1)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        if fact is _coconut_recursive_func_44:
            _coconut_match_to_args, _coconut_match_to_kwargs = _coconut_mock_func(n, 1)
            continue
        else:
            raise _coconut_tail_call(fact, n, 1)
        return None
_coconut_recursive_func_44 = fact
@addpattern(fact)
def fact(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) == 1) and (_coconut_match_to_args[0] == 0):
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc")
        if (not _coconut_match_to_kwargs):
            acc = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match def fact(0, acc) = acc'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'match def fact(0, acc) = acc'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return acc
@addpattern(fact)
@_coconut_tco
def fact(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc")
        if (not _coconut_match_to_kwargs):
            n = _coconut_match_temp_0
            acc = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match def fact(n, acc) = fact(n-1, acc*n)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'match def fact(n, acc) = fact(n-1, acc*n)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    raise _coconut_tail_call(fact, n - 1, acc * n)

# Match Functions:
def classify(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, tuple)):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty tuple"
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            return "singleton tuple"
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return "duplicate pair tuple of " + str(x)
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            return "pair tuple"
        return "tuple"
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, list)):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty list"
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            return "singleton list"
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return "duplicate pair list of " + str(x)
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            return "pair list"
        return "list"
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, dict)):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty dict"
        else:
            return "dict"
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, (set, frozenset))):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Set)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty set"
        _coconut_match_check = False
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Set)) and (_coconut.len(_coconut_match_to) == 1) and (0 in _coconut_match_to):
            _coconut_match_check = True
        if _coconut_match_check:
            return "set of 0"
        return "set"
    raise TypeError()
def classify_sequence(value):
    out = ""
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        out += "empty"
    if not _coconut_match_check:
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            out += "singleton"
    if not _coconut_match_check:
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            out += "duplicate pair of " + str(x)
    if not _coconut_match_check:
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            out += "pair"
    if not _coconut_match_check:
        _coconut_match_to = value
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 3):
            _coconut_match_check = True
        if (not _coconut_match_check) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 4):
            _coconut_match_check = True
        if _coconut_match_check:
            out += "few"
    if not _coconut_match_check:
        raise TypeError()
    return out
def dictpoint(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2) and ("x" in _coconut_match_to) and (_coconut.isinstance(_coconut_match_to["x"], int)) and ("y" in _coconut_match_to) and (_coconut.isinstance(_coconut_match_to["y"], int)):
        x = _coconut_match_to["x"]
        y = _coconut_match_to["y"]
        _coconut_match_check = True
    if _coconut_match_check:
        return (x, y)
    else:
        raise TypeError()
def map_(func, args):
    _coconut_match_check = False
    _coconut_match_to = args
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        l = _coconut_match_to
        _coconut_match_check = True
    if (not _coconut_match_check) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        l = _coconut_match_to
        _coconut_match_check = True
    if _coconut_match_check:
        return l
    _coconut_match_check = False
    _coconut_match_to = args
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        xs = _coconut.tuple(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check and not ((isinstance)(args, tuple)):
        _coconut_match_check = False
    if _coconut_match_check:
        return (func(x),) + map_(func, xs)
    _coconut_match_check = False
    _coconut_match_to = args
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        xs = _coconut.list(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check and not ((isinstance)(args, list)):
        _coconut_match_check = False
    if _coconut_match_check:
        return [func(x)] + map_(func, xs)
def duplicate_first1(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        l = _coconut_match_to
        xs = _coconut.list(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return [x] + l
    else:
        raise TypeError()
@_coconut_tco
def duplicate_first2(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        l = _coconut_match_to
        xs = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1):
            x = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: [x], lambda: l)))
    else:
        raise TypeError()
@_coconut_tco
def duplicate_first3(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        l = _coconut_match_to
        xs = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1):
            x = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: [x], lambda: l)))
    else:
        raise TypeError()
def one_to_five(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 2) and (_coconut_match_to[0] == 1) and (_coconut_match_to[-1] == 5):
        m = _coconut.list(_coconut_match_to[1:-1])
        _coconut_match_check = True
    if _coconut_match_check:
        return m
    else:
        return False

# Unicode Functions:
square_u = lambda x: x**2
def neg_u(x):
    return -x
neg_square_u = lambda x: (neg_u)((square_u)(x))

# In-Place Functions:
def pipe(a, b):
    a = (b)(a)
    return a
def compose(a, b):
    a = _coconut_compose(a, (b))
    return a
def chain(a, b):
    _coconut_lazy_chain_2 = a
    a = _coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: _coconut_lazy_chain_2, lambda: (b))))
    return a

# Algebraic Data Types:
class empty(_coconut.collections.namedtuple("empty", "")):
    __slots__ = ()
class leaf(_coconut.collections.namedtuple("leaf", "n")):
    __slots__ = ()
class node(_coconut.collections.namedtuple("node", "l, r")):
    __slots__ = ()
tree = (empty, leaf, node)

def depth(t):
    _coconut_match_check = False
    _coconut_match_to = t
    if (_coconut.isinstance(_coconut_match_to, tree)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 0
    _coconut_match_check = False
    _coconut_match_to = t
    if (_coconut.isinstance(_coconut_match_to, tree)) and (_coconut.len(_coconut_match_to) == 1):
        n = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_check = False
    _coconut_match_to = t
    if (_coconut.isinstance(_coconut_match_to, tree)) and (_coconut.len(_coconut_match_to) == 2):
        l = _coconut_match_to[0]
        r = _coconut_match_to[1]
        _coconut_match_check = True
    if _coconut_match_check:
        return 1 + max([depth(l), depth(r)])

# Monads:
def base_maybe(x, f):
    return f(x) if x is not None else None
@_coconut_tco
def maybes(*fs):
    raise _coconut_tail_call(reduce, base_maybe, fs)

class Nothing(_coconut.collections.namedtuple("Nothing", "")):
    __slots__ = ()
    @_coconut_tco
    def __call__(self, *args):
        raise _coconut_tail_call(Nothing)
    def __eq__(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, Nothing)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
class Just(_coconut.collections.namedtuple("Just", "item")):
    __slots__ = ()
    @_coconut_tco
    def __call__(self, *args):
        raise _coconut_tail_call((Just), reduce(_coconut_pipe, args, self.item))
    def __eq__(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, Just)) and (_coconut.len(_coconut_match_to) == 1):
            item = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return self.item == item
        else:
            return False
Maybe = (Nothing, Just)

# Destructuring Assignment:
def head_tail(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        tail = _coconut.list(_coconut_match_to[1:])
        head = _coconut_match_to[0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match [head] + tail = l'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'match [head] + tail = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return head, tail
def init_last(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        init = _coconut.list(_coconut_match_to[:-1])
        last = _coconut_match_to[-1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'init + [last] = l'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'init + [last] = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return init, last
def last_two(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 2):
        _ = _coconut.list(_coconut_match_to[:-2])
        a = _coconut_match_to[-2]
        b = _coconut_match_to[-1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'_ + [a, b] = l'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = '_ + [a, b] = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return a, b
def delist2(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.len(_coconut_match_to) == 2):
        a = _coconut_match_to[0]
        b = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match list(a, b) = l'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'match list(a, b) = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return a, b
def delist2_(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.len(_coconut_match_to) == 2):
        a = _coconut_match_to[0]
        b = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'list(a, b)  = l'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'list(a, b)  = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return a, b

# Optional Explicit Assignment:
def expl_ident(x):
    return x
def dictpoint_(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2) and ("x" in _coconut_match_to) and (_coconut.isinstance(_coconut_match_to["x"], int)) and ("y" in _coconut_match_to) and (_coconut.isinstance(_coconut_match_to["y"], int)):
        x = _coconut_match_to["x"]
        y = _coconut_match_to["y"]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"x":x is int, "y":y is int} = value\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = '{"x":x is int, "y":y is int} = value'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return x, y
def dictpoint__(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to_args[0]) == 2) and ("x" in _coconut_match_to_args[0]) and (_coconut.isinstance(_coconut_match_to_args[0]["x"], int)) and ("y" in _coconut_match_to_args[0]) and (_coconut.isinstance(_coconut_match_to_args[0]["y"], int)):
        x = _coconut_match_to_args[0]["x"]
        y = _coconut_match_to_args[0]["y"]
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'def dictpoint__({"x":x is int, "y":y is int}):\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def dictpoint__({"x":x is int, "y":y is int}):'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x, y
def tuple1(a):
    return a,
def tuple1_(a):
    return a,
def tuple2(a, b):
    return a, b
def tuple2_(a, b):
    return a, b

# Enhanced Decorators:
_coconut_decorator_0 = lambda f: f
@_coconut_decorator_0
def dectest(x):
    return x

# Match Function Definition:
def last_two_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 2):
        _ = _coconut.list(_coconut_match_to_args[0][:-2])
        a = _coconut_match_to_args[0][-2]
        b = _coconut_match_to_args[0][-1]
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def last_two_(_ + [a, b]):'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def last_two_(_ + [a, b]):'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a, b
def htsplit(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
        tail = _coconut.list(_coconut_match_to_args[0][1:])
        head = _coconut_match_to_args[0][0]
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match def htsplit([head] + tail) = [head, tail]'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'match def htsplit([head] + tail) = [head, tail]'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return [head, tail]
def htsplit_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
        tail = _coconut.list(_coconut_match_to_args[0][1:])
        head = _coconut_match_to_args[0][0]
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def htsplit_([head] + tail) = [head, tail]'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def htsplit_([head] + tail) = [head, tail]'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return [head, tail]
def iadd(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match def (x is int) `iadd` (y is int) = x + y'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'match def (x is int) `iadd` (y is int) = x + y'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x + y
def iadd_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def (x is int) `iadd_` (y is int) = x + y'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def (x is int) `iadd_` (y is int) = x + y'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x + y
def strmul(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            a = _coconut_match_temp_0
            x = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match def strmul(a is str, x is int):'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'match def strmul(a is str, x is int):'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a * x
def strmul_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            a = _coconut_match_temp_0
            x = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def strmul_(a is str, x is int):'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def strmul_(a is str, x is int):'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a * x

# Lazy Lists:
class lazy(_coconut.object):
    done = False
    def finish(self):
        self.done = True
    def list(self):
        return (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2, lambda: 3, lambda: self.finish()))
def is_empty(i):
    _coconut_match_check = False
    _coconut_match_to = i
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        _coconut_match_temp_0 = _coconut.tuple(_coconut_match_to)
        if (_coconut.len(_coconut_match_temp_0) == 0):
            _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False
def is_one(i):
    _coconut_match_check = False
    _coconut_match_to = i
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        _coconut_match_temp_0 = _coconut.tuple(_coconut_match_to)
        if (_coconut.len(_coconut_match_temp_0) == 1) and (_coconut_match_temp_0[0] == 1):
            _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False

# Constructed Data Types:
class trilen(_coconut.collections.namedtuple("trilen", "h")):
    __slots__ = ()
    @_coconut_tco
    def __new__(cls, a, b):
        raise _coconut_tail_call((datamaker(cls)), (a**2 + b**2)**0.5)

# Inheritance:
class A(_coconut.object):
    def true(self):
        return True
class B(A):
    pass

# Infinite Grid:

class pt(_coconut.collections.namedtuple("pt", "x, y")):
    """Cartesian point in the x-y plane. Immutable."""
    __slots__ = ()
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __eq__(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, pt)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == self.x) and (_coconut_match_to[1] == self.y):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False

@_coconut_tco
def vertical_line(x=0, y=0):
    """Infinite iterator of pt representing a vertical line."""
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: (pt(x, y),), lambda: vertical_line(x, y + 1))))

@_coconut_tco
def grid(x=0):
    """Infinite iterator of infinite iterators representing cartesian space."""
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: (vertical_line(x, 0),), lambda: grid(x + 1))))

@_coconut_tco
def grid_map(func, gridsample):
    """Map a function over every point in a grid."""
    raise _coconut_tail_call((_coconut.functools.partial(map, _coconut.functools.partial(map, func))), gridsample)

@_coconut_tco
def parallel_grid_map(func, gridsample):
    """Map a function over every point in a grid in parallel."""
    raise _coconut_tail_call((_coconut.functools.partial(parallel_map, _coconut.functools.partial(parallel_map, func))), gridsample)

@_coconut_tco
def grid_trim(gridsample, xmax, ymax):
    """Convert a grid to a list of lists up to xmax and ymax."""
    raise _coconut_tail_call((list), (_coconut.functools.partial(map, lambda l: (list)(_coconut_igetitem(l, _coconut.slice(None, ymax)))))(_coconut_igetitem(gridsample, _coconut.slice(None, xmax))))

# Physics function:

def SHOPeriodTerminate(X, t, params):
    if X[1] > 0:
        return -1  # passed the turning point, so go back
    epsilon = params['epsilon'] if 'epsilon' in params else 1e-8
    if abs(X[1]) < epsilon and X[0] < 0:
        return 1  # we're done
    return 0  # keep going

# Multiple dispatch:

def add_int_or_str_1(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def add_int_or_str_1(x is int) = x + 1'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def add_int_or_str_1(x is int) = x + 1'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x + 1
@addpattern(add_int_or_str_1)
def add_int_or_str_1(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'def add_int_or_str_1(x is str) = x + "1"\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def add_int_or_str_1(x is str) = x + "1"'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x + "1"

def coercive_add(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "b" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("b")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            a = _coconut_match_temp_0
            b = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def coercive_add(a is int, b) = a + int(b)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def coercive_add(a is int, b) = a + int(b)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a + int(b)
@addpattern(coercive_add)
def coercive_add(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "b" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("b")
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (not _coconut_match_to_kwargs):
            a = _coconut_match_temp_0
            b = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def coercive_add(a is str, b) = a + str(b)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def coercive_add(a is str, b) = a + str(b)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a + str(b)

@addpattern(ident)
def still_ident(x):
    return "foo"

@prepattern(ident)
def not_ident(x):
    return "bar"

# Pattern-matching functions with guards

def pattern_abs(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check and not (x < 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def pattern_abs(x if x < 0) = -x'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def pattern_abs(x if x < 0) = -x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return -x
@addpattern(pattern_abs)
def pattern_abs(x):
    return x

def pattern_abs_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check and not (x < 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def `pattern_abs_` (x) if x < 0 = -x'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def `pattern_abs_` (x) if x < 0 = -x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return -x
@addpattern(pattern_abs_)
def pattern_abs_(x):
    return x

# Recursive iterator

@recursive_iterator
@_coconut_tco
def fib():
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: (1, 2), lambda: map(_coconut.operator.add, fib(), _coconut_igetitem(fib(), _coconut.slice(1, None))))))

@recursive_iterator
@_coconut_tco
def loop(it):
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: it, lambda: loop(it))))

# Sieve Example

def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
        _coconut_match_temp_0 = _coconut.tuple(_coconut_match_to_args[0])
        if (_coconut.len(_coconut_match_temp_0) == 0) and (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def sieve((||)) = []'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def sieve((||)) = []'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return []

@prepattern(sieve)
@_coconut_tco
def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
        tail = _coconut.iter(_coconut_match_to_args[0])
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1) and (not _coconut_match_to_kwargs):
            head = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def sieve([head] :: tail) = [head] :: sieve(n for n in tail if n % head)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def sieve([head] :: tail) = [head] :: sieve(n for n in tail if n % head)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: [head], lambda: sieve((n for n in tail if n % head)))))

# "Assignment function" definitions

def double_plus_one(x):
    x *= 2
    return x + 1

@_coconut_tco
def assign_func_1(f, x, y):
    @_coconut_tco
    def inner_assign_func(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 2):
            a = _coconut_match_to_args[0][0]
            b = _coconut_match_to_args[0][1]
            if (not _coconut_match_to_kwargs):
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def inner_assign_func((a, b)) = f(a, b)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def inner_assign_func((a, b)) = f(a, b)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        raise _coconut_tail_call(f, a, b)
    raise _coconut_tail_call(inner_assign_func, (x, y))

@_coconut_tco
def assign_func_2(f, x, y):
    @_coconut_tco
    def inner_assign_func(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 2):
            a = _coconut_match_to_args[0][0]
            b = _coconut_match_to_args[0][1]
            if (not _coconut_match_to_kwargs):
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def inner_assign_func((a, b)) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def inner_assign_func((a, b)) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        raise _coconut_tail_call(f, a, b)
    raise _coconut_tail_call(inner_assign_func, (x, y))

# Composable Functions

mul = _coconut.operator.mul
def minus(a, b):
    return b - a

# Exception Functions

def raise_exc():
    raise Exception()

def does_raise_exc(func):
    try:
        return func()
    except Exception:
        return True

# Returns

@_coconut_tco
def ret_none(n):
    while True:
        if n != 0:
            if ret_none is _coconut_recursive_func_122:
                n = n - 1
                continue
            else:
                raise _coconut_tail_call(ret_none, n - 1)


        return None
_coconut_recursive_func_122 = ret_none
def ret_args_kwargs(*args, **kwargs):
    return (args, kwargs)

# Typing

import sys
if sys.version_info > (3, 5):
    from typing import Any
    from typing import List
    from typing import Dict

    def args_kwargs_func(args=[],  # type: List[Any]
     kwargs={}  # type: Dict[Any, Any]
    ):
# type: (...) -> None
        pass
else:
    def args_kwargs_func(args=[],  # type: [int]
     kwargs={}  # type: {▶81⏹: int}
    ):
# type: (...) -> None
        pass

def anything_func(*args,  # type: int
     **kwargs  # type: int
    ):
# type: (...) -> None
    pass

# Enhanced Pattern-Matching

def fact_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) <= 1) and (_coconut_match_to_args[0] == 0):
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc") if "acc" in _coconut_match_to_kwargs else 1
        if (not _coconut_match_to_kwargs):
            acc = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def fact_(0, acc=1) = acc'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def fact_(0, acc=1) = acc'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return acc
@addpattern(fact_)
@_coconut_tco
def fact_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) <= 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc") if "acc" in _coconut_match_to_kwargs else 1
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            n = _coconut_match_temp_0
            acc = _coconut_match_temp_1
            _coconut_match_check = True
    if _coconut_match_check and not (n > 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def fact_(n is int, acc=1 if n > 0) = fact_(n-1, acc*n)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def fact_(n is int, acc=1 if n > 0) = fact_(n-1, acc*n)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    raise _coconut_tail_call(fact_, n - 1, acc * n)

def x_is_int(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def x_is_int(x is int) = x'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def x_is_int(x is int) = x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x

def x_as_y(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "y" in _coconut_match_to_kwargs, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("y") if "y" in _coconut_match_to_kwargs else _coconut_match_to_kwargs.pop("x")
        if (not _coconut_match_to_kwargs):
            y = _coconut_match_temp_0
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def x_as_y(x as y) = (x, y)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def x_as_y(x as y) = (x, y)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return (x, y)

def x_y_are_int_gt_0(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if _coconut_match_check and not (x > 0 and y > 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def (x is int) `x_y_are_int_gt_0` (y is int) if x > 0 and y > 0 = (x, y)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def (x is int) `x_y_are_int_gt_0` (y is int) if x > 0 and y > 0 = (x, y)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return (x, y)

def x_is_int_def_0(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) <= 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x") if "x" in _coconut_match_to_kwargs else 0
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def x_is_int_def_0(x is int = 0) = x'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def x_is_int_def_0(x is int = 0) = x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x

def head_tail_def_none(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else [None]
        if (_coconut.isinstance(_coconut_match_temp_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_0) >= 1) and (not _coconut_match_to_kwargs):
            tail = _coconut.list(_coconut_match_temp_0[1:])
            head = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def head_tail_def_none([head] + tail = [None]) = (head, tail)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def head_tail_def_none([head] + tail = [None]) = (head, tail)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return (head, tail)

def kwd_only_x_is_int_def_0(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 0):
        _coconut_match_temp_0 = _coconut_match_to_kwargs.pop("x") if "x" in _coconut_match_to_kwargs else 0
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def kwd_only_x_is_int_def_0(*, x is int = 0) = x'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def kwd_only_x_is_int_def_0(*, x is int = 0) = x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x
