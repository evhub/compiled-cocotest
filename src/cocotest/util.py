#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x1af5a1d7

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------

import sys as _coconut_sys
import os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
import __coconut__
_coconut_sys.path.remove(_coconut_file_path)

__coconut_version__ = __coconut__.version
reduce = __coconut__.functools.reduce
takewhile = __coconut__.itertools.takewhile
dropwhile = __coconut__.itertools.dropwhile
tee = __coconut__.itertools.tee
recursive = __coconut__.recursive
datamaker = __coconut__.datamaker
consume = __coconut__.consume
MatchError = __coconut__.MatchError

# Compiled Coconut: ------------------------------------------------------------

# Imports:
import random

# Random Number Helper:
def rand_list(n):
    '''Generates A Random List Of Length n.'''
    return [random.randrange(10) for x in range(0, n)]

# Infix Functions:
plus = __coconut__.operator.__add__
mod = __coconut__.operator.__mod__
base = int
def join_with(a, b=""): return b.join(a)

# Basic Functions:
prod = __coconut__.functools.partial(reduce, __coconut__.operator.__mul__)
def zipwith(f, *args): return map(lambda items: f(*items), zip(*args))
zipsum = (lambda *args, **kwargs: __coconut__.functools.partial(map, sum)((zip)(*args, **kwargs)))
plus1 = __coconut__.functools.partial(plus, 1)
def sqrt(x): return x**0.5
def sqrt_(x): return x**0.5
square = lambda x: x**2
plus1sq = (lambda *args, **kwargs: square((plus1)(*args, **kwargs)))
sqplus1 = (lambda *args, **kwargs: plus1((square)(*args, **kwargs)))
plus1sq_ = lambda x: (square)((plus1)(x))
sqplus1_ = lambda x: (plus1)((square)(x))
clean = lambda s: s.strip()
add2 = lambda x: lambda y: x + y
def swap2(f): return lambda x, y: f(y, x)
swap2_ = lambda f: lambda x, y: f(y, x)
def same(iter1, iter2): return map(__coconut__.operator.__eq__, iter1, iter2)

# Partial Applications:
sum_ = __coconut__.functools.partial(reduce, __coconut__.operator.__add__)
add = __coconut__.functools.partial(zipwith, __coconut__.operator.__add__)

# Quick-Sorts:
def qsort1(l):
    '''Non-Functional Quick Sort.'''
    if len(l) == 0:
        return []
    else:
        split = l.pop(0)
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
    if len(l) == 0:
        return []
    else:
        head, tail = l[0], l[1:] # Python Pattern-Matching
        return (qsort2([x for x in tail if x <= head]) + [head] + qsort2([x for x in tail if x > head]))
def qsort3(l):
    """Iterator Quick Sort."""
    try:
        tail, tail_ = (tee)((iter)(l))
# Since only iter is ever called on l, and next on tail, l only has to be an iterator
        head = next(tail)
        return (__coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: qsort3((x for x in tail if x <= head)), lambda: (head,), lambda: qsort3((x for x in tail_ if x > head))))))
    except (StopIteration):
        return iter(())
def qsort4(l):
    """Match Quick Sort."""
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return l
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 1):
        tail = __coconut__.list(_coconut_match_to[1:])
        head = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return (qsort2([x for x in tail if x <= head]) + [head] + qsort2([x for x in tail if x > head]))
def qsort5(l):
    """Iterator Match Quick Sort."""
    try:
        _coconut_match_check = False
        _coconut_match_to = l
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Iterable)):
            tail = __coconut__.iter(_coconut_match_to)
            _coconut_match_iter_0 = __coconut__.tuple(__coconut__.itertools.islice(tail, 0, 1))
            if (__coconut__.len(_coconut_match_iter_0) == 1):
                head = _coconut_match_iter_0[0]
                _coconut_match_check = True
        if _coconut_match_check:
            tail, tail_ = tee(tail)
            return (__coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: qsort3((x for x in tail if x <= head)), lambda: (head,), lambda: qsort3((x for x in tail_ if x > head))))))
    except (StopIteration):
        return iter(())

# Infinite Iterators:
def repeat(elem):
    """Repeat Iterator."""
    while True:
        yield elem
def repeat_(elem):
    return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (elem,), lambda: repeat_(elem))))
def N(n=0):
    """Natural Numbers."""
    while True:
        yield n
        n += 1
def N_(n=0):
    return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (n,), lambda: N_(n + 1))))
def N__(n=0):
    it = n,
    _coconut_lazy_chain_0 = it
    it = __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: _coconut_lazy_chain_0, lambda: (N__(n + 1)))))
    return it
def preN(it):
    _coconut_lazy_chain_1 = it
    it = __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: _coconut_lazy_chain_1, lambda: (N()))))
    return it
def map_iter(func, args):
    _coconut_match_check = False
    _coconut_match_to = args
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Iterable)):
        xs = __coconut__.iter(_coconut_match_to)
        _coconut_match_iter_0 = __coconut__.tuple(__coconut__.itertools.islice(xs, 0, 1))
        if (__coconut__.len(_coconut_match_iter_0) == 1):
            x = _coconut_match_iter_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: func(x),)), lambda: map_iter(func, xs))))

# Recursive Functions:
_coconut_decorator_0 = recursive
@_coconut_decorator_0
def next_mul_of(n, x):
    if x % n == 0:
        return x
    else:
        return next_mul_of(n, x + 1)
_coconut_decorator_0 = recursive
@_coconut_decorator_0
def collatz(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return collatz(n / 2)
    else:
        return collatz(3 * n + 1)

# Data Blocks:
class preop(__coconut__.collections.namedtuple("preop", "x, y")):
    __slots__ = ()
    def add(self):
        return self.x + self.y
class vector(__coconut__.collections.namedtuple("vector", "x, y")):
    __slots__ = ()
    def __new__(cls, x, y=None):
        _coconut_match_check = False
        _coconut_match_to = x
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check:
            pass
        return datamaker(cls)(x, y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5
    def transform(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check:
            return vector(self.x + x, self.y + y)
        else:
            raise TypeError()
    def __eq__(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == self.x) and (_coconut_match_to[1] == self.y):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
class triangle(__coconut__.collections.namedtuple("triangle", "a, b, c")):
    __slots__ = ()
    def is_right(self):
        return self.a**2 + self.b**2 == self.c**2
class null1(__coconut__.collections.namedtuple("null1", "")):
    __slots__ = ()
    pass
class null2(__coconut__.collections.namedtuple("null2", "")):
    __slots__ = ()
    pass
null = (null1, null2)
def is_null(item):
    _coconut_match_check = False
    _coconut_match_to = item
    if (__coconut__.isinstance(_coconut_match_to, null)) and (__coconut__.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False

# Match Functions:
def factorial1(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, (int))):
        n = _coconut_match_to
        if (n > 0):
            _coconut_match_check = True
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
        if (__coconut__.isinstance(_coconut_match_to, (int))):
            n = _coconut_match_to
            if (n > 0):
                _coconut_match_check = True
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
    if (__coconut__.isinstance(_coconut_match_to, (int))):
        n = _coconut_match_to
        if (n > 0):
            _coconut_match_check = True
    if _coconut_match_check:
        return n * factorial3(n - 1)
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return []
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 1):
        tail = __coconut__.list(_coconut_match_to[1:])
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
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, (int))):
            n = _coconut_match_to
            if (n > 0):
                _coconut_match_check = True
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
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, (int))):
            n = _coconut_match_to
            if (n > 0):
                _coconut_match_check = True
        if _coconut_match_check:
            return n * factorial5(n - 1)
    if not _coconut_match_check:
        return None
    raise TypeError()
def classify(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, (tuple))):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty tuple"
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            return "singleton tuple"
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return "duplicate pair tuple of " + str(x)
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            return "pair tuple"
        return "tuple"
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, (list))):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty list"
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            return "singleton list"
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return "duplicate pair list of " + str(x)
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            return "pair list"
        return "list"
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, (dict))):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Mapping)) and (__coconut__.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty dict"
        else:
            return "dict"
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, (set, frozenset))):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Set)) and (__coconut__.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty set"
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Set)) and (__coconut__.len(_coconut_match_to) == 1) and (0 in _coconut_match_to):
            _coconut_match_check = True
        if _coconut_match_check:
            return "set of 0"
        return "set"
    raise TypeError()
def classify_sequence(value):
    out = ""
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        out += "empty"
    if not _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            out += "singleton"
    if not _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            out += "duplicate pair of " + str(x)
    if not _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            out += "pair"
    if not _coconut_match_check:
        _coconut_match_check = False
        _coconut_match_to = value
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 3):
            _coconut_match_check = True
        if (not _coconut_match_check):
            if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 4):
                _coconut_match_check = True
        if _coconut_match_check:
            out += "few"
    if not _coconut_match_check:
        raise TypeError()
    return out
def dictpoint(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Mapping)) and (__coconut__.len(_coconut_match_to) == 2) and ("x" in _coconut_match_to) and (__coconut__.isinstance(_coconut_match_to["x"], (int))) and ("y" in _coconut_match_to) and (__coconut__.isinstance(_coconut_match_to["y"], (int))):
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
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 0):
        l = _coconut_match_to
        _coconut_match_check = True
    if (not _coconut_match_check):
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 0):
            l = _coconut_match_to
            _coconut_match_check = True
    if _coconut_match_check:
        return l
    _coconut_match_check = False
    _coconut_match_to = args
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 1):
        xs = __coconut__.tuple(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        if ((isinstance)(args, tuple)):
            _coconut_match_check = True
    if _coconut_match_check:
        return (func(x),) + map_(func, xs)
    _coconut_match_check = False
    _coconut_match_to = args
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 1):
        xs = __coconut__.list(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        if ((isinstance)(args, list)):
            _coconut_match_check = True
    if _coconut_match_check:
        return [func(x)] + map_(func, xs)
def duplicate_first1(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 1):
        l = _coconut_match_to
        xs = __coconut__.list(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return [x] + l
    else:
        raise TypeError()
def duplicate_first2(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, (list))) and (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Iterable)):
        l = _coconut_match_to
        xs = __coconut__.iter(_coconut_match_to)
        _coconut_match_iter_0 = __coconut__.tuple(__coconut__.itertools.islice(xs, 0, 1))
        if (__coconut__.len(_coconut_match_iter_0) == 1):
            x = _coconut_match_iter_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: [x], lambda: l)))
    else:
        raise TypeError()
def one_to_five(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 2) and (_coconut_match_to[0] == 1) and (_coconut_match_to[-1] == 5):
        m = __coconut__.list(_coconut_match_to[1:-1])
        _coconut_match_check = True
    if _coconut_match_check:
        return m
    else:
        return False

# Unicode Functions:
square_u = lambda x: x**2
def neg_u(x): return -x
neg_square_u = lambda x: (neg_u)((square_u)(x))

# In-Place Functions:
def pipe(a, b):
    a = (b)(a)
    return a
def compose(a, b):
    a = (lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs)))(a, (b))
    return a
def chain(a, b):
    _coconut_lazy_chain_2 = a
    a = __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: _coconut_lazy_chain_2, lambda: (b))))
    return a

# Algebraic Data Types:
class empty(__coconut__.collections.namedtuple("empty", "")):
    __slots__ = ()
    pass
class leaf(__coconut__.collections.namedtuple("leaf", "n")):
    __slots__ = ()
    pass
class node(__coconut__.collections.namedtuple("node", "l, r")):
    __slots__ = ()
    pass
tree = (empty, leaf, node)

def depth(t):
    _coconut_match_check = False
    _coconut_match_to = t
    if (__coconut__.isinstance(_coconut_match_to, tree)) and (__coconut__.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 0
    _coconut_match_check = False
    _coconut_match_to = t
    if (__coconut__.isinstance(_coconut_match_to, tree)) and (__coconut__.len(_coconut_match_to) == 1):
        n = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_check = False
    _coconut_match_to = t
    if (__coconut__.isinstance(_coconut_match_to, tree)) and (__coconut__.len(_coconut_match_to) == 2):
        l = _coconut_match_to[0]
        r = _coconut_match_to[1]
        _coconut_match_check = True
    if _coconut_match_check:
        return 1 + max([depth(l), depth(r)])

# Monads:
def base_maybe(x, f): return f(x) if x is not None else None
def maybes(*fs): return reduce(base_maybe, fs)

class Nothing(__coconut__.collections.namedtuple("Nothing", "")):
    __slots__ = ()
    def __call__(self, *args):
        return Nothing()
    def __eq__(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, Nothing)) and (__coconut__.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
class Just(__coconut__.collections.namedtuple("Just", "item")):
    __slots__ = ()
    def __call__(self, *args):
        return (Just)(reduce((lambda x, f: f(x)), args, self.item))
    def __eq__(self, other):
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, Just)) and (__coconut__.len(_coconut_match_to) == 1):
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
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 1):
        tail = __coconut__.list(_coconut_match_to[1:])
        head = _coconut_match_to[0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'match [head] + tail = l'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'match [head] + tail = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return head, tail
def init_last(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 1):
        init = __coconut__.list(_coconut_match_to[:-1])
        last = _coconut_match_to[-1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'init + [last] = l'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'init + [last] = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return init, last
def last_two(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) >= 2):
        _ = __coconut__.list(_coconut_match_to[:-2])
        a = _coconut_match_to[-2]
        b = _coconut_match_to[-1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'_ + [a, b] = l'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = '_ + [a, b] = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return a, b
def delist2(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, list)) and (__coconut__.len(_coconut_match_to) == 2):
        a = _coconut_match_to[0]
        b = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'match list(a, b) = l'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'match list(a, b) = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return a, b
def delist2_(l):
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, list)) and (__coconut__.len(_coconut_match_to) == 2):
        a = _coconut_match_to[0]
        b = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'list(a, b)  = l'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'list(a, b)  = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return a, b

# Optional Explicit Assignment:
def expl_ident(x): return x
def dictpoint_(value):
    _coconut_match_check = False
    _coconut_match_to = value
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Mapping)) and (__coconut__.len(_coconut_match_to) == 2) and ("x" in _coconut_match_to) and (__coconut__.isinstance(_coconut_match_to["x"], (int))) and ("y" in _coconut_match_to) and (__coconut__.isinstance(_coconut_match_to["y"], (int))):
        x = _coconut_match_to["x"]
        y = _coconut_match_to["y"]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " '\'{"54":x is int, "55":y is int} = value\'' " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = '{"54":x is int, "55":y is int} = value'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return x, y
def dictpoint__ (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 1) and (__coconut__.isinstance(_coconut_match_to[0], __coconut__.abc.Mapping)) and (__coconut__.len(_coconut_match_to[0]) == 2) and ("x" in _coconut_match_to[0]) and (__coconut__.isinstance(_coconut_match_to[0]["x"], (int))) and ("y" in _coconut_match_to[0]) and (__coconut__.isinstance(_coconut_match_to[0]["y"], (int))):
        x = _coconut_match_to[0]["x"]
        y = _coconut_match_to[0]["y"]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " '\'def dictpoint__({"56":x is int, "57":y is int}):\'' " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'def dictpoint__({"56":x is int, "57":y is int}):'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return x, y
def tuple1(a): return a,
def tuple1_(a): return a,
def tuple2(a, b): return a, b
def tuple2_(a, b): return a, b

# Enhanced Decorators:
_coconut_decorator_0 = lambda f: f
@_coconut_decorator_0
def dectest(x): return x

# Match Function Definition:
def last_two_ (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 1) and (__coconut__.isinstance(_coconut_match_to[0], __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to[0]) >= 2):
        _ = __coconut__.list(_coconut_match_to[0][:-2])
        a = _coconut_match_to[0][-2]
        b = _coconut_match_to[0][-1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'def last_two_(_ + [a, b]):'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'def last_two_(_ + [a, b]):'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return a, b
def htsplit (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 1) and (__coconut__.isinstance(_coconut_match_to[0], __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to[0]) >= 1):
        tail = __coconut__.list(_coconut_match_to[0][1:])
        head = _coconut_match_to[0][0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'match def htsplit([head] + tail) = [head, tail]'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'match def htsplit([head] + tail) = [head, tail]'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return [head, tail]

def htsplit_ (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 1) and (__coconut__.isinstance(_coconut_match_to[0], __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to[0]) >= 1):
        tail = __coconut__.list(_coconut_match_to[0][1:])
        head = _coconut_match_to[0][0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'def htsplit_([head] + tail) = [head, tail]'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'def htsplit_([head] + tail) = [head, tail]'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return [head, tail]

def iadd (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (__coconut__.isinstance(_coconut_match_to[0], (int))) and (__coconut__.isinstance(_coconut_match_to[1], (int))):
        x = _coconut_match_to[0]
        y = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'match def (x is int) `iadd` (y is int) = x + y'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'match def (x is int) `iadd` (y is int) = x + y'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return x + y

def iadd_ (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (__coconut__.isinstance(_coconut_match_to[0], (int))) and (__coconut__.isinstance(_coconut_match_to[1], (int))):
        x = _coconut_match_to[0]
        y = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'def (x is int) `iadd_` (y is int) = x + y'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'def (x is int) `iadd_` (y is int) = x + y'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return x + y

def strmul (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (__coconut__.isinstance(_coconut_match_to[0], (str))) and (__coconut__.isinstance(_coconut_match_to[1], (int))):
        a = _coconut_match_to[0]
        x = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'match def strmul(a is str, x is int):'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'match def strmul(a is str, x is int):'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return a * x
def strmul_ (*_coconut_match_to):
    _coconut_match_check = False
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (__coconut__.isinstance(_coconut_match_to[0], (str))) and (__coconut__.isinstance(_coconut_match_to[1], (int))):
        a = _coconut_match_to[0]
        x = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'def strmul_(a is str, x is int):'" " in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
        _coconut_match_err.pattern = 'def strmul_(a is str, x is int):'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    return a * x

# Lazy Lists:
class lazy:
    done = False
    def finish(self):
        self.done = True
    def list(self):
        return (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2, lambda: 3, lambda: self.finish()))
def is_empty(i):
    _coconut_match_check = False
    _coconut_match_to = i
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Iterable)):
        _coconut_match_iter_0 = __coconut__.tuple(_coconut_match_to)
        if (__coconut__.len(_coconut_match_iter_0) == 0):
            _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False
def is_one(i):
    _coconut_match_check = False
    _coconut_match_to = i
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Iterable)):
        _coconut_match_iter_0 = __coconut__.tuple(_coconut_match_to)
        if (__coconut__.len(_coconut_match_iter_0) == 1) and (_coconut_match_iter_0[0] == 1):
            _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False

# Constructed Data Types:
class trilen(__coconut__.collections.namedtuple("trilen", "h")):
    __slots__ = ()
    def __new__(cls, a, b):
        return (datamaker(cls))((a**2 + b**2)**0.5)

# Inheritance:
class A:
    def true(self):
        return True
class B(A):
    pass

# Infinite Grid:

class pt(__coconut__.collections.namedtuple("pt", "x, y")):
    __slots__ = ()
    """Cartesian point in the x-y plane. Immutable."""
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

def vertical_line(x=0, y=0):
    """Infinite iterator of pt representing a vertical line."""
    return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (pt(x, y),), lambda: vertical_line(x, y + 1))))

def grid(x=0):
    """Infinite iterator of infinite iterators representing cartesian space."""
    return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (vertical_line(x, 0),), lambda: grid(x + 1))))

def grid_map(func, gridsample):
    """Map a function over every point in a grid."""
    return (__coconut__.functools.partial(map, lambda l: (__coconut__.functools.partial(map, lambda p: func(p)))(l)))(gridsample)

def grid_trim(gridsample, xmax, ymax):
    """Convert a grid to a list of lists up to xmax and ymax."""
    return (list)((__coconut__.functools.partial(map, lambda l: (list)(__coconut__.itertools.islice(l, 0, ymax))))(__coconut__.itertools.islice(gridsample, 0, xmax)))
