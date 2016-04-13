#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x35c6c1aa

# Compiled with Coconut version 0.4.1-post_dev [Pinnate]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
import __coconut__
_coconut_sys.path.remove(_coconut_file_path)
for name in dir(__coconut__):
    if not name.startswith("__"):
        globals()[name] = getattr(__coconut__, name)

# Compiled Coconut: ------------------------------------------------------------

import sys
from .util import *

def main_test():
    """Executes the main test suite."""
    assert "\n" == ('''
''') == """
"""
    assert _coconut
    assert "_coconut" in globals()
    assert "_coconut" not in locals()
    x = 5
    assert x == 5
    x == 6
    assert x == 5
    assert r"hello, world" == "hello, world" == "hello," " " "world"
    assert "\n " == """
 """
    assert "\\" "\"" == "\\\""
    assert """

""" == "\n\n"
    assert {"a": 5}["a"] == 5
    a, = [24]
    assert a == 24
    assert set((1, 2, 3)) == _coconut.set((1, 2, 3))
    olist = [0, 1, 2]
    olist[1] += 4
    assert olist == [0, 5, 2]
    assert +5e+5 == +5 * +10**+5
    assert (plus)(1, 1) == 2 == (_coconut.operator.__add__)(1, 1)
    assert (plus)("1", "1") == "11" == (_coconut.operator.__add__)("1", "1")
    assert (mod)(3, 6) == 3 == (_coconut.operator.__mod__)(3, 6)
    assert (mod)(5, 4) == 1 == (mod_)(5, 4)
    assert (mod)(5, (plus)(2, 2)) == 1 == (_coconut.operator.__mod__)(5, (_coconut.operator.__add__)(2, 2))
    assert (base)("11", 2) == 3
    assert (int)("10A", 12) == 154
    assert (join_with)(["1", "2"], ", ") == "1, 2"
    assert (join_with)(["a", "b", "c"]) == "abc"
    assert (len)(_coconut.set(("a", 5))) == 2
    assert repr(3) == "3" == ascii(3)
    assert (_coconut.functools.partial(_coconut.operator.__mul__, 2))((_coconut.functools.partial(_coconut_minus, 2))(5)) == -6
    assert (_coconut.functools.partial(_coconut.operator.__mul__, 2))((_coconut.functools.partial(swap2(_coconut_minus), 2))(5)) == 6 == (_coconut.functools.partial(_coconut.operator.__mul__, 2))((_coconut.functools.partial(swap2_(_coconut_minus), 2))(5))
    assert all(same((1, 2, 3), [1, 2, 3]))
    assert (list)(chain2((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 3, lambda: 4)))) == [1, 2, 3, 4]
    assert (prod)((range)(1, 5)) == 24
    assert plus1(4) == 5 == plus1_(4)
    assert (plus1)(2) == 3 == plus1(2)
    assert plus1(plus1(5)) == 7 == _coconut_compose(plus1, plus1)(5)
    assert (sqrt)(16) == 4 == (sqrt_)(16)
    assert (square)(3) == 9
    assert sqplus1(3) == 10 == _coconut_compose(plus1, square)(3)
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
    assert (sum_(takewhile(lambda x: x < 5, N())) == 10 == (sum)(_coconut_igetitem(dropwhile(_coconut.functools.partial(_coconut.operator.__gt__, 0), (_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: range(-10, 0), lambda: N()))))), _coconut.slice(None, 5))))
    assert (sum_)(((lambda s: map(_coconut.functools.partial(_coconut.operator.__getitem__, s), (1, 3, 5))))("ABCDEFG")) == "BDF"
    assert (list)(map(_coconut.functools.partial(pow, 2), (range)(0, 5))) == [1, 2, 4, 8, 16]
    assert (list)(_coconut_igetitem(N(), _coconut.slice(10, 15))) == [10, 11, 12, 13, 14] == (list)(_coconut_igetitem(N_(), _coconut.slice(10, 15)))
    assert ((list)((_coconut.functools.partial(takewhile, _coconut.functools.partial(_coconut.operator.__gt__, 5)))(N())) == [0, 1, 2, 3, 4] == (list)(_coconut_igetitem(range(0, 10), _coconut.slice(None, 5, None))))
    assert (sum)(_coconut_igetitem((_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: range(-10, 0), lambda: N())))), _coconut.slice(5, 15))) == -5 == (sum)(_coconut_igetitem(chain(range(-10, 0), N()), _coconut.slice(5, 15)))
    assert (list)(_coconut_igetitem(add(repeat(1), N()), _coconut.slice(None, 5))) == [1, 2, 3, 4, 5] == (list)(_coconut_igetitem(add(repeat(1), N_()), _coconut.slice(None, 5)))
    assert sum(_coconut_igetitem(_coconut_igetitem(N(), _coconut.slice(5, None)), _coconut.slice(None, 5))) == 35 == sum(_coconut_igetitem(_coconut_igetitem(N_(), _coconut.slice(5, None)), _coconut.slice(None, 5)))
    assert (list)(_coconut.functools.partial(_coconut_igetitem, N())(slice(5, 10))) == [5, 6, 7, 8, 9] == _coconut.functools.partial(_coconut.operator.__getitem__, list(range(0, 15)))(slice(5, 10))
    assert (list)(_coconut_igetitem(N(), slice(5, 10))) == [5, 6, 7, 8, 9] == list(range(0, 15))[slice(5, 10)]
    assert (list)(_coconut_igetitem(preN(range(-5, 0)), _coconut.slice(1, 10))) == [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    assert (list)(_coconut_igetitem(map_iter(_coconut.functools.partial(_coconut.operator.__mul__, 2), N()), _coconut.slice(None, 5))) == [0, 2, 4, 6, 8]
    assert (tuple)(_coconut_igetitem(N(), _coconut.slice(None, 100))) == (tuple)(_coconut_igetitem(N_(), _coconut.slice(None, 100))) == (tuple)(_coconut_igetitem(N__(), _coconut.slice(None, 100)))
    assert (_coconut.functools.partial(next_mul_of, 5))(12) == 15
    assert collatz(27) and collatz_(27)
    assert preop(1, 2).add() == 3
    assert (abs)(vector(3, 4)) == 5
    assert (tuple)(((lambda v: map(_coconut.functools.partial(_coconut.getattr, v), ("x", "y"))))(vector(1, 2))) == (1, 2)
    assert (tuple)(((lambda v: map(_coconut.functools.partial(_coconut.operator.__getitem__, v), (0, 1))))((vector(1, 2).transform)(vector(3, 1)))) == (4, 3)
    assert (vector(1, 2).__eq__)(vector(1, 2))
    assert not (vector(3, 4).__eq__)(vector(1, 2))
    assert not (vector(1, 2).__eq__)((1, 2))
    assert vector(vector(4, 3)) == vector(4, 3)
    assert triangle(3, 4, 5).is_right()
    assert _coconut.getattr(triangle(3, 4, 5), "is_right")
    assert factorial1(3) == 6
    assert factorial2(3) == 6
    assert factorial4(3) == 6
    assert factorial5(3) == 6
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
    assert map_(_coconut.functools.partial(_coconut.operator.__add__, 1), []) == []
    assert map_(_coconut.functools.partial(_coconut.operator.__add__, 1), ()) == ()
    assert map_(_coconut.functools.partial(_coconut.operator.__add__, 1), [0, 1, 2, 3]) == [1, 2, 3, 4]
    assert map_(_coconut.functools.partial(_coconut.operator.__add__, 1), (0, 1, 2, 3)) == (1, 2, 3, 4)
    assert duplicate_first1([1, 2, 3]) == [1, 1, 2, 3]
    assert (list)(duplicate_first2([1, 2, 3])) == [1, 1, 2, 3] == (list)(duplicate_first3([1, 2, 3]))
    assert one_to_five([1, 2, 3, 4, 5]) == [2, 3, 4]
    assert not one_to_five([0, 1, 2, 3, 4, 5])
    assert one_to_five([1, 5]) == []
    assert -4 == neg_square_u(2) != 4 & 0 <= neg_square_u(0) <= 0
    iter1 = range(0, 10)
    iter1, iter2 = tee(iter1)
    assert (list)(_coconut_igetitem(iter1, _coconut.slice(2, 8))) == (list)(_coconut_igetitem(iter2, _coconut.slice(2, 8)))
    data = 5
    assert data == 5
    data = 3
    assert data == 3
    def backslash_test():
        return lambda x: x
    assert 1 == 1 == backslash_test()(1)
    assert (
            "hello"
         == "hello" == 
            'hello'
        )
    def multiline_backslash_test(
                                   x,
                                   y):
        return x + y
    assert multiline_backslash_test(1, 2) == 3
    assert True
    class one_line_class(_coconut.object): pass
    assert isinstance(one_line_class(), one_line_class)
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
    assert ((_coconut.operator.attrgetter("join"))(""))(["1", "2", "3"]) == "123" == ((_coconut.functools.partial(_coconut.getattr, ""))("join"))(["1", "2", "3"])
    assert ((_coconut.functools.partial(_coconut.functools.partial, mod))(5))(3) == 2 == ((_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.__mod__))(5))(3)
    assert (_coconut.functools.partial(_coconut.operator.__getitem__, [1, 2, 3]))(1) == 2 == (_coconut.functools.partial(_coconut_igetitem, [1, 2, 3]))(1)
    assert (_coconut.functools.partial(_coconut.operator.__getitem__, "123"))(1) == "2" == (_coconut.functools.partial(_coconut_igetitem, "123"))(1)
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
    assert (list)(_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: -1, lambda: 0)), lambda: range(1, 5))))) == [-1, 0, 1, 2, 3, 4]
    assert (list)(_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1,)), lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 2,)))))) == [1, 2]
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
    assert not isinstance(map(_coconut.functools.partial(_coconut.operator.__add__, 2), [1, 2, 3]), list)
    assert not isinstance(range(10), list)
    assert isinstance(10**100, int)
    assert chr(1000)
    assert (abs)(3 + 4j) == 5
    assert 3.14j == 3.14j
    assert 10.j == 10.j
    assert 10j == 10j
    assert .001j == .001j
    assert 1e100j == 1e100j
    assert 3.14e-10j == 3.14e-10j
    _coconut_match_check = False
    _coconut_match_to = {"text": "abc", "tags": [1, 2, 3]}
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2) and ("text" in _coconut_match_to) and ("tags" in _coconut_match_to) and (_coconut.isinstance(_coconut_match_to["tags"], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to["tags"]) >= 1):
        text = _coconut_match_to["text"]
        rest = _coconut.list(_coconut_match_to["tags"][1:])
        first = _coconut_match_to["tags"][0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"text": text, "tags": [first] + rest} = {"text": "abc", "tags": [1, 2, 3]}\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = '{"text": text, "tags": [first] + rest} = {"text": "abc", "tags": [1, 2, 3]}'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    assert text == "abc"
    assert first == 1
    assert rest == [2, 3]
    assert trilen(3, 4).h == 5 == datamaker(trilen)(5).h
    assert bytes(3) == b"\x00\x00\x00"
    assert isinstance("a", str)
    assert isinstance(b"a", bytes)
    assert A().true()
    assert B().true()
    global glob_a, glob_b
    glob_a, glob_b = 0, 0
    assert glob_a == 0 == glob_b
    def set_globs(x):
        global glob_a, glob_b
        glob_a, glob_b = x, x
    set_globs(2)
    assert glob_a == 2 == glob_b
    assert _coconut_minus(1) == -1 == _coconut.functools.partial(_coconut_minus, 1)(2)
    assert pt.__doc__
    out0 = (_coconut.functools.partial(grid_trim, xmax=5, ymax=5))(grid())
    assert out0 == [[pt(x=0, y=0), pt(x=0, y=1), pt(x=0, y=2), pt(x=0, y=3), pt(x=0, y=4)], [pt(x=1, y=0), pt(x=1, y=1), pt(x=1, y=2), pt(x=1, y=3), pt(x=1, y=4)], [pt(x=2, y=0), pt(x=2, y=1), pt(x=2, y=2), pt(x=2, y=3), pt(x=2, y=4)], [pt(x=3, y=0), pt(x=3, y=1), pt(x=3, y=2), pt(x=3, y=3), pt(x=3, y=4)], [pt(x=4, y=0), pt(x=4, y=1), pt(x=4, y=2), pt(x=4, y=3), pt(x=4, y=4)]]
    out1 = (_coconut.functools.partial(grid_trim, xmax=5, ymax=5))((_coconut.functools.partial(grid_map, abs))(grid()))
    out1_ = (list)((_coconut.functools.partial(map, list))((_coconut.functools.partial(parallel_grid_map, abs))((_coconut.functools.partial(grid_trim, xmax=5, ymax=5))(grid()))))
    assert out1[0] == [0.0, 1.0, 2.0, 3.0, 4.0] == out1_[0]
    assert out1[1][0] == 1.0 == out1_[1][0]
    assert out1[2][0] == 2.0 == out1_[2][0]
    assert out1[3][0] == 3.0 == out1_[3][0]
    assert out1[3][4] == 5.0 == out1_[3][4]
    assert out1[4][0] == 4.0 == out1_[4][0]
    assert out1[4][3] == 5.0 == out1_[4][3]
    assert (_coconut.operator.__le__)(3, 3)
    assert (list)((consume)(range(10))) == []
    assert (list)((_coconut.functools.partial(consume, keep_last=2))(range(10))) == [8, 9]
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
    x = (lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs)))(x, (_coconut.functools.partial(_coconut.operator.__add__, 1)))
    x = x((4))
    assert x == 25
    i = int()
    try:
        i.x = 12
    except AttributeError as err:
        assert err
    else:
        assert False
    b = bytes()
    try:
        b.x = 12
    except AttributeError as err:
        assert err
    else:
        assert False
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
    if _coconut_sys.version_info < (3,):
        import Queue as q
    else:
        import queue as q
    if _coconut_sys.version_info < (3,):
        import __builtin__ as builtins
    else:
        import builtins
    if _coconut_sys.version_info < (3,):
        import email.MIMEBase as _coconut_import
        try:
            email
        except:
            email = _coconut.imp.new_module("email")
        else:
            if not _coconut.isinstance(email, _coconut.types.ModuleType):
                email = _coconut.imp.new_module("email")
        try:
            email.mime
        except:
            email.mime = _coconut.imp.new_module("email.mime")
        else:
            if not _coconut.isinstance(email.mime, _coconut.types.ModuleType):
                email.mime = _coconut.imp.new_module("email.mime")
        email.mime.base = _coconut_import
    else:
        import email.mime.base
    assert q.Queue
    assert builtins.len([1, 1]) == 2
    assert email.mime.base
    if _coconut_sys.version_info < (3,):
        import email.MIMEBase as mimebase
    else:
        from email.mime import base as mimebase
    assert mimebase
    from_err = TypeError()
    try:
        _coconut_raise_from = ValueError()
        _coconut_raise_from.__cause__ = from_err
        raise _coconut_raise_from
    except ValueError as err:
        assert err.__cause__ is from_err
    else:
        assert False
    class doc(_coconut.collections.namedtuple("doc", "")):
        "doc"
        __slots__ = ()
    class doc_(_coconut.collections.namedtuple("doc_", "")):
        """doc"""
        __slots__ = ()
    assert doc.__doc__ == "doc" == doc_.__doc__
    assert 10000000.0 == 10000000.0
    assert (tuple)(_coconut.iter(())) == ()
    import collections
    if _coconut_sys.version_info < (3, 3):
        import collections as _coconut_import
        try:
            collections
        except:
            collections = _coconut.imp.new_module("collections")
        else:
            if not _coconut.isinstance(collections, _coconut.types.ModuleType):
                collections = _coconut.imp.new_module("collections")
        collections.abc = _coconut_import
    else:
        import collections.abc
    assert isinstance([], collections.abc.Sequence)
    assert isinstance(range(1), collections.abc.Sequence)
    assert collections.defaultdict(int)[5] == 0
    assert len(range(10)) == 10
    assert (tuple)((reversed)(range(4))) == (3, 2, 1, 0)
    assert (tuple)(range(5)[1:]) == (1, 2, 3, 4) == (tuple)(_coconut_igetitem(range(5), _coconut.slice(1, None)))
    assert (tuple)(range(10)[-3:-1]) == (7, 8) == (tuple)(_coconut_igetitem(range(10), _coconut.slice(-3, -1)))
    assert (tuple)(_coconut_igetitem(map(abs, (1, -2, -5, 2)), _coconut.slice(None, None))) == (1, 2, 5, 2)
    assert _coconut_igetitem((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)), -1) == 2
    assert (tuple)(_coconut_igetitem((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), _coconut.slice(-2, None))) == (2, 3)
    assert (tuple)(_coconut_igetitem((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), _coconut.slice(None, -2))) == (0, 1)
    assert _coconut_igetitem(map(_coconut.operator.__add__, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2))), -1) == 22 == map(_coconut.operator.__add__, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)))[-1]
    assert _coconut_igetitem(map(lambda x: x + 1, range(10**9)), -1) == 10**9 == _coconut_igetitem(count(), 10**9)
    assert (tuple)(_coconut_igetitem(count(), _coconut.slice(10, 15))) == (10, 11, 12, 13, 14) == (tuple)(count()[10:15])
    assert (tuple)(zip((1, 2), (3, 4))) == ((1, 3), (2, 4)) == (tuple)(_coconut_igetitem(zip((1, 2), (3, 4)), _coconut.slice(None, None)))
    assert (tuple)(_coconut_igetitem(zip((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2))), -1)) == (20, 2) == (tuple)(zip((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)))[-1])
    assert (tuple)(_coconut_igetitem(zip(count(), count()), 10**9)) == (10**9, 10**9) == (tuple)(zip(count(), count())[10**9])
    assert _coconut_igetitem(count(1.5, 0.5), 0) == 1.5 == _coconut_igetitem((1.5, 2, 2.5, 3), 0)
    assert (tuple)(_coconut_igetitem(count(1.5, 0.5), _coconut.slice(1, 3))) == (2, 2.5) == (tuple)(_coconut_igetitem((1.5, 2, 2.5, 3), _coconut.slice(1, 3)))
    assert SHOPeriodTerminate([-1, 0], 0, {"epsilon": 1})
    assert (tuple)(_coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, 2))) == (0, 2, 4)
    assert (tuple)(_coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, -1))) == (4, 3, 2, 1, 0)
    assert dict(((x), (x)) for x in range(5)) == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    _coconut_match_check = False
    _coconut_match_to = 12
    x = _coconut_match_to
    _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match x = 12'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'match x = 12'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    assert x == 12
    get_int = lambda: int
    _coconut_match_check = False
    _coconut_match_to = 5
    if (_coconut.isinstance(_coconut_match_to, get_int())):
        x = _coconut_match_to
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'x is get_int() = 5'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'x is get_int() = 5'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    assert x == 5
    class a(get_int()): pass
    assert isinstance(a(), int)
    assert (len)(map(_coconut.operator.__add__, range(5), range(6))) == 5 == (len)(zip(range(5), range(6)))
    assert map(_coconut_minus, range(5))._func(3) == -3
    assert (tuple)(map(_coconut_minus, range(5))._iters[0]) == (tuple)(range(5)) == (tuple)(zip(range(5), range(6))._iters[0])
    assert repr(zip((0, 1), (1, 2))) == "zip((0, 1), (1, 2))"
    assert repr(map(_coconut_minus, range(5))).startswith("map(")
    assert repr(parallel_map(_coconut_minus, range(5))).startswith("parallel_map(")
    assert (tuple)(parallel_map(_coconut_minus, range(5))) == (0, -1, -2, -3, -4) == (tuple)(_coconut_igetitem(parallel_map(_coconut.functools.partial(map, _coconut_minus), (range(5),)), 0))
    assert (tuple)((_coconut.functools.partial(map, tuple))(parallel_map(zip, (range(2),), (range(2),)))) == (((0, 0), (1, 1)),)
    assert (tuple)((_coconut.functools.partial(map, _coconut.operator.__add__))(*(range(0, 5), range(5, 10)))) == (5, 7, 9, 11, 13)
    assert (tuple)(parallel_map(_coconut.functools.partial(_coconut_compose(_coconut.functools.partial(_coconut.operator.__mul__, 2), _coconut.operator.__add__), 1), range(5))) == (2, 4, 6, 8, 10)
    assert 0 in range(1)
    assert range(1).count(0) == 1
    assert 2 in range(5)
    assert range(5).count(2) == 1
    assert 10 not in range(3)
    assert range(3).count(10) == 0
    assert 1 in range(1, 2, 3)
    assert range(1, 2, 3).count(1) == 1
    assert range(1, 2, 3).index(1) == 0
    assert range(1, 2, 3)[0] == 1
    assert range(1, 5, 3).index(4) == 1
    assert range(1, 5, 3)[1] == 4
    try:
        range(1, 2, 3).index(2)
    except ValueError as err:
        assert err
    else:
        assert False
    assert 0 in count()
    assert count().count(0) == 1
    assert -1 not in count()
    assert count().count(-1) == 0
    assert 1 not in count(5)
    assert count(5).count(1) == 0
    assert 2 not in count(1, 2)
    assert count(1, 2).count(2) == 0
    try:
        count(1, 2).index(2)
    except ValueError as err:
        assert err
    else:
        assert False
    assert count(1, 3).index(1) == 0
    assert count(1, 3)[0] == 1
    assert count(1, 3).index(4) == 1
    assert count(1, 3)[1] == 4

def main(doc):
    """Executes Tests."""
    assert doc
    main_test()
    if sys.version_info < (3,):
        from .py2_test import py2_test
        py2_test()
    else:
        from .py3_test import py3_test
        py3_test()
        if sys.version_info >= (3, 5):
            from .py35_test import py35_test
            py35_test()
    from . import tutorial
    print("<success>")
