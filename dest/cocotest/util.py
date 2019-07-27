#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x472f5261

# Compiled with Coconut version 1.4.1 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:
import random
from contextlib import contextmanager

# Random Number Helper:
def rand_list(n):
    '''Generates A Random List Of Length n.'''
    return [random.randrange(10) for x in range(0, n)]

# Infix Functions:
plus = _coconut.operator.add
mod = _coconut.operator.mod  # type: _coconut.typing.Callable[[int, int], int]
def mod_(a,  # type: int
    b,  # type: int
    ):
# type: (...) -> int
    return a % b
base = int
@_coconut_tco
def join_with(a, b=""):
    return _coconut_tail_call(b.join, a)

# Composable Functions:
plus1 = _coconut.functools.partial(plus, 1)
square = _coconut_partial(_coconut.operator.pow, {1: 2}, 2)
times2 = _coconut.functools.partial(_coconut.operator.mul, 2)

# Function Compositions:
plus1sq_1 = _coconut_forward_compose(plus1, square)  # type: ignore
sqplus1_1 = plus1
sqplus1_1 = _coconut_forward_compose((square), sqplus1_1)  # type: ignore

plus1sq_2 = lambda x: (square)((plus1)(x))  # type: ignore
sqplus1_2 = lambda x: (plus1)((square)(x))

plus1sq_3 = _coconut_base_compose(plus1, (square, 0))
sqplus1_3 = plus1
sqplus1_3 = _coconut_forward_compose((square), sqplus1_3)  # type: ignore

plus1sq_4 = _coconut_base_compose(plus1, (square, 0))
sqplus1_4 = square
sqplus1_4 = _coconut_forward_compose(sqplus1_4, (plus1))  # type: ignore

square_times2_plus1 = _coconut_base_compose(square, (times2, 0), (plus1, 0))
square_times2_plus1_ = _coconut_base_compose(square, (times2, 0), (plus1, 0))
plus1_cube = _coconut_base_compose(plus1, (lambda x: x**3, 0))

@_coconut_tco
def plus1_all(*args):
    return _coconut_tail_call(map, plus1, args)
@_coconut_tco
def square_all(*args):
    return _coconut_tail_call(map, square, args)
@_coconut_tco
def times2_all(*args):
    return _coconut_tail_call(map, times2, args)

plus1sq_all = _coconut_base_compose(plus1_all, (square_all, 1))
sqplus1_all = plus1_all
sqplus1_all = _coconut_forward_star_compose((square_all), sqplus1_all)

plus1sq_all_ = _coconut_base_compose(plus1_all, (square_all, 1))
sqplus1_all_ = square_all
sqplus1_all_ = _coconut_forward_star_compose(sqplus1_all_, (plus1_all))

square_times2_plus1_all = _coconut_base_compose(square_all, (times2_all, 1), (plus1_all, 1))
square_times2_plus1_all_ = _coconut_base_compose(square_all, (times2_all, 1), (plus1_all, 1))

plus1_square_times2_all = _coconut_forward_star_compose(plus1_all, square_all, times2_all)
plus1_square_times2_all_ = _coconut_back_star_compose(times2_all, square_all, plus1_all)

plus1sqsum_all = _coconut_base_compose(plus1_all, (square_all, 1), (sum, 0))
plus1sqsum_all_ = _coconut_base_compose(plus1_all, (square_all, 1), (sum, 0))

# Basic Functions:
product = _coconut.functools.partial(reduce, _coconut.operator.mul)
@_coconut_tco
def zipwith(f, *args):
    return _coconut_tail_call(map, lambda items: f(*items), zip(*args))
@_coconut_tco
def zipwith_(f, *args):
    return _coconut_tail_call((_coconut_forward_compose(zip, _coconut.functools.partial(starmap, f))), *args)
zipsum = _coconut_forward_compose(zip, _coconut.functools.partial(map, sum))  # type: ignore
ident = lambda x: x
_coconut_decorator_0 = _coconut_forward_compose(ident, ident)
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
clean = lambda s: s.strip()
add2 = lambda x: lambda y: x + y
def swap2(f):
    return lambda x, y: f(y, x)
swap2_ = lambda f: lambda x, y: f(y, x)
@_coconut_tco
def same(iter1, iter2):
    return _coconut_tail_call(map, _coconut.operator.eq, iter1, iter2)
def chain2(a, b):
    _coconut_yield_from = a
    for _coconut_yield_item in _coconut_yield_from:
        yield _coconut_yield_item

    _coconut_yield_from = b
    for _coconut_yield_item in _coconut_yield_from:
        yield _coconut_yield_item

def threeple(a, b, c):
    return (a, b, c)
@_coconut_tco
def toprint(*args):
    return _coconut_tail_call(" ".join, (str(a) for a in args))

# Partial Applications:
sum_ = _coconut.functools.partial(reduce, _coconut.operator.add)
add = _coconut.functools.partial(zipwith, _coconut.operator.add)
add_ = _coconut.functools.partial(zipwith_, _coconut.operator.add)

# Quick-Sorts:
def qsort1(l  # type: _coconut.typing.Sequence[int]
    ):
# type: (...) -> _coconut.typing.Sequence[int]
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
        return list(qsort1(smalls)) + [split] + list(qsort1(larges))
def qsort2(l  # type: _coconut.typing.Sequence[int]
    ):
# type: (...) -> _coconut.typing.Sequence[int]
    """Functional Quick Sort."""
    if not l:
        return []
    else:
        head, tail = l[0], l[1:]  # Python Pattern-Matching
        return (list(qsort2([x for x in tail if x <= head])) + [head] + list(qsort2([x for x in tail if x > head])))
@_coconut_tco
def qsort3(l  # type: _coconut.typing.Iterable[int]
    ):
# type: (...) -> _coconut.typing.Iterable[int]
    """Iterator Quick Sort."""
    try:
        tail, tail_ = (tee)((iter)(l))
# Since only iter is ever called on l, and next on tail, l only has to be an iterator
        head = next(tail)
        return (_coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: qsort3((x for x in tail if x <= head)), lambda: (head,), lambda: qsort3((x for x in tail_ if x > head))))))  # type: ignore
    except StopIteration:
        return _coconut_tail_call(iter, ())
def qsort4(l  # type: _coconut.typing.Sequence[int]
    ):
# type: (...) -> _coconut.typing.Sequence[int]
    """Match Quick Sort."""
    _coconut_match_to = l
    _coconut_case_check_0 = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_case_check_0 = True
    if _coconut_case_check_0:
        return l
    if not _coconut_case_check_0:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
            tail = _coconut.list(_coconut_match_to[1:])
            head = _coconut_match_to[0]
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            return (list(qsort4([x for x in tail if x <= head])) + [head] + list(qsort4([x for x in tail if x > head])))
    return None  # type: ignore
@_coconut_tco
def qsort5(l  # type: _coconut.typing.Iterable[int]
    ):
# type: (...) -> _coconut.typing.Iterable[int]
    """Iterator Match Quick Sort."""
    _coconut_match_to = l  # type: ignore
    _coconut_match_check = False  # type: ignore
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):  # type: ignore
        tail = _coconut.iter(_coconut_match_to)  # type: ignore
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))  # type: ignore
        if _coconut.len(_coconut_match_temp_0) == 1:  # type: ignore
            head = _coconut_match_temp_0[0]  # type: ignore
            _coconut_match_check = True  # type: ignore
    if _coconut_match_check:  # type: ignore
        tail, tail_ = tee(tail)
        return (_coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: qsort5((x for x in tail if x <= head)), lambda: (head,), lambda: qsort5((x for x in tail_ if x > head))))))  # type: ignore
    else:
        return _coconut_tail_call(iter, ())
def qsort6(l  # type: _coconut.typing.Iterable[int]
    ):
# type: (...) -> _coconut.typing.Iterable[int]
    _coconut_match_to = l  # type: ignore
    _coconut_match_check = False  # type: ignore
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):  # type: ignore
        tail = _coconut.iter(_coconut_match_to)  # type: ignore
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))  # type: ignore
        if _coconut.len(_coconut_match_temp_0) == 1:  # type: ignore
            head = _coconut_match_temp_0[0]  # type: ignore
            _coconut_match_check = True  # type: ignore
    if _coconut_match_check:  # type: ignore
        tail = reiterable(tail)  # type: ignore
        _coconut_yield_from = (_coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: qsort6((x for x in tail if x <= head)), lambda: (head,), lambda: qsort6((x for x in tail if x > head))))))  # type: ignore
        for _coconut_yield_item in _coconut_yield_from:  # type: ignore
            yield _coconut_yield_item  # type: ignore
# type: ignore

def empty_list_base_case(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 0):
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def empty_list_base_case([]) = []'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def empty_list_base_case([]) = []'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return []

# use separate name for base func for pickle
def _qsort7(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
        tail = _coconut.list(_coconut_match_to_args[0][1:])
        head = _coconut_match_to_args[0][0]
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def _qsort7([head] + tail) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def _qsort7([head] + tail) ='
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    left = [x for x in tail if x <= head]
    right = [x for x in tail if x > head]
    return qsort7(left) + [head] + qsort7(right)
qsort7 = addpattern(empty_list_base_case)(_qsort7)

# use separate name for base func for pickle
def _qsort8(l):
    midpt = len(l) // 2
    mid, rest = l[midpt], l[:midpt] + l[midpt + 1:]
    left = [x for x in rest if x < mid]
    right = [x for x in rest if x >= mid]
    return qsort8(left) + [mid] + qsort8(right)
qsort8 = addpattern(empty_list_base_case)(_qsort8)


# Infinite Iterators:
def repeat(elem):
    """Repeat Iterator."""
    while True:
        yield elem
@_coconut_tco
def repeat_(elem):
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: (elem,), lambda: repeat_(elem))))
def N(n=0):
    """Natural Numbers."""
    while True:
        yield n
        n += 1
@_coconut_tco
def N_(n=0):
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: (n,), lambda: N_(n + 1))))
def N__(n=0):
    it = n,
    _coconut_lazy_chain_0 = it
    it = _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: _coconut_lazy_chain_0, lambda: (N__(n + 1)))))
    return it
def preN(it):
    _coconut_lazy_chain_1 = it
    it = _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: _coconut_lazy_chain_1, lambda: (N()))))
    return it
def map_iter(func, args):
    _coconut_match_to = args
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        xs = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
        if _coconut.len(_coconut_match_temp_0) == 1:
            x = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        _coconut_yield_from = _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: (_coconut_func() for _coconut_func in (lambda: func(x),)), lambda: map_iter(func, xs))))
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


# Recursive Functions:

@_coconut_tco
def next_mul_of(n, x):
    while True:
        if x % n == 0:
            return x
        else:
            try:
                _coconut_is_recursive = next_mul_of is _coconut_recursive_func_31
            except _coconut.NameError:
                _coconut_is_recursive = False
            if _coconut_is_recursive:
                n, x = n, x + 1
                continue
            else:
                return _coconut_tail_call(next_mul_of, n, x + 1)


        return None
_coconut_recursive_func_31 = next_mul_of
@_coconut_tco
def collatz(n):
    """this is a docstring"""
    while True:
        if n == 1:
            return True
        elif n % 2 == 0:
            try:
                _coconut_is_recursive = collatz is _coconut_recursive_func_32
            except _coconut.NameError:
                _coconut_is_recursive = False
            if _coconut_is_recursive:
                n = n / 2
                continue
            else:
                return _coconut_tail_call(collatz, n / 2)

        else:
            try:
                _coconut_is_recursive = collatz is _coconut_recursive_func_32
            except _coconut.NameError:
                _coconut_is_recursive = False
            if _coconut_is_recursive:
                n = 3 * n + 1
                continue
            else:
                return _coconut_tail_call(collatz, 3 * n + 1)


        return None
_coconut_recursive_func_32 = collatz
@_coconut_tco
def recurse_n_times(n):
    """this is a docstring"""
    while True:
        if not n:
            return True
        try:
            _coconut_is_recursive = recurse_n_times is _coconut_recursive_func_33
        except _coconut.NameError:
            _coconut_is_recursive = False
        if _coconut_is_recursive:
            n = n - 1
            continue
        else:
            return _coconut_tail_call(recurse_n_times, n - 1)


        return None
_coconut_recursive_func_33 = recurse_n_times
@_coconut_tco
def is_even(n):
    if not n:
        return True
    return _coconut_tail_call(is_odd, n - 1)
@_coconut_tco
def is_odd(n):
    if not n:
        return False
    return _coconut_tail_call(is_even, n - 1)

def is_even_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def is_even_(0) = True'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def is_even_(0) = True'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return True
@_coconut_addpattern(is_even_)  # type: ignore
@_coconut_tco  # type: ignore
def is_even_(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            n = _coconut_match_temp_0  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def is_even_(n) = is_odd_(n-1)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def is_even_(n) = is_odd_(n-1)   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return _coconut_tail_call(is_odd_, n - 1)  # type: ignore

def is_odd_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def is_odd_(0) = False'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def is_odd_(0) = False'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return False
@_coconut_addpattern(is_odd_)  # type: ignore
@_coconut_tco  # type: ignore
def is_odd_(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            n = _coconut_match_temp_0  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def is_odd_(n) = is_even_(n-1)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def is_odd_(n) = is_even_(n-1)   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return _coconut_tail_call(is_even_, n - 1)  # type: ignore

# TCO/TRE tests:

@_coconut_tco
def tco_chain(it):
    return _coconut_tail_call(consume, _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: it, lambda: ["last"]))), keep_last=1)

@_coconut_tco
def partition(items, pivot, lprefix=[], rprefix=[]):
    _coconut_match_to = items
    _coconut_case_check_1 = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        tail = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))
        if _coconut.len(_coconut_match_temp_0) == 1:
            head = _coconut_match_temp_0[0]
            _coconut_case_check_1 = True
    if _coconut_case_check_1:
        if head < pivot:
            return _coconut_tail_call(partition, tail, pivot, _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: [head], lambda: lprefix))), rprefix)
        else:
            return _coconut_tail_call(partition, tail, pivot, lprefix, _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: [head], lambda: rprefix))))
    if not _coconut_case_check_1:
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
            _coconut_case_check_1 = True
        if _coconut_case_check_1:
            return lprefix, rprefix
partition_ = recursive_iterator(partition)

@_coconut_tco
def myreduce(func, items):
    _coconut_match_to = items
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        tail1 = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail1, _coconut.slice(None, 1)))
        if _coconut.len(_coconut_match_temp_0) == 1:
            first = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_to = tail1
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
            tail2 = _coconut.iter(_coconut_match_to)
            _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail2, _coconut.slice(None, 1)))
            if _coconut.len(_coconut_match_temp_0) == 1:
                second = _coconut_match_temp_0[0]
                _coconut_match_check = True
        if _coconut_match_check:
            return _coconut_tail_call(myreduce, func, _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: [func(first, second)], lambda: tail2))))
        else:
            return first

@_coconut_tco
def fake_recurse_n_times(n):
    while True:
        fake_recurse_n_times = recurse_n_times
        try:
            _coconut_is_recursive = fake_recurse_n_times is _coconut_recursive_func_41
        except _coconut.NameError:
            _coconut_is_recursive = False
        if _coconut_is_recursive:
            continue
        else:
            return _coconut_tail_call(fake_recurse_n_times, n)


        return None
_coconut_recursive_func_41 = fake_recurse_n_times
def return_in_loop(x):
    if x == 0:
        return True
    while True:
        return return_in_loop(x - 1)

class methtest(_coconut.object):
    @_coconut_tco
    def meth(self, arg):
        while True:
            try:
                _coconut_is_recursive = meth is _coconut_recursive_func_43
            except _coconut.NameError:
                _coconut_is_recursive = False
            if _coconut_is_recursive:
                continue
            else:
                return _coconut_tail_call(meth, self, arg)

            return None
    _coconut_recursive_func_43 = meth
    @_coconut_tco
    def tail_call_meth(self, arg):
        return _coconut_tail_call(self.meth, arg)
def meth(self, arg):
    return arg

# Data Blocks:
try:
    datamaker
except NameError:
    @_coconut_tco
    def datamaker(data_type):
        """Get the original constructor of the given data type or class."""
        return _coconut_tail_call(_coconut.functools.partial, makedata, data_type)

class preop(_coconut.collections.namedtuple("preop", "x y"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def add(self):
        return self.x + self.y
class vector(_coconut.collections.namedtuple("vector", "x y"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @_coconut_tco
    def __new__(cls, x, y=None  # type: _coconut.typing.Optional[int]
    ):
        _coconut_match_to = x
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check:
            pass
        return _coconut_tail_call(datamaker(cls), x, y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5
    @_coconut_tco
    def transform(self, other):
        _coconut_match_to = other
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check:
            return _coconut_tail_call(vector, self.x + x, self.y + y)
        else:
            raise TypeError()
    @_coconut_tco
    def __add__(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 2) and ("self" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[1], vector)) and (_coconut.len(_coconut_match_to_args[1]) == 2):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("self")
            x_ = _coconut_match_to_args[1][0]
            y_ = _coconut_match_to_args[1][1]
            if not _coconut_match_to_kwargs:
                self = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def __add__(self, vector(x_, y_)) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'def __add__(self, vector(x_, y_)) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(vector, self.x + x_, self.y + y_)
    @_coconut_addpattern(__add__)  # type: ignore
    @_coconut_tco  # type: ignore
    def __add__(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
        _coconut_match_check = False  # type: ignore
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "self" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "n" in _coconut_match_to_kwargs)) == 1):  # type: ignore
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("self")  # type: ignore
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("n")  # type: ignore
            if (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):  # type: ignore
                self = _coconut_match_temp_0  # type: ignore
                n = _coconut_match_temp_1  # type: ignore
                _coconut_match_check = True  # type: ignore
        if not _coconut_match_check:  # type: ignore
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def __add__(self, n is int) =   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
            _coconut_match_err.pattern = 'addpattern def __add__(self, n is int) =   # type: ignore'  # type: ignore
            _coconut_match_err.value = _coconut_match_to_args  # type: ignore
            raise _coconut_match_err  # type: ignore
# type: ignore
        return _coconut_tail_call(vector, self.x + n, self.y + n)
class triangle(_coconut.collections.namedtuple("triangle", "a b c"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def is_right(self):
        return self.a**2 + self.b**2 == self.c**2
class null1(_coconut.collections.namedtuple("null1", ""), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    pass
class null2(_coconut.collections.namedtuple("null2", ""), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    pass
null = (null1, null2)
def is_null(item):
    _coconut_match_to = item
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, null)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False
class Elems(_coconut.collections.namedtuple("Elems", "elems"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @_coconut_tco
    def __new__(cls, *elems):
        return _coconut_tail_call((datamaker(cls)), elems)
class vector_with_id(_coconut.collections.namedtuple("vector_with_id", "x y i"), vector):  # type: ignore
    __slots__ = ()  # type: ignore
    __ne__ = _coconut.object.__ne__  # type: ignore
    def __eq__(self, other):  # type: ignore
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  # type: ignore
    def __hash__(self):  # type: ignore
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  # type: ignore
# type: ignore
class vector2(_coconut.typing.NamedTuple("vector2", [("x", 'int'), ("y", 'int')]), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, x=0, y=0):
        return _coconut.tuple.__new__(_cls, (x, y))
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5

# Factorial:
def factorial1(value):
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut_match_to == 0:
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, int):
        n = _coconut_match_to
        _coconut_match_check = True
    if _coconut_match_check and not (n > 0):
        _coconut_match_check = False
    if _coconut_match_check:
        return n * factorial1(n - 1)
def factorial2(value):
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut_match_to == 0:
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    else:
        _coconut_match_to = value
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, int):
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
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut_match_to == 0:
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, int):
        n = _coconut_match_to
        _coconut_match_check = True
    if _coconut_match_check and not (n > 0):
        _coconut_match_check = False
    if _coconut_match_check:
        return n * factorial3(n - 1)
    _coconut_match_to = value
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return []
    _coconut_match_to = value
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        tail = _coconut.list(_coconut_match_to[1:])
        head = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return [factorial3(head)] + factorial3(tail)
def factorial4(value):
    _coconut_match_to = value
    _coconut_case_check_2 = False
    if _coconut_match_to == 0:
        _coconut_case_check_2 = True
    if _coconut_case_check_2:
        return 1
    if not _coconut_case_check_2:
        if _coconut.isinstance(_coconut_match_to, int):
            n = _coconut_match_to
            _coconut_case_check_2 = True
        if _coconut_case_check_2 and not (n > 0):
            _coconut_case_check_2 = False
        if _coconut_case_check_2:
            return n * factorial4(n - 1)
def factorial5(value):
    _coconut_match_to = value
    _coconut_case_check_3 = False
    if _coconut_match_to == 0:
        _coconut_case_check_3 = True
    if _coconut_case_check_3:
        return 1
    if not _coconut_case_check_3:
        if _coconut.isinstance(_coconut_match_to, int):
            n = _coconut_match_to
            _coconut_case_check_3 = True
        if _coconut_case_check_3 and not (n > 0):
            _coconut_case_check_3 = False
        if _coconut_case_check_3:
            return n * factorial5(n - 1)
    if not _coconut_case_check_3:
        return None
    raise TypeError()

@_coconut_tco  # type: ignore
def fact(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    def _coconut_mock_func(*_coconut_match_to_args, **_coconut_match_to_kwargs): return _coconut_match_to_args, _coconut_match_to_kwargs  # type: ignore
    while True:  # type: ignore
        _coconut_match_check = False  # type: ignore
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):  # type: ignore
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")  # type: ignore
            if not _coconut_match_to_kwargs:  # type: ignore
                n = _coconut_match_temp_0  # type: ignore
                _coconut_match_check = True  # type: ignore
        if not _coconut_match_check:  # type: ignore
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def fact(n) = fact(n, 1)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
            _coconut_match_err.pattern = 'match def fact(n) = fact(n, 1)   # type: ignore'  # type: ignore
            _coconut_match_err.value = _coconut_match_to_args  # type: ignore
            raise _coconut_match_err  # type: ignore
# type: ignore
        try:  # type: ignore
            _coconut_is_recursive = fact is _coconut_recursive_func_61  # type: ignore
        except _coconut.NameError:  # type: ignore
            _coconut_is_recursive = False  # type: ignore
        if _coconut_is_recursive:  # type: ignore
            _coconut_match_to_args, _coconut_match_to_kwargs = _coconut_mock_func(n, 1)  # type: ignore
            continue  # type: ignore
        else:  # type: ignore
            return _coconut_tail_call(fact, n, 1)  # type: ignore
# type: ignore
        return None  # type: ignore
_coconut_recursive_func_61 = fact  # type: ignore
@_coconut_addpattern(fact)  # type: ignore
def fact(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) == 1) and (_coconut_match_to_args[0] == 0):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc")  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            acc = _coconut_match_temp_0  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match addpattern def fact(0, acc) = acc   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'match addpattern def fact(0, acc) = acc   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return acc  # type: ignore
@_coconut_addpattern(fact)  # type: ignore
@_coconut_tco  # type: ignore
def fact(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")  # type: ignore
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc")  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            n = _coconut_match_temp_0  # type: ignore
            acc = _coconut_match_temp_1  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern match def fact(n, acc) = fact(n-1, acc*n)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern match def fact(n, acc) = fact(n-1, acc*n)   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return _coconut_tail_call(fact, n - 1, acc * n)  # type: ignore

def factorial(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) <= 1) and (_coconut_match_to_args[0] == 0):
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc") if "acc" in _coconut_match_to_kwargs else 1
        if not _coconut_match_to_kwargs:
            acc = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def factorial(0, acc=1) = acc'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def factorial(0, acc=1) = acc'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return acc
@_coconut_addpattern(factorial)  # type: ignore
@_coconut_tco  # type: ignore
def factorial(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    """this is a docstring"""
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
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
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def factorial(n is int, acc=1 if n > 0) =   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'addpattern def factorial(n is int, acc=1 if n > 0) =   # type: ignore'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(factorial, n - 1, acc * n)

# Match Functions:
def classify(value):
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, tuple):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty tuple"
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            return "singleton tuple"
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return "duplicate pair tuple of " + str(x)
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            return "pair tuple"
        return "tuple"
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, list):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty list"
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
            _coconut_match_check = True
        if _coconut_match_check:
            return "singleton list"
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return "duplicate pair list of " + str(x)
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            _coconut_match_check = True
        if _coconut_match_check:
            return "pair list"
        return "list"
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, dict):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty dict"
        else:
            return "dict"
    _coconut_match_to = value
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, (set, frozenset)):
        _coconut_match_check = True
    if _coconut_match_check:
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Set)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty set"
        _coconut_match_to = value
        _coconut_match_check = False
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Set)) and (_coconut.len(_coconut_match_to) == 1) and (0 in _coconut_match_to):
            _coconut_match_check = True
        if _coconut_match_check:
            return "set of 0"
        return "set"
    raise TypeError()
def classify_sequence(value):
    out = ""
    _coconut_match_to = value
    _coconut_case_check_4 = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_case_check_4 = True
    if _coconut_case_check_4:
        out += "empty"
    if not _coconut_case_check_4:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
            _coconut_case_check_4 = True
        if _coconut_case_check_4:
            out += "singleton"
    if not _coconut_case_check_4:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
            x = _coconut_match_to[0]
            _coconut_case_check_4 = True
        if _coconut_case_check_4:
            out += "duplicate pair of " + str(x)
    if not _coconut_case_check_4:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            _coconut_case_check_4 = True
        if _coconut_case_check_4:
            out += "pair"
    if not _coconut_case_check_4:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 3):
            _coconut_case_check_4 = True
        if (not _coconut_case_check_4) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 4):
            _coconut_case_check_4 = True
        if _coconut_case_check_4:
            out += "few"
    if not _coconut_case_check_4:
        raise TypeError()
    return out
def dictpoint(value):
    _coconut_match_to = value
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
        _coconut_match_temp_0 = _coconut_match_to.get("x", _coconut_sentinel)
        _coconut_match_temp_1 = _coconut_match_to.get("y", _coconut_sentinel)
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_1, int)):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if _coconut_match_check:
        return (x, y)
    else:
        raise TypeError()
def map_(func, args):
    _coconut_match_to = args
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        l = _coconut_match_to
        _coconut_match_check = True
    if (not _coconut_match_check) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        l = _coconut_match_to
        _coconut_match_check = True
    if _coconut_match_check:
        return l
    _coconut_match_to = args
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        xs = _coconut.tuple(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check and not ((isinstance)(args, tuple)):
        _coconut_match_check = False
    if _coconut_match_check:
        return (func(x),) + map_(func, xs)
    _coconut_match_to = args
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        xs = _coconut.list(_coconut_match_to[1:])
        x = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check and not ((isinstance)(args, list)):
        _coconut_match_check = False
    if _coconut_match_check:
        return [func(x)] + map_(func, xs)
def duplicate_first1(value):
    _coconut_match_to = value
    _coconut_match_check = False
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
    _coconut_match_to = value
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        l = _coconut_match_to
        xs = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
        if _coconut.len(_coconut_match_temp_0) == 1:
            x = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: [x], lambda: l)))
    else:
        raise TypeError()
@_coconut_tco
def duplicate_first3(value):
    _coconut_match_to = value
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        l = _coconut_match_to
        xs = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
        if _coconut.len(_coconut_match_temp_0) == 1:
            x = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: [x], lambda: l)))
    else:
        raise TypeError()
def one_to_five(l):
    _coconut_match_to = l
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 2) and (_coconut_match_to[0] == 1) and (_coconut_match_to[-1] == 5):
        m = _coconut.list(_coconut_match_to[1:-1])
        _coconut_match_check = True
    if _coconut_match_check:
        return m
    else:
        return False
def list_type(xs):
    _coconut_match_to = reiterable(xs)
    _coconut_case_check_5 = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        tail = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 2)))
        if _coconut.len(_coconut_match_temp_0) == 2:
            fst = _coconut_match_temp_0[0]
            snd = _coconut_match_temp_0[1]
            _coconut_case_check_5 = True
    if _coconut_case_check_5:
        return "at least 2"
    if not _coconut_case_check_5:
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
            tail = _coconut.iter(_coconut_match_to)
            _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))
            if _coconut.len(_coconut_match_temp_0) == 1:
                fst = _coconut_match_temp_0[0]
                _coconut_case_check_5 = True
        if _coconut_case_check_5:
            return "at least 1"
    if not _coconut_case_check_5:
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
            _coconut_match_temp_0 = _coconut.tuple(_coconut_match_to)
            if _coconut.len(_coconut_match_temp_0) == 0:
                _coconut_case_check_5 = True
        if _coconut_case_check_5:
            return "empty"

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
    a = _coconut_forward_compose((b), a)
    return a
def chain(a, b):
    _coconut_lazy_chain_2 = a
    a = _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: _coconut_lazy_chain_2, lambda: (b))))
    return a

# Algebraic Data Types:
class empty(_coconut.collections.namedtuple("empty", ""), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    pass
class leaf(_coconut.collections.namedtuple("leaf", "n"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    pass
class node(_coconut.collections.namedtuple("node", "l r"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    pass
tree = (empty, leaf, node)

def depth(t):
    _coconut_match_to = t
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, tree)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 0
    _coconut_match_to = t
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, tree)) and (_coconut.len(_coconut_match_to) == 1):
        n = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    _coconut_match_to = t
    _coconut_match_check = False
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
    return _coconut_tail_call(reduce, base_maybe, fs)

class Nothing(_coconut.collections.namedtuple("Nothing", ""), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @_coconut_tco
    def __call__(self, *args):
        return _coconut_tail_call(Nothing)
class Just(_coconut.collections.namedtuple("Just", "item"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @_coconut_tco
    def __call__(self, *args):
        return _coconut_tail_call((Just), reduce(_coconut_pipe, args, self.item))
Maybe = (Nothing, Just)

# Destructuring Assignment:
def head_tail(l):
    _coconut_match_to = l
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        tail = _coconut.list(_coconut_match_to[1:])
        head = _coconut_match_to[0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match [head] + tail = l'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match [head] + tail = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return head, tail
def init_last(l):
    _coconut_match_to = l
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        init = _coconut.list(_coconut_match_to[:-1])
        last = _coconut_match_to[-1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'init + [last] = l'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'init + [last] = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return init, last
def last_two(l):
    _coconut_match_to = l
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 2):
        a = _coconut_match_to[-2]
        b = _coconut_match_to[-1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'_ + [a, b] = l'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = '_ + [a, b] = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return a, b
def delist2(l):
    _coconut_match_to = l
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.len(_coconut_match_to) == 2):
        a = _coconut_match_to[0]
        b = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match list(a, b) = l'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match list(a, b) = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return a, b
def delist2_(l):
    _coconut_match_to = l
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.len(_coconut_match_to) == 2):
        a = _coconut_match_to[0]
        b = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'list(a, b)  = l'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'list(a, b)  = l'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return a, b

# Optional Explicit Assignment:
def expl_ident(x):
    return x
def dictpoint_(value):
    _coconut_match_to = value
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
        _coconut_match_temp_0 = _coconut_match_to.get("x", _coconut_sentinel)
        _coconut_match_temp_1 = _coconut_match_to.get("y", _coconut_sentinel)
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_1, int)):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"x":x is int, "y":y is int} = value\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = '{"x":x is int, "y":y is int} = value'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    return x, y
def dictpoint__(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to_args[0]) == 2):
        _coconut_match_temp_0 = _coconut_match_to_args[0].get("x", _coconut_sentinel)
        _coconut_match_temp_1 = _coconut_match_to_args[0].get("y", _coconut_sentinel)
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " '\'def dictpoint__({"x":x is int, "y":y is int}):\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
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
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 2):
        a = _coconut_match_to_args[0][-2]
        b = _coconut_match_to_args[0][-1]
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def last_two_(_ + [a, b]):'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def last_two_(_ + [a, b]):'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a, b
def htsplit(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
        tail = _coconut.list(_coconut_match_to_args[0][1:])
        head = _coconut_match_to_args[0][0]
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def htsplit([head] + tail) = [head, tail]'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match def htsplit([head] + tail) = [head, tail]'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return [head, tail]
def htsplit_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
        tail = _coconut.list(_coconut_match_to_args[0][1:])
        head = _coconut_match_to_args[0][0]
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def htsplit_([head] + tail) = [head, tail]'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def htsplit_([head] + tail) = [head, tail]'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return [head, tail]
def iadd(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    """this is a docstring"""
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def (x is int) `iadd` (y is int) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match def (x is int) `iadd` (y is int) ='
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x + y
def iadd_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            y = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def (x is int) `iadd_` (y is int) = x + y'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def (x is int) `iadd_` (y is int) = x + y'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x + y
def strmul(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            a = _coconut_match_temp_0
            x = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def strmul(a is str, x is int):'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match def strmul(a is str, x is int):'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a * x
def strmul_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
            a = _coconut_match_temp_0
            x = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def strmul_(a is str, x is int):'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
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
        return (_coconut_func() for _coconut_func in (lambda: 1, lambda: 2, lambda: 3, lambda: self.finish()))
def is_empty(i):
    _coconut_match_to = i
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        _coconut_match_temp_0 = _coconut.tuple(_coconut_match_to)
        if _coconut.len(_coconut_match_temp_0) == 0:
            _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False
def is_one(i):
    _coconut_match_to = i
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        _coconut_match_temp_0 = _coconut.tuple(_coconut_match_to)
        if (_coconut.len(_coconut_match_temp_0) == 1) and (_coconut_match_temp_0[0] == 1):
            _coconut_match_check = True
    if _coconut_match_check:
        return True
    else:
        return False

# Constructed Data Types:
class trilen(_coconut.collections.namedtuple("trilen", "h"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @_coconut_tco
    def __new__(cls, a, b):
        return _coconut_tail_call((datamaker(cls)), (a**2 + b**2)**0.5)

# Inheritance:
class A(_coconut.object):
    def true(self):
        return True
class B(A):
    pass

# Nesting:
class Nest(_coconut.object):
    class B(_coconut.object):
        class C(_coconut.object):
            d = "data"
            def m(self):
                return "method"
            none = None
        c = C()
    b = B()

# Infinite Grid:

class pt(_coconut.collections.namedtuple("pt", "x y"), _coconut.object):
    """Cartesian point in the x-y plane. Immutable."""
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

@_coconut_tco
def vertical_line(x=0, y=0):
    """Infinite iterator of pt representing a vertical line."""
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: (pt(x, y),), lambda: vertical_line(x, y + 1))))

@_coconut_tco
def grid(x=0):
    """Infinite iterator of infinite iterators representing cartesian space."""
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: (vertical_line(x, 0),), lambda: grid(x + 1))))

@_coconut_tco
def grid_map(func, gridsample):
    """Map a function over every point in a grid."""
    return _coconut_tail_call(map, _coconut.functools.partial(map, func), gridsample)

@_coconut_tco
def parallel_grid_map(func, gridsample):
    """Map a function over every point in a grid in parallel."""
    return _coconut_tail_call(parallel_map, _coconut.functools.partial(parallel_map, func), gridsample)

@_coconut_tco
def grid_trim(gridsample, xmax, ymax):
    """Convert a grid to a list of lists up to xmax and ymax."""
    return _coconut_tail_call((list), map(lambda l: (list)(_coconut_igetitem(l, _coconut.slice(None, ymax))), _coconut_igetitem(gridsample, _coconut.slice(None, xmax))))

# Physics function:

def SHOPeriodTerminate(X, t, params):
    if X[1] > 0:
        return -1  # passed the turning point, so go back
    epsilon = params['epsilon'] if 'epsilon' in params else 1e-8
    if abs(X[1]) < epsilon and X[0] < 0:
        return 1  # we're done
    return 0  # keep going

# Multiple dispatch:
try:
    prepattern
except NameError:
    def prepattern(base_func):
        """Decorator to add a new case to a pattern-matching function,
        where the new case is checked first."""
        @_coconut_tco
        def pattern_prepender(func):
            return _coconut_tail_call(addpattern(func), base_func)
        return pattern_prepender

def add_int_or_str_1(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def add_int_or_str_1(x is int) = x + 1'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def add_int_or_str_1(x is int) = x + 1'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x + 1
@_coconut_addpattern(add_int_or_str_1)  # type: ignore
def add_int_or_str_1(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")  # type: ignore
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (not _coconut_match_to_kwargs):  # type: ignore
            x = _coconut_match_temp_0  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " '\'addpattern def add_int_or_str_1(x is str) = x + "1"   # type: ignore\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def add_int_or_str_1(x is str) = x + "1"   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return x + "1"  # type: ignore

def coercive_add(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "b" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("b")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            a = _coconut_match_temp_0
            b = _coconut_match_temp_1
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def coercive_add(a is int, b) = a + int(b)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def coercive_add(a is int, b) = a + int(b)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return a + int(b)
@_coconut_addpattern(coercive_add)  # type: ignore
def coercive_add(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "a" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "b" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("a")  # type: ignore
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("b")  # type: ignore
        if (_coconut.isinstance(_coconut_match_temp_0, str)) and (not _coconut_match_to_kwargs):  # type: ignore
            a = _coconut_match_temp_0  # type: ignore
            b = _coconut_match_temp_1  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def coercive_add(a is str, b) = a + str(b)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def coercive_add(a is str, b) = a + str(b)   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return a + str(b)  # type: ignore

@addpattern(ident)
def still_ident(x):
    """docstring"""
    return "foo"

@prepattern(ident)
def not_ident(x):
    return "bar"

# Pattern-matching functions with guards

def pattern_abs(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if not _coconut_match_to_kwargs:
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check and not (x < 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def pattern_abs(x if x < 0) = -x'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def pattern_abs(x if x < 0) = -x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return -x
@_coconut_addpattern(pattern_abs)  # type: ignore
def pattern_abs(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            x = _coconut_match_temp_0  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def pattern_abs(x) = x   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def pattern_abs(x) = x   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return x  # type: ignore

def pattern_abs_(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if not _coconut_match_to_kwargs:
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check and not (x < 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def `pattern_abs_` (x) if x < 0 = -x'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def `pattern_abs_` (x) if x < 0 = -x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return -x
@_coconut_addpattern(pattern_abs_)  # type: ignore
def pattern_abs_(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            x = _coconut_match_temp_0  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def `pattern_abs_` (x) = x   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def `pattern_abs_` (x) = x   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return x  # type: ignore

# Recursive iterator

@recursive_iterator
@_coconut_tco
def fibs():
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: (1, 1), lambda: map(_coconut.operator.add, fibs(), _coconut_igetitem(fibs(), _coconut.slice(1, None))))))

# use separate name for base func for pickle
@_coconut_tco
def _loop(it):
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: it, lambda: loop(it))))
loop = recursive_iterator(_loop)

# Sieve Example

def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
        _coconut_match_temp_0 = _coconut.tuple(_coconut_match_to_args[0])
        if (_coconut.len(_coconut_match_temp_0) == 0) and (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def sieve((||)) = []'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def sieve((||)) = []'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return []

@prepattern(sieve)  # type: ignore
@_coconut_tco  # type: ignore
def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):  # type: ignore
        tail = _coconut.iter(_coconut_match_to_args[0])  # type: ignore
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))  # type: ignore
        if (_coconut.len(_coconut_match_temp_0) == 1) and (not _coconut_match_to_kwargs):  # type: ignore
            head = _coconut_match_temp_0[0]  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def sieve([head] :: tail) = [head] :: sieve(n for n in tail if n % head)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'def sieve([head] :: tail) = [head] :: sieve(n for n in tail if n % head)   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: [head], lambda: sieve((n for n in tail if n % head)))))  # type: ignore

# "Assignment function" definitions

def double_plus_one(x  # type: int
    ):
# type: (...) -> int
    x *= 2
    return x + 1

@_coconut_tco
def assign_func_1(f, x, y):
    @_coconut_tco
    def inner_assign_func(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 2):
            a = _coconut_match_to_args[0][0]
            b = _coconut_match_to_args[0][1]
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def inner_assign_func((a, b)) = f(a, b)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'def inner_assign_func((a, b)) = f(a, b)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(f, a, b)
    return _coconut_tail_call(inner_assign_func, (x, y))

@_coconut_tco
def assign_func_2(f, x, y):
    @_coconut_tco
    def inner_assign_func(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 2):
            a = _coconut_match_to_args[0][0]
            b = _coconut_match_to_args[0][1]
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def inner_assign_func((a, b)) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'def inner_assign_func((a, b)) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(f, a, b)
    return _coconut_tail_call(inner_assign_func, (x, y))

# Composable Functions

mul = _coconut.operator.mul
def minus(a, b):
    return b - a

# Exception Functions

def raise_exc():
    raise Exception("raise_exc")

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
            try:
                _coconut_is_recursive = ret_none is _coconut_recursive_func_130
            except _coconut.NameError:
                _coconut_is_recursive = False
            if _coconut_is_recursive:
                n = n - 1
                continue
            else:
                return _coconut_tail_call(ret_none, n - 1)


        return None
_coconut_recursive_func_130 = ret_none
def ret_args_kwargs(*args, **kwargs):
    return (args, kwargs)

# Useful Classes

class identity_operations(_coconut.object):
    def __getitem__(self, args):
        return args
    def method(self, *args, **kwargs):
        return (args, kwargs)
identity = identity_operations()

class container(_coconut.object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return isinstance(other, container) and self.x == other.x

class container_(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return isinstance(other, container_) and self.x == other.x

class counter(_coconut.object):
    count = 0
    def inc(self):
        self.count += 1

# Typing
if TYPE_CHECKING:
    from typing import List
    from typing import Dict
    from typing import Any

def args_kwargs_func(args=[],  # type: List[Any]
     kwargs={}  # type: Dict[Any, Any]
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
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) <= 1) and (_coconut_match_to_args[0] == 0):
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc") if "acc" in _coconut_match_to_kwargs else 1
        if not _coconut_match_to_kwargs:
            acc = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def fact_(0, acc=1) = acc'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def fact_(0, acc=1) = acc'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return acc
@_coconut_addpattern(fact_)  # type: ignore
@_coconut_tco  # type: ignore
def fact_(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "acc" in _coconut_match_to_kwargs)) <= 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")  # type: ignore
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("acc") if "acc" in _coconut_match_to_kwargs else 1  # type: ignore
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):  # type: ignore
            n = _coconut_match_temp_0  # type: ignore
            acc = _coconut_match_temp_1  # type: ignore
            _coconut_match_check = True  # type: ignore
    if _coconut_match_check and not (n > 0):  # type: ignore
        _coconut_match_check = False  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def fact_(n is int, acc=1 if n > 0) = fact_(n-1, acc*n)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def fact_(n is int, acc=1 if n > 0) = fact_(n-1, acc*n)   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return _coconut_tail_call(fact_, n - 1, acc * n)  # type: ignore

def x_is_int(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def x_is_int(x is int) = x'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def x_is_int(x is int) = x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x

def x_as_y(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "y" in _coconut_match_to_kwargs, "x" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("y") if "y" in _coconut_match_to_kwargs else _coconut_match_to_kwargs.pop("x")
        if not _coconut_match_to_kwargs:
            y = _coconut_match_temp_0
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def x_as_y(x as y) = (x, y)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def x_as_y(x as y) = (x, y)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return (x, y)

def x_y_are_int_gt_0(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
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
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def (x is int) `x_y_are_int_gt_0` (y is int) if x > 0 and y > 0 = (x, y)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def (x is int) `x_y_are_int_gt_0` (y is int) if x > 0 and y > 0 = (x, y)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return (x, y)

def x_is_int_def_0(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) <= 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x") if "x" in _coconut_match_to_kwargs else 0
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def x_is_int_def_0(x is int = 0) = x'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def x_is_int_def_0(x is int = 0) = x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x

def head_tail_def_none(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if _coconut.len(_coconut_match_to_args) <= 1:
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else [None]
        if (_coconut.isinstance(_coconut_match_temp_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_0) >= 1) and (not _coconut_match_to_kwargs):
            tail = _coconut.list(_coconut_match_temp_0[1:])
            head = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def head_tail_def_none([head] + tail = [None]) = (head, tail)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def head_tail_def_none([head] + tail = [None]) = (head, tail)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return (head, tail)

def kwd_only_x_is_int_def_0(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if _coconut.len(_coconut_match_to_args) == 0:
        _coconut_match_temp_0 = _coconut_match_to_kwargs.pop("x") if "x" in _coconut_match_to_kwargs else 0
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def kwd_only_x_is_int_def_0(*, x is int = 0) = x'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match def kwd_only_x_is_int_def_0(*, x is int = 0) = x'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return x

def no_args_kwargs(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.isinstance(_coconut_match_to_args[0:], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0:]) == 0):
        if (_coconut.isinstance(_coconut_match_to_kwargs, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to_kwargs) == 0):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def no_args_kwargs(*(), **{}) = True'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def no_args_kwargs(*(), **{}) = True'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return True

# Alternative Class Notation

class altclass(_coconut.object):
    func = None  # type: _coconut.typing.Callable[[Any, Any], Any]
    zero = None  # type: _coconut.typing.Callable[[Any, int], int]

def func(self, x):
    return x

altclass.func = func
@_coconut_tco
def zero(self, x  # type: int
    ):
# type: (...) -> int
    while True:
        if x == 0:
            return 0
        try:  # tail recursive
            _coconut_is_recursive = altclass.zero is _coconut_recursive_func_150  # tail recursive
        except _coconut.NameError:  # tail recursive
            _coconut_is_recursive = False  # tail recursive
        if _coconut_is_recursive:  # tail recursive
            self, x = self, x - 1  # tail recursive
            continue  # tail recursive
        else:  # tail recursive
            return _coconut_tail_call(altclass.zero, self, x - 1)  # tail recursive
# tail recursive

# Logic Stuff

        return None
_coconut_recursive_func_150 = zero
altclass.zero = zero
class Vars(_coconut.object):
    var_one = 1

    @classmethod
    def items(cls):
        for name, var in vars(cls).items():
            if not name.startswith("_"):
                yield name, var
    @classmethod
    def use(cls, globs=None):
        """Put variables into the global namespace."""
        if globs is None:
            globs = globals()
        for name, var in cls.items():
            globs[name] = var
    @classmethod
    @contextmanager
    def using(cls, globs=None):
        """Temporarily put variables into the global namespace."""
        if globs is None:
            globs = globals()
        prevars = {}
        for name, var in cls.items():
            if name in globs:
                prevars[name] = globs[name]
            globs[name] = var
        try:
            yield
        finally:
            for name, var in cls.items():
                if name in prevars:
                    globs[name] = prevars[name]
                else:
                    del globs[name]

# Complex Data

class Tuple_(_coconut.collections.namedtuple("Tuple_", "elems"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *elems):
        return _coconut.tuple.__new__(_cls, elems)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=None):
        return new(cls, iterable)
    def _asdict(self):
        return _coconut.OrderedDict([("elems", self[:])])
    def __repr__(self):
        return "Tuple_(*elems=%r)" % (self[:],)
    def _replace(_self, **kwds):
        result = self._make(kwds.pop("elems", _self))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: " + _coconut.repr(kwds.keys()))
        return result
    @_coconut.property
    def elems(self):
        return self[:]


class Pred(_coconut.collections.namedtuple("Pred", "name args"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, name, *args):
        return _coconut.tuple.__new__(_cls, (name,) + args)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=_coconut.len):
        result = new(cls, iterable)
        if len(result) < 1:
            raise _coconut.TypeError("Expected at least 1 argument(s), got %d" % len(result))
        return result
    def _asdict(self):
        return _coconut.OrderedDict((f, _coconut.getattr(self, f)) for f in self._fields)
    def __repr__(self):
        return "Pred(name={name!r}, *args={args!r})".format(**self._asdict())
    def _replace(_self, **kwds):
        result = _self._make(_coconut.tuple(_coconut.map(kwds.pop, ("name",), _self)) + kwds.pop("args", self.args))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: " + _coconut.repr(kwds.keys()))
        return result
    @_coconut.property
    def args(self):
        return self[1:]

class Pred_(_coconut.typing.NamedTuple("Pred_", [("name", 'str'), ("args", '_coconut.typing.Any')]), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, name, *args):
        return _coconut.tuple.__new__(_cls, (name,) + args)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=_coconut.len):
        result = new(cls, iterable)
        if len(result) < 1:
            raise _coconut.TypeError("Expected at least 1 argument(s), got %d" % len(result))
        return result
    def _asdict(self):
        return _coconut.OrderedDict((f, _coconut.getattr(self, f)) for f in self._fields)
    def __repr__(self):
        return "Pred_(name={name!r}, *args={args!r})".format(**self._asdict())
    def _replace(_self, **kwds):
        result = _self._make(_coconut.tuple(_coconut.map(kwds.pop, ("name",), _self)) + kwds.pop("args", self.args))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: " + _coconut.repr(kwds.keys()))
        return result
    @_coconut.property
    def args(self):
        return self[1:]


class Quant(_coconut.collections.namedtuple("Quant", "name var args"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, name, var, *args):
        return _coconut.tuple.__new__(_cls, (name, var) + args)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=_coconut.len):
        result = new(cls, iterable)
        if len(result) < 2:
            raise _coconut.TypeError("Expected at least 2 argument(s), got %d" % len(result))
        return result
    def _asdict(self):
        return _coconut.OrderedDict((f, _coconut.getattr(self, f)) for f in self._fields)
    def __repr__(self):
        return "Quant(name={name!r}, var={var!r}, *args={args!r})".format(**self._asdict())
    def _replace(_self, **kwds):
        result = _self._make(_coconut.tuple(_coconut.map(kwds.pop, ("name", "var"), _self)) + kwds.pop("args", self.args))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: " + _coconut.repr(kwds.keys()))
        return result
    @_coconut.property
    def args(self):
        return self[2:]

class Quant_(_coconut.typing.NamedTuple("Quant_", [("name", 'str'), ("var", 'str'), ("args", '_coconut.typing.Any')]), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, name, var, *args):
        return _coconut.tuple.__new__(_cls, (name, var) + args)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=_coconut.len):
        result = new(cls, iterable)
        if len(result) < 2:
            raise _coconut.TypeError("Expected at least 2 argument(s), got %d" % len(result))
        return result
    def _asdict(self):
        return _coconut.OrderedDict((f, _coconut.getattr(self, f)) for f in self._fields)
    def __repr__(self):
        return "Quant_(name={name!r}, var={var!r}, *args={args!r})".format(**self._asdict())
    def _replace(_self, **kwds):
        result = _self._make(_coconut.tuple(_coconut.map(kwds.pop, ("name", "var"), _self)) + kwds.pop("args", self.args))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: " + _coconut.repr(kwds.keys()))
        return result
    @_coconut.property
    def args(self):
        return self[2:]


class Point(_coconut.collections.namedtuple("Point", "x y"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, x=0, y=0):
        return _coconut.tuple.__new__(_cls, (x, y))

class Point_(_coconut.typing.NamedTuple("Point_", [("x", 'int'), ("y", 'int')]), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, x=0, y=0):
        return _coconut.tuple.__new__(_cls, (x, y))


class RadialVector(_coconut.collections.namedtuple("RadialVector", "mag angle"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, mag, angle=0):
        return _coconut.tuple.__new__(_cls, (mag, angle))

class RadialVector_(_coconut.typing.NamedTuple("RadialVector_", [("mag", 'int'), ("angle", 'int')]), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, mag, angle=0):
        return _coconut.tuple.__new__(_cls, (mag, angle))


class ABC(_coconut.collections.namedtuple("ABC", "a b c"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, a, b=1, *c):
        return _coconut.tuple.__new__(_cls, (a, b) + c)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=_coconut.len):
        result = new(cls, iterable)
        if len(result) < 1:
            raise _coconut.TypeError("Expected at least 1 argument(s), got %d" % len(result))
        return result
    def _asdict(self):
        return _coconut.OrderedDict((f, _coconut.getattr(self, f)) for f in self._fields)
    def __repr__(self):
        return "ABC(a={a!r}, b={b!r}, *c={c!r})".format(**self._asdict())
    def _replace(_self, **kwds):
        result = _self._make(_coconut.tuple(_coconut.map(kwds.pop, ("a", "b"), _self)) + kwds.pop("c", self.c))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: " + _coconut.repr(kwds.keys()))
        return result
    @_coconut.property
    def c(self):
        return self[2:]

class ABC_(_coconut.typing.NamedTuple("ABC_", [("a", 'int'), ("b", 'int'), ("c", '_coconut.typing.Any')]), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, a, b=1, *c):
        return _coconut.tuple.__new__(_cls, (a, b) + c)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=_coconut.len):
        result = new(cls, iterable)
        if len(result) < 1:
            raise _coconut.TypeError("Expected at least 1 argument(s), got %d" % len(result))
        return result
    def _asdict(self):
        return _coconut.OrderedDict((f, _coconut.getattr(self, f)) for f in self._fields)
    def __repr__(self):
        return "ABC_(a={a!r}, b={b!r}, *c={c!r})".format(**self._asdict())
    def _replace(_self, **kwds):
        result = _self._make(_coconut.tuple(_coconut.map(kwds.pop, ("a", "b"), _self)) + kwds.pop("c", self.c))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: " + _coconut.repr(kwds.keys()))
        return result
    @_coconut.property
    def c(self):
        return self[2:]


# Type-Checking Tests

any_to_ten = lambda *args, **kwargs: 10  # type: _coconut.typing.Callable[..., int]
none_to_ten = lambda: 10  # type: _coconut.typing.Callable[[], int]

@_coconut_tco
def int_map(f,  # type: _coconut.typing.Callable[[int], int]
     xs  # type: _coconut.typing.Sequence[int]
    ):
# type: (...) -> _coconut.typing.Sequence[int]
    return _coconut_tail_call(list, map(f, xs))

@_coconut_tco
def sum_list_range(n  # type: int
    ):
# type: (...) -> int
    return _coconut_tail_call(sum, [i for i in range(1, n)])

# Context managers
@_coconut_tco
def context_produces(out):
    @contextmanager
    def manager():
        yield out
    return _coconut_tail_call(manager)

# Where statements
def sum2(ab):
    a, b = ab

# Memoization
    return a + b
import functools

@memoize()
def ridiculously_recursive(n):
    """Requires maxsize=None when called on large numbers."""
    if n <= 0:
        return 1
    result = 0
    for i in range(1, 200):
        result += ridiculously_recursive(n - i)
    return result

@functools.lru_cache(maxsize=None)  # type: ignore
def ridiculously_recursive_(n):
    """Requires maxsize=None when called on large numbers."""
    if n <= 0:
        return 1
    result = 0
    for i in range(1, 200):
        result += ridiculously_recursive_(n - i)
    return result

def fib(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")
        if not _coconut_match_to_kwargs:
            n = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check and not (n < 2):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def fib(n if n < 2) = n'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def fib(n if n < 2) = n'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return n

@memoize()  # type: ignore
@_coconut_addpattern(fib)  # type: ignore
def fib(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):  # type: ignore
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            n = _coconut_match_temp_0  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def fib(n) = fib(n-1) + fib(n-2)   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def fib(n) = fib(n-1) + fib(n-2)   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    return fib(n - 1) + fib(n - 2)  # type: ignore

# MapReduce
from collections import defaultdict

def _coconut_lambda_0(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 2) and ("acc" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[1]) == 2):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("acc")
        k = _coconut_match_to_args[1][0]
        v = _coconut_match_to_args[1][1]
        if not _coconut_match_to_kwargs:
            acc = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'join_pairs1 = reduce$((def (acc, (k, v)) ->     acc[k] += v;     acc ), ?, defaultdict(list))'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'join_pairs1 = reduce$((def (acc, (k, v)) ->     acc[k] += v;     acc ), ?, defaultdict(list))'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err
    acc[k] += v
    return acc
join_pairs1 = _coconut_partial(reduce, {0: (_coconut_lambda_0), 2: defaultdict(list)}, 3)

@_coconut_tco
def join_pairs2(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 0):
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def join_pairs2([]) = defaultdict(list)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def join_pairs2([]) = defaultdict(list)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(defaultdict, list)
@_coconut_addpattern(join_pairs2)  # type: ignore
def join_pairs2(*_coconut_match_to_args, **_coconut_match_to_kwargs):  # type: ignore
    _coconut_match_check = False  # type: ignore
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  # type: ignore
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1) and (_coconut.isinstance(_coconut_match_to_args[0][0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0][0]) == 2):  # type: ignore
        tail = _coconut.list(_coconut_match_to_args[0][1:])  # type: ignore
        k = _coconut_match_to_args[0][0][0]  # type: ignore
        v = _coconut_match_to_args[0][0][1]  # type: ignore
        if not _coconut_match_to_kwargs:  # type: ignore
            _coconut_match_check = True  # type: ignore
    if not _coconut_match_check:  # type: ignore
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)  # type: ignore
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def join_pairs2([(k, v)] + tail) =   # type: ignore'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))  # type: ignore
        _coconut_match_err.pattern = 'addpattern def join_pairs2([(k, v)] + tail) =   # type: ignore'  # type: ignore
        _coconut_match_err.value = _coconut_match_to_args  # type: ignore
        raise _coconut_match_err  # type: ignore
# type: ignore
    result = join_pairs2(tail)
    result[k] += v
    return result


# Match data
class data1(_coconut.collections.namedtuple("data1", "x"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                _coconut_match_check = True

        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match data data1(x)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match data data1(x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.tuple.__new__(_cls, (x,))


class data2(_coconut.collections.namedtuple("data2", "x"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
                x = _coconut_match_temp_0
                _coconut_match_check = True

        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'data data2(x is int)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'data data2(x is int)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.tuple.__new__(_cls, (x,))


class data3(_coconut.collections.namedtuple("data3", "xs"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        xs = _coconut_match_to_args[0:]
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True

        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match data data3(*xs)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match data data3(*xs)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.tuple.__new__(_cls, (xs,))


class data4(_coconut.collections.namedtuple("data4", "kws"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if _coconut.len(_coconut_match_to_args) == 0:
            kws = _coconut_match_to_kwargs
            _coconut_match_check = True

        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'data data4(**kws)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'data data4(**kws)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.tuple.__new__(_cls, (kws,))


class data5(_coconut.collections.namedtuple("data5", "x, y, z"), _coconut.object):
    """docstring"""
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 2, "z" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
            _coconut_match_temp_2 = _coconut_match_to_args[2] if _coconut.len(_coconut_match_to_args) > 2 else _coconut_match_to_kwargs.pop("z")
            if (_coconut.isinstance(_coconut_match_temp_1, int)) and (_coconut.isinstance(_coconut_match_temp_2, str)) and (not _coconut_match_to_kwargs):
                x = _coconut_match_temp_0
                y = _coconut_match_temp_1
                z = _coconut_match_temp_2
                _coconut_match_check = True

        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'data data5(x, y is int, z is str):'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'data data5(x, y is int, z is str):'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.tuple.__new__(_cls, (x, y, z))
    attr = 1

class BaseClass(_coconut.object): pass

class data6(_coconut.collections.namedtuple("data6", "x"), BaseClass):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
                x = _coconut_match_temp_0
                _coconut_match_check = True

        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'data data6(x is int) from BaseClass'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'data data6(x is int) from BaseClass'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.tuple.__new__(_cls, (x,))


class namedpt(_coconut.collections.namedtuple("namedpt", "name, x, y"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    def __new__(_cls, *_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "name" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 2, "y" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("name")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("x")
            _coconut_match_temp_2 = _coconut_match_to_args[2] if _coconut.len(_coconut_match_to_args) > 2 else _coconut_match_to_kwargs.pop("y")
            if (_coconut.isinstance(_coconut_match_temp_0, str)) and (_coconut.isinstance(_coconut_match_temp_1, int)) and (_coconut.isinstance(_coconut_match_temp_2, int)) and (not _coconut_match_to_kwargs):
                name = _coconut_match_temp_0
                x = _coconut_match_temp_1
                y = _coconut_match_temp_2
                _coconut_match_check = True

        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'data namedpt(name is str, x is int, y is int):'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'data namedpt(name is str, x is int, y is int):'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.tuple.__new__(_cls, (name, x, y))
    def mag(self):
        return (self.x**2 + self.y**2)**0.5


# Descriptor test
def tuplify(*args):
    return args

class descriptor_test(_coconut.object):
    lam = lambda self: self
    comp = _coconut_forward_compose(ident, tuplify)

    @recursive_iterator
    @_coconut_tco
    def N(self, i=0):
        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: [(self, i)], lambda: self.N(i + 1))))
