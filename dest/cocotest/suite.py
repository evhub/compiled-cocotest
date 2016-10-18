#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb5a62c08

# Compiled with Coconut version 1.2.0-post_dev13 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_tee, _coconut_map
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

from .util import *

def suite_test():
    """Executes the main test suite."""
    assert (plus)(1, 1) == 2 == (_coconut.operator.add)(1, 1)
    assert (plus)("1", "1") == "11" == (_coconut.operator.add)("1", "1")
    assert (mod)(3, 6) == 3 == (_coconut.operator.mod)(3, 6)
    assert (mod)(5, 4) == 1 == (mod_)(5, 4)
    assert (mod)(5, (plus)(2, 2)) == 1 == (_coconut.operator.mod)(5, (_coconut.operator.add)(2, 2))
    assert (base)("11", 2) == 3
    assert (int)("10A", 12) == 154
    assert (join_with)(["1", "2"], ", ") == "1, 2"
    assert (join_with)(["a", "b", "c"]) == "abc"
    assert (len)(_coconut.set(("a", 5))) == 2
    assert _coconut.operator.mul(2, swap2(_coconut_minus)(2, 5)) == 6 == _coconut.operator.mul(2, swap2_(_coconut_minus)(2, 5))
    assert all(same((1, 2, 3), [1, 2, 3]))
    assert (list)(chain2((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 3, lambda: 4)))) == [1, 2, 3, 4]
    assert (prod)((range)(1, 5)) == 24
    assert plus1(4) == 5 == plus1_(4)
    assert (plus1)(2) == 3 == plus1(2)
    assert plus1(plus1(5)) == 7 == (_coconut_compose(plus1, plus1))(5)
    assert (sqrt)(16) == 4 == (sqrt_)(16)
    assert (square)(3) == 9
    assert sqplus1(3) == 10 == (_coconut_compose(plus1, square))(3)
    assert (plus1sq)(3) == 16 == (plus1sq_)(3)
    assert (sqplus1)(3) == 10 == (sqplus1_)(3)
    assert (square)((plus1)(3)) == 16 == (square)((plus1_)(3))
    assert reduce(_coconut_pipe, [3, plus1, square]) == 16 == pipe(pipe(3, plus1), square)
    assert reduce(_coconut_compose, [sqrt, square, plus1])(3) == 4 == compose(compose(sqrt, square), plus1)(3)
    assert sum_([1, 7, 3, 5]) == 16
    assert ((list)(add([1, 2, 3], [10, 20, 30])) == [11, 22, 33] == (list)(zipsum([1, 2, 3], [10, 20, 30])))
    assert clean("   ab cd ef   ") == "ab cd ef" == (clean)("   ab cd ef   ")
    assert ((add2)(2))(3) == 5
    for qsort in [qsort1, qsort2, qsort3, qsort4, qsort5]:
        to_sort = rand_list(10)
        assert (tuple)((qsort)(to_sort)) == (tuple)((sorted)(to_sort))
    assert _coconut_igetitem(repeat(3), 2) == 3 == _coconut_igetitem(repeat_(3), 2)
    assert sum_(_coconut_igetitem(repeat(1), _coconut.slice(None, 5))) == 5 == sum_(_coconut_igetitem(repeat_(1), _coconut.slice(None, 5)))
    assert (sum_(takewhile(lambda x: x < 5, N())) == 10 == (sum)(_coconut_igetitem(dropwhile(_coconut.functools.partial(_coconut.operator.gt, (0)), (_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: range(-10, 0), lambda: N()))))), _coconut.slice(None, 5))))
    assert (sum_)(((lambda s: map(_coconut.functools.partial(_coconut.operator.getitem, s), (1, 3, 5))))("ABCDEFG")) == "BDF"
    assert (list)(_coconut_igetitem(N(), _coconut.slice(10, 15))) == [10, 11, 12, 13, 14] == (list)(_coconut_igetitem(N_(), _coconut.slice(10, 15)))
    assert ((list)(takewhile(_coconut.functools.partial(_coconut.operator.gt, (5)), N())) == [0, 1, 2, 3, 4] == (list)(_coconut_igetitem(range(0, 10), _coconut.slice(None, 5, None))))
    assert (sum)(_coconut_igetitem((_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: range(-10, 0), lambda: N())))), _coconut.slice(5, 15))) == -5 == (sum)(_coconut_igetitem(chain(range(-10, 0), N()), _coconut.slice(5, 15)))
    assert (list)(_coconut_igetitem(add(repeat(1), N()), _coconut.slice(None, 5))) == [1, 2, 3, 4, 5] == (list)(_coconut_igetitem(add(repeat(1), N_()), _coconut.slice(None, 5)))
    assert sum(_coconut_igetitem(_coconut_igetitem(N(), _coconut.slice(5, None)), _coconut.slice(None, 5))) == 35 == sum(_coconut_igetitem(_coconut_igetitem(N_(), _coconut.slice(5, None)), _coconut.slice(None, 5)))
    assert (list)(_coconut.functools.partial(_coconut_igetitem, N())(slice(5, 10))) == [5, 6, 7, 8, 9] == _coconut.functools.partial(_coconut.operator.getitem, list(range(0, 15)))(slice(5, 10))
    assert (list)(_coconut_igetitem(N(), slice(5, 10))) == [5, 6, 7, 8, 9] == list(range(0, 15))[slice(5, 10)]
    assert (list)(_coconut_igetitem(preN(range(-5, 0)), _coconut.slice(1, 10))) == [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    assert (list)(_coconut_igetitem(map_iter(_coconut.functools.partial(_coconut.operator.mul, (2)), N()), _coconut.slice(None, 5))) == [0, 2, 4, 6, 8]
    assert (tuple)(_coconut_igetitem(N(), _coconut.slice(None, 100))) == (tuple)(_coconut_igetitem(N_(), _coconut.slice(None, 100))) == (tuple)(_coconut_igetitem(N__(), _coconut.slice(None, 100)))
    assert next_mul_of(5, 12) == 15
    assert collatz(27)
    assert preop(1, 2).add() == 3
    assert (abs)(vector(3, 4)) == 5
    assert (tuple)(((lambda v: map(_coconut.functools.partial(_coconut.getattr, v), ("x", "y"))))(vector(1, 2))) == (1, 2)
    assert (tuple)(((lambda v: map(_coconut.functools.partial(_coconut.operator.getitem, v), (0, 1))))((vector(1, 2).transform)(vector(3, 1)))) == (4, 3)
    assert (vector(1, 2).__eq__)(vector(1, 2))
    assert not (vector(3, 4).__eq__)(vector(1, 2))
    assert not (vector(1, 2).__eq__)((1, 2))
    assert vector(vector(4, 3)) == vector(4, 3)
    assert triangle(3, 4, 5).is_right()
    assert _coconut.getattr(triangle(3, 4, 5), "is_right")
    assert (_coconut.operator.methodcaller("is_right"))(triangle(3, 4, 5))
    assert factorial1(3) == 6
    assert factorial2(3) == 6
    assert factorial4(3) == 6
    assert factorial5(3) == 6
    assert fact(3) == 6
    assert factorial1(-1) is None
    assert factorial2(-1) is None
    assert factorial4(-1) is None
    assert factorial5(-1) is None
    assert factorial3([2, 3]) == [2, 6] == factorial3((2, 3))
    assert classify(()) == "empty tuple"
    assert classify([]) == "empty list"
    assert classify((1,)) == "singleton tuple"
    assert classify([1, 1]) == "duplicate pair list of 1"
    assert classify((1, 2)) == "pair tuple"
    assert classify([1, 2, 3]) == "list"
    assert classify((1, 1, 1)) == "tuple"
    assert classify({}) == "empty dict"
    assert classify({"a": 1}) == "dict"
    assert classify(_coconut.set((0,))) == "set of 0" == classify(_coconut.frozenset((0,)))
    assert classify(_coconut.set((0, 1))) == "set" == classify(_coconut.frozenset((1,)))
    assert classify(_coconut.set()) == "empty set" == classify(_coconut.frozenset())
    assert classify_sequence(()) == "empty"
    assert classify_sequence((1,)) == "singleton"
    assert classify_sequence((1, 1)) == "duplicate pair of 1"
    assert classify_sequence((1, 2)) == "pair"
    assert classify_sequence((1, 2, 3)) == "few"
    assert dictpoint({"x": 1, "y": 2}) == (1, 2)
    assert dictpoint_({"x": 1, "y": 2}) == (1, 2) == dictpoint__({"x": 1, "y": 2})
    assert map_(_coconut.functools.partial(_coconut.operator.add, (1)), []) == []
    assert map_(_coconut.functools.partial(_coconut.operator.add, (1)), ()) == ()
    assert map_(_coconut.functools.partial(_coconut.operator.add, (1)), [0, 1, 2, 3]) == [1, 2, 3, 4]
    assert map_(_coconut.functools.partial(_coconut.operator.add, (1)), (0, 1, 2, 3)) == (1, 2, 3, 4)
    assert duplicate_first1([1, 2, 3]) == [1, 1, 2, 3]
    assert (list)(duplicate_first2([1, 2, 3])) == [1, 1, 2, 3] == (list)(duplicate_first3([1, 2, 3]))
    assert one_to_five([1, 2, 3, 4, 5]) == [2, 3, 4]
    assert not one_to_five([0, 1, 2, 3, 4, 5])
    assert one_to_five([1, 5]) == []
    assert -4 == neg_square_u(2) != 4 & 0 <= neg_square_u(0) <= 0
    assert is_null(null1())
    assert is_null(null2())
    assert (depth)(empty()) == 0
    assert (depth)(leaf(5)) == 1
    assert (depth)(node(leaf(2), node(empty(), leaf(3)))) == 3
    assert maybes(5, square, plus1) == 26
    assert maybes(None, square, plus1) is None
    assert (square)(2) == 4
    assert (mod)(*(5, 3)) == 2 == (mod)(*(5, 3))
    assert ((Just(5))(square))(plus1) == Just(26)
    assert ((Nothing())(square))(plus1) == Nothing()
    assert head_tail([1, 2, 3]) == (1, [2, 3])
    assert init_last([1, 2, 3]) == ([1, 2], 3)
    assert last_two([1, 2, 3]) == (2, 3) == last_two_([1, 2, 3])
    assert expl_ident(5) == 5
    assert ((_coconut.functools.partial(_coconut.functools.partial, mod))(5))(3) == 2 == ((_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.mod))(5))(3)
    assert (dectest)(5) == 5
    try:
        raise ValueError()
    except (TypeError, ValueError) as err:
        assert err
    else:
        assert False
    assert delist2([1, 2]) == (1, 2) == delist2_([1, 2])
    assert tuple1(1) == (1,) == tuple1_(1)
    assert tuple2(1, 2) == (1, 2) == tuple2_(1, 2)
    assert htsplit([1, 2, 3]) == [1, [2, 3]] == htsplit_([1, 2, 3])
    assert iadd(1, 2) == 3 == iadd_(1, 2)
    assert strmul("a", 3) == "aaa" == strmul_("a", 3)
    try:
        strmul("a", "b")
    except MatchError as err:
        assert err.pattern == "match def strmul(a is str, x is int):"
        assert err.value == ("a", "b")
    else:
        assert False
    laz = lazy()
    assert not laz.done
    lazl = laz.list()
    assert (list)(_coconut_igetitem(lazl, _coconut.slice(None, 3))) == [1, 2, 3]
    assert not laz.done
    assert (list)(lazl) == [None]
    assert laz.done
    assert is_empty(iter(()))
    assert is_empty(())
    assert not is_empty([1])
    assert is_one(iter([1]))
    assert not is_one(iter(()))
    assert not is_one([])
    assert is_one([1])
    assert trilen(3, 4).h == 5 == datamaker(trilen)(5).h
    assert A().true()
    assert B().true()
    assert pt.__doc__
    out0 = grid_trim(grid(), xmax=5, ymax=5)
    assert out0 == [[pt(x=0, y=0), pt(x=0, y=1), pt(x=0, y=2), pt(x=0, y=3), pt(x=0, y=4)], [pt(x=1, y=0), pt(x=1, y=1), pt(x=1, y=2), pt(x=1, y=3), pt(x=1, y=4)], [pt(x=2, y=0), pt(x=2, y=1), pt(x=2, y=2), pt(x=2, y=3), pt(x=2, y=4)], [pt(x=3, y=0), pt(x=3, y=1), pt(x=3, y=2), pt(x=3, y=3), pt(x=3, y=4)], [pt(x=4, y=0), pt(x=4, y=1), pt(x=4, y=2), pt(x=4, y=3), pt(x=4, y=4)]]
    out1 = grid_trim(grid_map(abs, grid()), xmax=5, ymax=5)
    out1_ = (list)(map(list, parallel_grid_map(abs, grid_trim(grid(), xmax=5, ymax=5))))
    assert out1[0] == [0.0, 1.0, 2.0, 3.0, 4.0] == out1_[0]
    assert out1[1][0] == 1.0 == out1_[1][0]
    assert out1[2][0] == 2.0 == out1_[2][0]
    assert out1[3][0] == 3.0 == out1_[3][0]
    assert out1[3][4] == 5.0 == out1_[3][4]
    assert out1[4][0] == 4.0 == out1_[4][0]
    assert out1[4][3] == 5.0 == out1_[4][3]
    x = 5
    x = (square)(x)
    y = square
    y = y((5))
    assert x == 25 == y
    x = (5, 3)
    x = (mod)(*x)
    y = mod
    y = y(*((5, 3)))
    assert x == 2 == y
    x = square
    x = (lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs)))(x, (_coconut.functools.partial(_coconut.operator.add, (1))))
    x = x((4))
    assert x == 25
    v = vector(1, 2)
    try:
        v.x = 3
    except AttributeError as err:
        assert err
    else:
        assert False
    try:
        v.new_attr = True
    except AttributeError as err:
        assert err
    else:
        assert False
    assert SHOPeriodTerminate([-1, 0], 0, {"epsilon": 1})
    assert add_int_or_str_1(2) == 3 == coercive_add(2, "1")
    assert add_int_or_str_1("2") == "21" == coercive_add("2", 1)
    assert still_ident(3) == 3
    assert not_ident(3) == "bar"
    assert pattern_abs(4) == 4 == pattern_abs_(4)
    assert pattern_abs(0) == 0 == pattern_abs_(0)
    assert pattern_abs(-4) == 4 == pattern_abs_(-4)
    assert _coconut.operator.eq(vector(1, 2), vector(1, 2))
    assert (_coconut.operator.methodcaller("__eq__", other=vector(1, 2)))(vector(1, 2))
    assert (sum)(filter(lambda i: i % 2 == 0, takewhile(lambda i: i < 4000000, fib()))) == 4613732
    assert (list)(_coconut_igetitem(loop([1, 2]), _coconut.slice(None, 4))) == [1, 2] * 2
    assert recurse_n_times(10000)
    assert is_even(5000) and is_odd(5001)
    assert is_even_(5000) and is_odd_(5001)
    def _coconut_lambda_0(_=None):
        return mod
    assert (_coconut_lambda_0)()(5, 3) == 2
    assert (list)(sieve((2, 3, 4, 5))) == [2, 3, 5]
    assert 11 == double_plus_one(5)
    assert 15 == assign_func_1(_coconut.operator.mul, 3, 5)
    assert 15 == assign_func_2(_coconut.operator.mul, 3, 5)
    assert 20 == _coconut_compose(_coconut.functools.partial(minus, (2)), _coconut.functools.partial(mul, (2)), _coconut.functools.partial(plus, (1)))(10)
    assert 20 == (_coconut_compose(_coconut.functools.partial(minus, (2)), _coconut.functools.partial(mul, (2)), _coconut.functools.partial(plus, (1))))(10)
    assert does_raise_exc(raise_exc)
    assert ret_none(10) is None
    return True
