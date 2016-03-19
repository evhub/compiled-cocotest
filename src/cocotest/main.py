#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xeab279b2

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
if _coconut_sys.version_info < (3,):
    from __coconut__ import py2_chr, py2_filter, py2_hex, py2_input, py2_int, py2_map, py2_oct, py2_open, py2_print, py2_range, py2_raw_input, py2_str, py2_xrange, py2_zip, ascii, bytes, chr, filter, hex, input, int, oct, open, print, range, raw_input, str, xrange
else:
    from __coconut__ import py3_map, py3_zip
from __coconut__ import __coconut__, __coconut_version__, MatchError, map, parallel_map, zip, reduce, takewhile, dropwhile, tee, count, recursive, datamaker, consume
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------------

import sys
from .util import *

def main_test():
    """Executes the main test suite."""
    assert "\n" == ('''
''') == """
"""
    assert __coconut__
    assert __coconut_version__
    assert "__coconut__" in globals()
    assert "__coconut__" not in locals()
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
    assert set((1, 2, 3)) == __coconut__.set((1, 2, 3))
    olist = [0, 1, 2]
    olist[1] += 4
    assert olist == [0, 5, 2]
    assert +5e+5 == +5 * +10**+5
    assert (plus)(1, 1) == 2 == (__coconut__.operator.__add__)(1, 1)
    assert (plus)("1", "1") == "11" == (__coconut__.operator.__add__)("1", "1")
    assert (mod)(3, 6) == 3 == (__coconut__.operator.__mod__)(3, 6)
    assert (mod)(5, 4) == 1 == (mod_)(5, 4)
    assert (mod)(5, (plus)(2, 2)) == 1 == (__coconut__.operator.__mod__)(5, (__coconut__.operator.__add__)(2, 2))
    assert (base)("11", 2) == 3
    assert (int)("10A", 12) == 154
    assert (join_with)(["1", "2"], ", ") == "1, 2"
    assert (join_with)(["a", "b", "c"]) == "abc"
    assert (len)(__coconut__.set(("a", 5))) == 2
    assert repr(3) == "3" == ascii(3)
    assert (__coconut__.functools.partial(__coconut__.operator.__mul__, 2))((__coconut__.functools.partial((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), 2))(5)) == -6
    assert (__coconut__.functools.partial(__coconut__.operator.__mul__, 2))((__coconut__.functools.partial(swap2((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args))), 2))(5)) == 6 == (__coconut__.functools.partial(__coconut__.operator.__mul__, 2))((__coconut__.functools.partial(swap2_((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args))), 2))(5))
    assert all(same((1, 2, 3), [1, 2, 3]))
    assert (list)(chain2((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 3, lambda: 4)))) == [1, 2, 3, 4]
    assert (prod)((range)(1, 5)) == 24
    assert plus1(4) == 5 == plus1_(4)
    assert (plus1)(2) == 3 == plus1(2)
    assert plus1(plus1(5)) == 7 == (lambda *args, **kwargs: plus1((plus1)(*args, **kwargs)))(5)
    assert (sqrt)(16) == 4 == (sqrt_)(16)
    assert (square)(3) == 9
    assert sqplus1(3) == 10 == (lambda *args, **kwargs: plus1((square)(*args, **kwargs)))(3)
    assert (plus1sq)(3) == 16 == (plus1sq_)(3)
    assert (sqplus1)(3) == 10 == (sqplus1_)(3)
    assert (square)((plus1)(3)) == 16 == (square)((plus1_)(3))
    assert reduce((lambda x, f: f(x)), [3, plus1, square]) == 16 == pipe(pipe(3, plus1), square)
    assert reduce((lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs))), [sqrt, square, plus1])(3) == 4 == compose(compose(sqrt, square), plus1)(3)
    assert sum_([1, 7, 3, 5]) == 16
    assert ((list)(add([1, 2, 3], [10, 20, 30])) == [11, 22, 33] == (list)(zipsum([1, 2, 3], [10, 20, 30])))
    assert clean("   ab cd ef   ") == "ab cd ef" == (clean)("   ab cd ef   ")
    assert ((add2)(2))(3) == 5
    for qsort in [qsort1, qsort2, qsort3, qsort4, qsort5]:
        to_sort = rand_list(10)
        assert (tuple)((qsort)(to_sort)) == (tuple)((sorted)(to_sort))
    assert __coconut__.igetitem(repeat(3), 2) == 3 == __coconut__.igetitem(repeat_(3), 2)
    assert sum_(__coconut__.igetitem(repeat(1), __coconut__.slice(None, 5))) == 5 == sum_(__coconut__.igetitem(repeat_(1), __coconut__.slice(None, 5)))
    assert (sum_(takewhile(lambda x: x < 5, N())) == 10 == (sum)(__coconut__.igetitem(dropwhile(__coconut__.functools.partial(__coconut__.operator.__gt__, 0), (__coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: range(-10, 0), lambda: N()))))), __coconut__.slice(None, 5))))
    assert (sum_)(((lambda s: map(__coconut__.functools.partial(__coconut__.operator.__getitem__, s), (1, 3, 5))))("ABCDEFG")) == "BDF"
    assert (list)(map(__coconut__.functools.partial(pow, 2), (range)(0, 5))) == [1, 2, 4, 8, 16]
    assert (list)(__coconut__.igetitem(N(), __coconut__.slice(10, 15))) == [10, 11, 12, 13, 14] == (list)(__coconut__.igetitem(N_(), __coconut__.slice(10, 15)))
    assert ((list)((__coconut__.functools.partial(takewhile, __coconut__.functools.partial(__coconut__.operator.__gt__, 5)))(N())) == [0, 1, 2, 3, 4] == (list)(__coconut__.igetitem(range(0, 10), __coconut__.slice(None, 5, None))))
    assert (sum)(__coconut__.igetitem((__coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: range(-10, 0), lambda: N())))), __coconut__.slice(5, 15))) == -5 == (sum)(__coconut__.igetitem(chain(range(-10, 0), N()), __coconut__.slice(5, 15)))
    assert (list)(__coconut__.igetitem(add(repeat(1), N()), __coconut__.slice(None, 5))) == [1, 2, 3, 4, 5] == (list)(__coconut__.igetitem(add(repeat(1), N_()), __coconut__.slice(None, 5)))
    assert sum(__coconut__.igetitem(__coconut__.igetitem(N(), __coconut__.slice(5, None)), __coconut__.slice(None, 5))) == 35 == sum(__coconut__.igetitem(__coconut__.igetitem(N_(), __coconut__.slice(5, None)), __coconut__.slice(None, 5)))
    assert (list)(__coconut__.functools.partial(__coconut__.igetitem, N())(slice(5, 10))) == [5, 6, 7, 8, 9] == __coconut__.functools.partial(__coconut__.operator.__getitem__, list(range(0, 15)))(slice(5, 10))
    assert (list)(__coconut__.igetitem(N(), slice(5, 10))) == [5, 6, 7, 8, 9] == list(range(0, 15))[slice(5, 10)]
    assert (list)(__coconut__.igetitem(preN(range(-5, 0)), __coconut__.slice(1, 10))) == [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    assert (list)(__coconut__.igetitem(map_iter(__coconut__.functools.partial(__coconut__.operator.__mul__, 2), N()), __coconut__.slice(None, 5))) == [0, 2, 4, 6, 8]
    assert (tuple)(__coconut__.igetitem(N(), __coconut__.slice(None, 100))) == (tuple)(__coconut__.igetitem(N_(), __coconut__.slice(None, 100))) == (tuple)(__coconut__.igetitem(N__(), __coconut__.slice(None, 100)))
    assert (__coconut__.functools.partial(next_mul_of, 5))(12) == 15
    assert collatz(27) and collatz_(27)
    assert preop(1, 2).add() == 3
    assert (abs)(vector(3, 4)) == 5
    assert (tuple)(((lambda v: map(__coconut__.functools.partial(__coconut__.getattr, v), ("x", "y"))))(vector(1, 2))) == (1, 2)
    assert (tuple)(((lambda v: map(__coconut__.functools.partial(__coconut__.operator.__getitem__, v), (0, 1))))((vector(1, 2).transform)(vector(3, 1)))) == (4, 3)
    assert (vector(1, 2).__eq__)(vector(1, 2))
    assert not (vector(3, 4).__eq__)(vector(1, 2))
    assert not (vector(1, 2).__eq__)((1, 2))
    assert vector(vector(4, 3)) == vector(4, 3)
    assert triangle(3, 4, 5).is_right()
    assert __coconut__.getattr(triangle(3, 4, 5), "is_right")
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
    assert classify(__coconut__.set((0,))) == "set of 0" == classify(__coconut__.frozenset((0,)))
    assert classify(__coconut__.set((0, 1))) == "set" == classify(__coconut__.frozenset((1,)))
    assert classify(__coconut__.set()) == "empty set" == classify(__coconut__.frozenset())
    assert classify_sequence(()) == "empty"
    assert classify_sequence((1,)) == "singleton"
    assert classify_sequence((1, 1)) == "duplicate pair of 1"
    assert classify_sequence((1, 2)) == "pair"
    assert classify_sequence((1, 2, 3)) == "few"
    assert dictpoint({"x": 1, "y": 2}) == (1, 2)
    assert dictpoint_({"x": 1, "y": 2}) == (1, 2) == dictpoint__({"x": 1, "y": 2})
    assert map_(__coconut__.functools.partial(__coconut__.operator.__add__, 1), []) == []
    assert map_(__coconut__.functools.partial(__coconut__.operator.__add__, 1), ()) == ()
    assert map_(__coconut__.functools.partial(__coconut__.operator.__add__, 1), [0, 1, 2, 3]) == [1, 2, 3, 4]
    assert map_(__coconut__.functools.partial(__coconut__.operator.__add__, 1), (0, 1, 2, 3)) == (1, 2, 3, 4)
    assert duplicate_first1([1, 2, 3]) == [1, 1, 2, 3]
    assert (list)(duplicate_first2([1, 2, 3])) == [1, 1, 2, 3] == (list)(duplicate_first3([1, 2, 3]))
    assert one_to_five([1, 2, 3, 4, 5]) == [2, 3, 4]
    assert not one_to_five([0, 1, 2, 3, 4, 5])
    assert one_to_five([1, 5]) == []
    assert -4 == neg_square_u(2) != 4 & 0 <= neg_square_u(0) <= 0
    iter1 = range(0, 10)
    iter1, iter2 = tee(iter1)
    assert (list)(__coconut__.igetitem(iter1, __coconut__.slice(2, 8))) == (list)(__coconut__.igetitem(iter2, __coconut__.slice(2, 8)))
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
    class one_line_class(__coconut__.object): pass
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
    assert ((__coconut__.operator.attrgetter("join"))(""))(["1", "2", "3"]) == "123" == ((__coconut__.functools.partial(__coconut__.getattr, ""))("join"))(["1", "2", "3"])
    assert ((__coconut__.functools.partial(__coconut__.functools.partial, mod))(5))(3) == 2 == ((__coconut__.functools.partial(__coconut__.functools.partial, __coconut__.operator.__mod__))(5))(3)
    assert (__coconut__.functools.partial(__coconut__.operator.__getitem__, [1, 2, 3]))(1) == 2 == (__coconut__.functools.partial(__coconut__.igetitem, [1, 2, 3]))(1)
    assert (__coconut__.functools.partial(__coconut__.operator.__getitem__, "123"))(1) == "2" == (__coconut__.functools.partial(__coconut__.igetitem, "123"))(1)
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
    except (MatchError) as err:
        assert err.pattern == "match def strmul(a is str, x is int):"
        assert err.value == ("a", "b")
    else:
        assert False
    assert (list)(__coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: -1, lambda: 0)), lambda: range(1, 5))))) == [-1, 0, 1, 2, 3, 4]
    assert (list)(__coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1,)), lambda: (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 2,)))))) == [1, 2]
    laz = lazy()
    assert not laz.done
    lazl = laz.list()
    assert (list)(__coconut__.igetitem(lazl, __coconut__.slice(None, 3))) == [1, 2, 3]
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
    assert not isinstance(map(__coconut__.functools.partial(__coconut__.operator.__add__, 2), [1, 2, 3]), list)
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
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Mapping)) and (__coconut__.len(_coconut_match_to) == 2) and ("text" in _coconut_match_to) and ("tags" in _coconut_match_to) and (__coconut__.isinstance(_coconut_match_to["tags"], __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to["tags"]) >= 1):
        text = _coconut_match_to["text"]
        rest = __coconut__.list(_coconut_match_to["tags"][1:])
        first = _coconut_match_to["tags"][0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " '\'{"text": text, "tags": [first] + rest} = {"text": "abc", "tags": [1, 2, 3]}\'' " in " + __coconut__.repr(__coconut__.repr(_coconut_match_to)))
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
    assert (lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args))(1) == -1 == __coconut__.functools.partial((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), 1)(2)
    assert pt.__doc__
    out0 = (__coconut__.functools.partial(grid_trim, xmax=5, ymax=5))(grid())
    assert out0 == [[pt(x=0, y=0), pt(x=0, y=1), pt(x=0, y=2), pt(x=0, y=3), pt(x=0, y=4)], [pt(x=1, y=0), pt(x=1, y=1), pt(x=1, y=2), pt(x=1, y=3), pt(x=1, y=4)], [pt(x=2, y=0), pt(x=2, y=1), pt(x=2, y=2), pt(x=2, y=3), pt(x=2, y=4)], [pt(x=3, y=0), pt(x=3, y=1), pt(x=3, y=2), pt(x=3, y=3), pt(x=3, y=4)], [pt(x=4, y=0), pt(x=4, y=1), pt(x=4, y=2), pt(x=4, y=3), pt(x=4, y=4)]]
    out1 = (__coconut__.functools.partial(grid_trim, xmax=5, ymax=5))((__coconut__.functools.partial(grid_map, abs))(grid()))
    out1_ = (list)((__coconut__.functools.partial(map, list))((__coconut__.functools.partial(parallel_grid_map, abs))((__coconut__.functools.partial(grid_trim, xmax=5, ymax=5))(grid()))))
    assert out1[0] == [0.0, 1.0, 2.0, 3.0, 4.0] == out1_[0]
    assert out1[1][0] == 1.0 == out1_[1][0]
    assert out1[2][0] == 2.0 == out1_[2][0]
    assert out1[3][0] == 3.0 == out1_[3][0]
    assert out1[3][4] == 5.0 == out1_[3][4]
    assert out1[4][0] == 4.0 == out1_[4][0]
    assert out1[4][3] == 5.0 == out1_[4][3]
    assert (__coconut__.operator.__le__)(3, 3)
    assert (list)((consume)(range(10))) == []
    assert (list)((__coconut__.functools.partial(consume, keep_last=2))(range(10))) == [8, 9]
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
    x = (lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs)))(x, (__coconut__.functools.partial(__coconut__.operator.__add__, 1)))
    x = x((4))
    assert x == 25
    i = int()
    try:
        i.x = 12
    except (AttributeError) as err:
        assert err
    else:
        assert False
    b = bytes()
    try:
        b.x = 12
    except (AttributeError) as err:
        assert err
    else:
        assert False
    v = vector(1, 2)
    try:
        v.x = 3
    except (AttributeError) as err:
        assert err
    else:
        assert False
    try:
        v.new_attr = True
    except (AttributeError) as err:
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
            email = __coconut__.imp.new_module("email")
        else:
            if not __coconut__.isinstance(email, __coconut__.types.ModuleType):
                email = __coconut__.imp.new_module("email")

        try:
            email.mime
        except:
            email.mime = __coconut__.imp.new_module("email.mime")
        else:
            if not __coconut__.isinstance(email.mime, __coconut__.types.ModuleType):
                email.mime = __coconut__.imp.new_module("email.mime")
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
    except (ValueError) as err:
        assert err.__cause__ is from_err
    else:
        assert False
    class doc(__coconut__.collections.namedtuple("doc", "")):
        "doc"
        __slots__ = ()
    class doc_(__coconut__.collections.namedtuple("doc_", "")):
        """doc"""
        __slots__ = ()
    assert doc.__doc__ == "doc" == doc_.__doc__
    assert 10000000.0 == 10000000.0
    assert (tuple)(__coconut__.iter(())) == ()
    import collections
    if _coconut_sys.version_info < (3, 3):
        import collections as _coconut_import
        try:
            collections
        except:
            collections = __coconut__.imp.new_module("collections")
        else:
            if not __coconut__.isinstance(collections, __coconut__.types.ModuleType):
                collections = __coconut__.imp.new_module("collections")
        collections.abc = _coconut_import
    else:
        import collections.abc

    assert isinstance([], collections.abc.Sequence)
    assert collections.defaultdict(int)[5] == 0
    assert len(range(10)) == 10
    assert (tuple)((reversed)(range(4))) == (3, 2, 1, 0)
    assert (tuple)(range(5)[1:]) == (1, 2, 3, 4) == (tuple)(__coconut__.igetitem(range(5), __coconut__.slice(1, None)))
    assert (tuple)(range(10)[-3:-1]) == (7, 8) == (tuple)(__coconut__.igetitem(range(10), __coconut__.slice(-3, -1)))
    assert (tuple)(__coconut__.igetitem(map(abs, (1, -2, -5, 2)), __coconut__.slice(None, None))) == (1, 2, 5, 2)
    assert __coconut__.igetitem((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)), -1) == 2
    assert (tuple)(__coconut__.igetitem((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), __coconut__.slice(-2, None))) == (2, 3)
    assert (tuple)(__coconut__.igetitem((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), __coconut__.slice(None, -2))) == (0, 1)
    assert __coconut__.igetitem(map(__coconut__.operator.__add__, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2))), -1) == 22 == map(__coconut__.operator.__add__, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)))[-1]
    assert __coconut__.igetitem(map(lambda x: x + 1, range(10**9)), -1) == 10**9 == __coconut__.igetitem(count(), 10**9)
    assert (tuple)(__coconut__.igetitem(count(), __coconut__.slice(10, 15))) == (10, 11, 12, 13, 14) == (tuple)(count()[10:15])
    assert (tuple)(zip((1, 2), (3, 4))) == ((1, 3), (2, 4)) == (tuple)(__coconut__.igetitem(zip((1, 2), (3, 4)), __coconut__.slice(None, None)))
    assert (tuple)(__coconut__.igetitem(zip((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2))), -1)) == (20, 2) == (tuple)(zip((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 10, lambda: 20)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)))[-1])
    assert (tuple)(__coconut__.igetitem(zip(count(), count()), 10**9)) == (10**9, 10**9) == (tuple)(zip(count(), count())[10**9])
    assert __coconut__.igetitem(count(1.5, 0.5), 0) == 1.5 == __coconut__.igetitem((1.5, 2, 2.5, 3), 0)
    assert (tuple)(__coconut__.igetitem(count(1.5, 0.5), __coconut__.slice(1, 3))) == (2, 2.5) == (tuple)(__coconut__.igetitem((1.5, 2, 2.5, 3), __coconut__.slice(1, 3)))
    assert SHOPeriodTerminate([-1, 0], 0, {"epsilon": 1})
    assert (tuple)(__coconut__.igetitem(iter((0, 1, 2, 3, 4)), __coconut__.slice(None, None, 2))) == (0, 2, 4)
    assert (tuple)(__coconut__.igetitem(iter((0, 1, 2, 3, 4)), __coconut__.slice(None, None, -1))) == (4, 3, 2, 1, 0)
    assert dict(((x), (x)) for x in range(5)) == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    _coconut_match_check = False
    _coconut_match_to = 12
    x = _coconut_match_to
    _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'match x = 12'" " in " + __coconut__.repr(__coconut__.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'match x = 12'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    assert x == 12
    get_int = lambda: int
    _coconut_match_check = False
    _coconut_match_to = 5
    if (__coconut__.isinstance(_coconut_match_to, get_int())):
        x = _coconut_match_to
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = __coconut__.MatchError("pattern-matching failed for " "'x is get_int() = 5'" " in " + __coconut__.repr(__coconut__.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'x is get_int() = 5'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err
    assert x == 5
    class a(get_int()): pass
    assert isinstance(a(), int)
    assert (len)(map(__coconut__.operator.__add__, range(5), range(6))) == 5 == (len)(zip(range(5), range(6)))
    assert map((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), range(5))._func(3) == -3
    assert (tuple)(map((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), range(5))._iters[0]) == (tuple)(range(5)) == (tuple)(zip(range(5), range(6))._iters[0])
    assert repr(zip((0, 1), (1, 2))) == "zip((0, 1), (1, 2))"
    assert repr(map((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), range(5))).startswith("map(")
    assert repr(parallel_map(__coconut__.functools.partial(__coconut__.operator.__mul__, -1), range(5))).startswith("parallel_map(")
    assert (tuple)(parallel_map(__coconut__.functools.partial(__coconut__.operator.__mul__, -1), range(5))) == (0, -1, -2, -3, -4) == (tuple)(__coconut__.igetitem(parallel_map(__coconut__.functools.partial(map, __coconut__.functools.partial(__coconut__.operator.__mul__, -1)), (range(5),)), 0))
    assert (tuple)((__coconut__.functools.partial(map, tuple))(parallel_map(zip, (range(2),), (range(2),)))) == (((0, 0), (1, 1)),)
    assert (tuple)((__coconut__.functools.partial(map, __coconut__.operator.__add__))(*(range(0, 5), range(5, 10)))) == (5, 7, 9, 11, 13)

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
    from . import tutorial
    print("<success>")
