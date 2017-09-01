#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4ea1bdd3

# Compiled with Coconut version 1.2.3-post_dev41 [Colonel]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

from .util import *

def suite_test():
    """Executes the main test suite."""
    assert (plus)(1, 1) == 2 == (_coconut.operator.add)(1, 1)
    assert (plus)("1", "1") == "11" == (_coconut.operator.add)("1", "1")
    assert (mod)(3, 6) == 3 == (_coconut.operator.mod)(3, 6)
    assert (mod)(5, 4) == 1 == (mod_)(5, 4)
    assert (plus)((mod)(5, 2), 2) == 3 == (_coconut.operator.add)((_coconut.operator.mod)(5, 2), 2)
    assert (base)("11", 2) == 3
    assert (int)("10A", 12) == 154
    assert (join_with)(["1", "2"], ", ") == "1, 2"
    assert (join_with)(["a", "b", "c"]) == "abc"
    assert (len)(_coconut.set(("a", 5))) == 2
    assert _coconut.operator.mul(2, swap2(_coconut_minus)(2, 5)) == 6 == _coconut.operator.mul(2, swap2_(_coconut_minus)(2, 5))
    assert all(same((1, 2, 3), [1, 2, 3]))
    assert (list)(chain2((f() for f in (lambda: 1, lambda: 2)), (f() for f in (lambda: 3, lambda: 4)))) == [1, 2, 3, 4]
    assert _coconut.functools.partial(threeple, 1, 2)(3) == (1, 2, 3)
    assert (product)((range)(1, 5)) == 24
    assert plus1(4) == 5 == plus1_(4)
    assert (plus1)(2) == 3 == plus1(2)
    assert plus1(plus1(5)) == 7 == _coconut_forward_compose(plus1, plus1)(5)
    assert (sqrt)(16) == 4 == (sqrt_)(16)
    assert (square)(3) == 9
    def test_sqplus1_plus1sq(sqplus1, plus1sq, parallel=True):
        assert sqplus1(3) == 10 == _coconut_forward_compose(square, plus1)(3), sqplus1
        if parallel:
            assert (tuple)(parallel_map(sqplus1, range(3))) == (1, 2, 5), sqplus1
        assert (plus1sq)(3) == 16, plus1sq
        assert (sqplus1)(3) == 10, sqplus1
    test_sqplus1_plus1sq(sqplus1_1, plus1sq_1)
    test_sqplus1_plus1sq(sqplus1_2, plus1sq_2, parallel=False)
    test_sqplus1_plus1sq(sqplus1_3, plus1sq_3)
    test_sqplus1_plus1sq(sqplus1_4, plus1sq_4)
    assert (square)((plus1)(3)) == 16 == (square)((plus1_)(3))
    assert reduce(_coconut_pipe, [3, plus1, square]) == 16 == pipe(pipe(3, plus1), square)
    assert reduce(_coconut_back_compose, [sqrt, square, plus1])(3) == 4 == compose(compose(sqrt, square), plus1)(3)
    assert sum_([1, 7, 3, 5]) == 16
    assert (list)(add([1, 2, 3], [10, 20, 30])) == [11, 22, 33]
    assert (list)(add_([1, 2, 3], [10, 20, 30])) == [11, 22, 33]
    assert (list)(zipsum([1, 2, 3], [10, 20, 30])) == [11, 22, 33]
    assert clean("   ab cd ef   ") == "ab cd ef" == (clean)("   ab cd ef   ")
    assert ((add2)(2))(3) == 5
    for qsort in [qsort1, qsort2, qsort3, qsort4, qsort5, qsort6]:
        to_sort = rand_list(10)
        assert (tuple)((qsort)(to_sort)) == (tuple)((sorted)(to_sort)), qsort
    assert _coconut_igetitem(repeat(3), 2) == 3 == _coconut_igetitem(repeat_(3), 2)
    assert sum_(_coconut_igetitem(repeat(1), _coconut.slice(None, 5))) == 5 == sum_(_coconut_igetitem(repeat_(1), _coconut.slice(None, 5)))
    assert (sum_(takewhile(lambda x: x < 5, N())) == 10 == (sum)(_coconut_igetitem(dropwhile(_coconut.functools.partial(_coconut.operator.gt, 0), (_coconut.itertools.chain.from_iterable((f() for f in (lambda: range(-10, 0), lambda: N()))))), _coconut.slice(None, 5))))
    assert (sum_)(((lambda s: map(_coconut.functools.partial(_coconut.operator.getitem, s), (1, 3, 5))))("ABCDEFG")) == "BDF"
    assert (list)(_coconut_igetitem(N(), _coconut.slice(10, 15))) == [10, 11, 12, 13, 14] == (list)(_coconut_igetitem(N_(), _coconut.slice(10, 15)))
    assert ((list)(takewhile(_coconut.functools.partial(_coconut.operator.gt, 5), N())) == [0, 1, 2, 3, 4] == (list)(_coconut_igetitem(range(0, 10), _coconut.slice(None, 5, None))))
    assert (sum)(_coconut_igetitem((_coconut.itertools.chain.from_iterable((f() for f in (lambda: range(-10, 0), lambda: N())))), _coconut.slice(5, 15))) == -5 == (sum)(_coconut_igetitem(chain(range(-10, 0), N()), _coconut.slice(5, 15)))
    assert (list)(_coconut_igetitem(add(repeat(1), N()), _coconut.slice(None, 5))) == [1, 2, 3, 4, 5] == (list)(_coconut_igetitem(add_(repeat(1), N_()), _coconut.slice(None, 5)))
    assert sum(_coconut_igetitem(_coconut_igetitem(N(), _coconut.slice(5, None)), _coconut.slice(None, 5))) == 35 == sum(_coconut_igetitem(_coconut_igetitem(N_(), _coconut.slice(5, None)), _coconut.slice(None, 5)))
    assert (list)(_coconut.functools.partial(_coconut_igetitem, N())(slice(5, 10))) == [5, 6, 7, 8, 9] == _coconut.functools.partial(_coconut.operator.getitem, list(range(0, 15)))(slice(5, 10))
    assert (list)(_coconut_igetitem(N(), slice(5, 10))) == [5, 6, 7, 8, 9] == list(range(0, 15))[slice(5, 10)]
    assert (list)(_coconut_igetitem(preN(range(-5, 0)), _coconut.slice(1, 10))) == [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    assert (list)(_coconut_igetitem(map_iter(_coconut.functools.partial(_coconut.operator.mul, 2), N()), _coconut.slice(None, 5))) == [0, 2, 4, 6, 8]
    assert (tuple)(_coconut_igetitem(N(), _coconut.slice(None, 100))) == (tuple)(_coconut_igetitem(N_(), _coconut.slice(None, 100))) == (tuple)(_coconut_igetitem(N__(), _coconut.slice(None, 100)))
    assert next_mul_of(5, 12) == 15
    assert collatz(27)
    assert preop(1, 2).add() == 3
    assert (abs)(vector(3, 4)) == 5 == (abs)(vector_with_id(3, 4, 1))
    assert (tuple)(((lambda v: map(_coconut.functools.partial(_coconut.getattr, v), ("x", "y"))))(vector(1, 2))) == (1, 2)
    assert (tuple)(((lambda v: map(_coconut.functools.partial(_coconut.operator.getitem, v), (0, 1))))((vector(1, 2).transform)(vector(3, 1)))) == (4, 3)
    assert (vector(1, 2).__eq__)(vector(1, 2))
    assert not (vector(3, 4).__eq__)(vector(1, 2))
    assert not (vector(1, 2).__eq__)((1, 2))
    assert vector(vector(4, 3)) == vector(4, 3)
    assert not vector(4, 3) != vector(4, 3)
    assert not vector(1, 2) == (1, 2)
    assert not vector(2, 3) != vector(2, 3)
    assert vector(1, 2) != (1, 2)
    assert triangle(3, 4, 5).is_right()
    assert _coconut.getattr(triangle(3, 4, 5), "is_right")
    assert (_coconut.operator.methodcaller("is_right"))(triangle(3, 4, 5))
    assert (triangle(3, 4, 5)).is_right()
    def test_factorial(factorial, test_none=True):
        assert factorial(0) == 1 == factorial(1)
        assert factorial(3) == 6
        if test_none:
            assert factorial(-1) is None
    test_factorial(factorial1)
    test_factorial(factorial2)
    test_factorial(factorial4)
    test_factorial(factorial5)
    test_factorial(fact, test_none=False)
    test_factorial(fact_, test_none=False)
    test_factorial(factorial, test_none=False)
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
    assert map_(_coconut.functools.partial(_coconut.operator.add, 1), []) == []
    assert map_(_coconut.functools.partial(_coconut.operator.add, 1), ()) == ()
    assert map_(_coconut.functools.partial(_coconut.operator.add, 1), [0, 1, 2, 3]) == [1, 2, 3, 4]
    assert map_(_coconut.functools.partial(_coconut.operator.add, 1), (0, 1, 2, 3)) == (1, 2, 3, 4)
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
    assert not Nothing() == ()
    assert not Nothing() != Nothing()
    assert Nothing() != ()
    assert not Just(1) == (1,)
    assert not Just(1) != Just(1)
    assert Just(1) != (1,)
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
    x = _coconut_forward_compose((_coconut.functools.partial(_coconut.operator.add, 1)), x)
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
    assert (vector(1, 2)).__eq__(other=vector(1, 2))
    assert (tuple)(_coconut_igetitem(fib(), _coconut.slice(1, 4))) == (1, 2, 3)
    assert (sum)(filter(lambda i: i % 2 == 0, takewhile(lambda i: i < 4000000, fib()))) == 4613732
    assert (list)(_coconut_igetitem(loop([1, 2]), _coconut.slice(None, 4))) == [1, 2] * 2
    def _coconut_lambda_0(_=None):
        return mod
    assert (_coconut_lambda_0)()(5, 3) == 2
    assert (list)(sieve((2, 3, 4, 5))) == [2, 3, 5]
    assert 11 == double_plus_one(5)
    assert 15 == assign_func_1(_coconut.operator.mul, 3, 5)
    assert 15 == assign_func_2(_coconut.operator.mul, 3, 5)
    assert 20 == _coconut_back_compose(_coconut.functools.partial(minus, 2), _coconut.functools.partial(mul, 2), _coconut.functools.partial(plus, 1))(10)
    assert 20 == _coconut_forward_compose(_coconut.functools.partial(plus, 1), _coconut.functools.partial(mul, 2), _coconut.functools.partial(minus, 2))(10)
    assert does_raise_exc(raise_exc)
    assert ret_none(10) is None
    assert (_coconut_partial(ret_args_kwargs, {0: 1, 3: 4}, 5, *(6, 7), a="k"))(*(2, 3, 5)) == ((1, 2, 3, 4, 5, 6, 7), {"a": "k"})
    assert anything_func() is None
    assert args_kwargs_func() is None
    assert x_is_int(4) == 4 == x_is_int(x=4)
    try:
        x_is_int(x="herp")
    except MatchError:
        pass
    else:
        assert False
    try:
        x_is_int()
    except MatchError:
        pass
    else:
        assert False
    assert x_as_y(x=2) == (2, 2) == x_as_y(y=2)
    assert x_y_are_int_gt_0(1, 2) == (1, 2) == x_y_are_int_gt_0(x=1, y=2)
    try:
        x_y_are_int_gt_0(1, y=0)
    except MatchError:
        pass
    else:
        assert False
    assert x_is_int_def_0() == 0 == x_is_int_def_0(x=0)
    try:
        x_is_int_def_0("derp")
    except MatchError:
        pass
    else:
        assert False
    assert head_tail_def_none() == (None, []) == head_tail_def_none([None])
    assert kwd_only_x_is_int_def_0() == 0 == kwd_only_x_is_int_def_0(x=0)
    try:
        kwd_only_x_is_int_def_0(1)
    except MatchError:
        pass
    else:
        assert False
    assert no_args_kwargs()
    try:
        no_args_kwargs(1)
    except MatchError:
        pass
    else:
        assert False
    try:
        no_args_kwargs(a=1)
    except MatchError:
        pass
    else:
        assert False
    a = altclass()
    assert a.func(1) == 1
    assert a.zero(10) == 0
    with Vars.using(globals()):
        assert var_one == 1
    try:
        var_one
    except NameError:
        assert True
    else:
        assert False
    assert (Just)(*map(lambda _=None: _ * 2, Just(3))) == Just(6) == fmap(lambda _=None: _ * 2, Just(3))
    assert (Nothing)(*map(lambda _=None: _ * 2, Nothing())) == Nothing() == fmap(lambda _=None: _ * 2, Nothing())
    assert Elems(1, 2, 3) != Elems(1, 2)
    assert (repr)(fmap(times2, map(plus1, (1, 2, 3)))) == (repr)(map(_coconut_forward_compose(plus1, times2), (1, 2, 3)))
    assert (repr)(fmap(plus1, reversed((1, 2, 3)))) == (repr)((reversed)(map(plus1, (1, 2, 3))))
    assert identity[1:2, 2:3] == (slice(1, 2), slice(2, 3))
    assert (identity)[_coconut.slice(1, 2), _coconut.slice(2, 3)] == (slice(1, 2), slice(2, 3))
    assert (_coconut.operator.itemgetter(_coconut.slice(1, 2), _coconut.slice(2, 3)))(identity) == (slice(1, 2), slice(2, 3))
    assert identity.method(*(1,), **{"a": 2}) == ((1,), {"a": 2})
    assert (_coconut.operator.methodcaller("method", *(1,), **{"a": 2}))(identity) == ((1,), {"a": 2})
    assert (identity).method(*(1,), **{"a": 2}) == ((1,), {"a": 2})
    assert container(1) == container(1)
    assert not container(1) != container(1)
    assert container(1) != container(2)
    assert not container(1) == container(2)
    assert container_(1) == container_(1)
    assert not container_(1) != container_(1)
    assert container_(1) != container_(2)
    assert not container_(1) == container_(2)
    t = Tuple(1, 2)
    assert repr(t) == "Tuple(*elems=(1, 2))"
    assert t.elems == (1, 2)
    assert isinstance(t.elems, tuple)
    assert fmap(lambda _=None: _ + 1, t) == Tuple(2, 3)
    _coconut_match_check = False
    _coconut_match_to = t
    if (_coconut.isinstance(_coconut_match_to, Tuple)) and (_coconut.len(_coconut_match_to) == 2):
        x = _coconut_match_to[0]
        y = _coconut_match_to[1]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'Tuple(x, y) = t'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'Tuple(x, y) = t'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert x == 1 and y == 2
    p = Pred("name", 1, 2)
    p_ = Pred_("name", 1, 2)
    assert p.name == "name" == p_.name
    assert p.args == (1, 2) == p_.args
    assert repr(p) in ("Pred(name='name', *args=(1, 2))", "Pred(name=u'name', *args=(1, 2))")
    assert repr(p_) in ("Pred_(name='name', *args=(1, 2))", "Pred_(name=u'name', *args=(1, 2))")
    for Pred_test, p_test in [(Pred, p), (Pred_, p_)]:
        assert isinstance(p_test.args, tuple)
        _coconut_match_check = False
        _coconut_match_to = p_test
        if (_coconut.isinstance(_coconut_match_to, Pred_test)) and (_coconut.len(_coconut_match_to) >= 1):
            name = _coconut_match_to[0]
            args = _coconut_match_to[1:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'Pred_test(name, *args) = p_test'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'Pred_test(name, *args) = p_test'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert name == "name"
        assert args == (1, 2)
    q = Quant("name", "var", 1, 2)
    q_ = Quant_("name", "var", 1, 2)
    assert q.name == "name" == q_.name
    assert q.var == "var" == q_.var
    assert q.args == (1, 2) == q_.args
    assert repr(q) in ("Quant(name='name', var='var', *args=(1, 2))", "Quant(name=u'name', var=u'var', *args=(1, 2))")
    assert repr(q_) in ("Quant_(name='name', var='var', *args=(1, 2))", "Quant_(name=u'name', var=u'var', *args=(1, 2))")
    for Quant_test, q_test in [(Quant, q), (Quant_, q_)]:
        assert isinstance(q_test.args, tuple)
        _coconut_match_check = False
        _coconut_match_to = q_test
        if (_coconut.isinstance(_coconut_match_to, Quant_test)) and (_coconut.len(_coconut_match_to) >= 2):
            name = _coconut_match_to[0]
            var = _coconut_match_to[1]
            args = _coconut_match_to[2:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'Quant_test(name, var, *args) = q_test'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'Quant_test(name, var, *args) = q_test'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert name == "name"
        assert var == "var"
        assert args == (1, 2)
    assert fmap(lambda _=None: _ + 1, Pred(0, 1, 2)) == Pred(1, 2, 3)
    assert fmap(lambda _=None: _ + 1, Pred_(0, 1, 2)) == Pred_(1, 2, 3)
    assert fmap(lambda _=None: _ + 1, Quant(0, 1, 2)) == Quant(1, 2, 3)
    assert fmap(lambda _=None: _ + 1, Quant_(0, 1, 2)) == Quant_(1, 2, 3)
    a = Nest()
    assert a.b.c.d == "data"
    assert (_coconut.operator.attrgetter("b.c.d"))(a) == "data"
    assert (a).b.c.d == "data"
    assert a.b.c.m() == "method"
    assert (_coconut_base_compose(_coconut.operator.attrgetter("b.c"), (_coconut.operator.methodcaller("m"), False)))(a) == "method"
    assert ((a).b.c).m() == "method"
    assert (lambda x: None if x is None else (lambda x: None if x is None else (lambda x: None if x is None else (lambda x: None if x is None else x())(x.m))(x.c))(x.b))(a) == "method"
    assert (lambda x: None if x is None else x.derp.herp)(a.b.c.none) is None
    assert (list)(tco_chain([1, 2, 3])) == ["last"]
    assert (list)(map(tuple, partition([1, 2, 3], 2))) == [(1,), (3, 2)] == (list)(map(tuple, partition_([1, 2, 3], 2)))
    assert myreduce(_coconut.operator.add, (1, 2, 3)) == 6
    assert recurse_n_times(10000)
    assert fake_recurse_n_times(10000)
    a = A()
    assert _coconut_forward_compose(a.true, _coconut.operator.not_)() is False
    assert 10 % 4 % 3 == 2 == (mod)((mod)(10, 4), 3)
    assert square_times2_plus1(3) == 19 == square_times2_plus1_(3)
    assert plus1_cube(2) == 27
    assert (repr)(_coconut_base_compose(square, (times2, False), (plus1, False))) == (repr)(_coconut_base_compose(square, ((_coconut_base_compose(times2, (plus1, False))), False)))
    assert (tuple)(starmap(toprint, map(range, range(1, 5)))) == ('0', '0 1', '0 1 2', '0 1 2 3')
    assert (tuple)(fmap(_coconut.operator.methodcaller("strip", " 0"), starmap(toprint, map(range, range(1, 5))))) == ("", "1", "1 2", "1 2 3")
    assert (len)(starmap(toprint, ())) == 0
    assert (starmap(toprint, [(1, 2)]))[0] == "1 2"
    assert (list)((starmap(toprint, [(1, 2), (2, 3), (3, 4)]))[_coconut.slice(1, None)]) == ["2 3", "3 4"]
    assert none_to_ten() == 10 == any_to_ten(1, 2, 3)
    assert int_map(plus1_, range(5)) == [1, 2, 3, 4, 5]
    assert still_ident.__doc__ == "docstring"
    with context_produces(1) as one:
        with context_produces(2) as two:
            assert one == 1
            assert two == 2
    assert raise_exc() if 1 is None else 1 == 1
    try:
        assert raise_exc() if None is None else None
    except Exception as err:
        assert str(err) == "raise_exc"
    else:
        assert False
    for u, Point_test in [("", Point), ("_", Point_)]:
        p = Point_test()
        assert p.x == 0 == p.y
        assert repr(p) == "Point{u}(x=0, y=0)".format(u=u)
        p = Point_test(1)
        assert p.x == 1
        assert p.y == 0
        assert repr(p) == "Point{u}(x=1, y=0)".format(u=u)
        p = Point_test(2, 3)
        assert p.x == 2
        assert p.y == 3
        assert repr(p) == "Point{u}(x=2, y=3)".format(u=u)
    try:
        RadialVector()
    except TypeError:
        try:
            RadialVector_()
        except TypeError:
            pass
        else:
            assert False
    else:
        assert False
    rv = RadialVector(1)
    rv_ = RadialVector_(1)
    assert rv.mag == 1 == rv_.mag
    assert rv.angle == 0 == rv_.angle
    assert repr(rv) == "RadialVector(mag=1, angle=0)"
    assert repr(rv_) == "RadialVector_(mag=1, angle=0)"
    for u, ABC_test in [("", ABC), ("_", ABC_)]:
        try:
            ABC_test()
        except TypeError:
            pass
        else:
            assert False
        abc = ABC_test(2)
        assert abc.a == 2
        assert abc.b == 1
        assert abc.c == ()
        assert repr(abc) == "ABC{u}(a=2, b=1, *c=())".format(u=u)
        abc = ABC_test(3, 4, 5)
        assert abc.a == 3
        assert abc.b == 4
        assert abc.c == (5,)
        assert repr(abc) == "ABC{u}(a=3, b=4, *c=(5,))".format(u=u)
        abc = ABC_test(5, 6, 7, 8)
        assert abc.a == 5
        assert abc.b == 6
        assert abc.c == (7, 8)
        assert repr(abc) == "ABC{u}(a=5, b=6, *c=(7, 8))".format(u=u)
    v = vector2(3, 4)
    assert repr(v) == "vector2(x=3, y=4)"
    assert abs(v) == 5
    try:
        v.x = 2
    except AttributeError:
        pass
    else:
        assert False
    v = vector2()
    assert repr(v) == "vector2(x=0, y=0)"
    assert factorial.__doc__ == "this is a docstring" == iadd.__doc__
    assert list_type((f() for f in (lambda: 1, lambda: 2))) == "at least 2"
    assert list_type((f() for f in (lambda: 1,))) == "at least 1"
    assert list_type(_coconut.iter(())) == "empty"
    cnt = counter()
    _coconut_match_to = cnt.inc()
    _coconut_match_check = False
    if _coconut_match_to == 1:
        _coconut_match_check = True
    if _coconut_match_check:
        assert False
    if not _coconut_match_check:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            assert False
    if not _coconut_match_check:
        if _coconut_match_to is None:
            _coconut_match_check = True
        if _coconut_match_check:
            pass
    if not _coconut_match_check:
        assert False
    assert cnt.count == 1
    assert (list)(plus1sq_all(1, 2, 3)) == [4, 9, 16] == (list)(plus1sq_all_(1, 2, 3))
    assert (list)(sqplus1_all(1, 2, 3)) == [2, 5, 10] == (list)(sqplus1_all_(1, 2, 3))
    assert (list)(square_times2_plus1_all(1, 2)) == [3, 9] == (list)(square_times2_plus1_all_(1, 2))
    assert (list)(plus1_square_times2_all(1, 2)) == [8, 18] == (list)(plus1_square_times2_all_(1, 2))
    assert plus1sqsum_all(1, 2) == 13 == plus1sqsum_all_(1, 2)
    return True

def tco_test():
    """Executes suite tests that rely on TCO."""
    assert is_even(5000) and is_odd(5001)
    assert is_even_(5000) and is_odd_(5001)
    return True
