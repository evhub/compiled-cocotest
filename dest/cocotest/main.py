#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe3458e5d

# Compiled with Coconut version 1.2.3-post_dev34 [Colonel]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_back_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

import sys

def main_test():
    """Basic no-dependency tests."""
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
    assert repr(3) == "3" == ascii(3)
    assert _coconut.operator.mul(2, _coconut_minus(2, 5)) == -6
    assert (list)(map(_coconut.functools.partial(pow, 2), (range)(0, 5))) == [1, 2, 4, 8, 16]
    iter1 = range(0, 10)
    iter1, iter2 = tee(iter1)
    assert (list)(_coconut_igetitem(iter1, _coconut.slice(2, 8))) == [2, 3, 4, 5, 6, 7] == (list)(_coconut_igetitem(iter1, slice(2, 8)))
    assert (list)(_coconut_igetitem(iter2, _coconut.slice(2, 8))) == [2, 3, 4, 5, 6, 7] == (list)(_coconut_igetitem(iter2, slice(2, 8)))
    data = 5
    assert data == 5
    data = 3
    assert data == 3
    def backslash_test():
        return lambda x: x
    assert 1 == 1 == backslash_test()(1)
    assert True is (
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
    class one_line_class(_coconut.object):
        pass
    assert isinstance(one_line_class(), one_line_class)
    assert (_coconut.operator.attrgetter("join"))("")(["1", "2", "3"]) == "123"
    assert (("").join)(["1", "2", "3"]) == "123"
    assert ((_coconut.functools.partial(_coconut.getattr, ""))("join"))(["1", "2", "3"]) == "123"
    assert (_coconut.functools.partial(_coconut.operator.getitem, [1, 2, 3]))(1) == 2 == (_coconut.functools.partial(_coconut_igetitem, [1, 2, 3]))(1)
    assert (_coconut.functools.partial(_coconut.operator.getitem, "123"))(1) == "2" == (_coconut.functools.partial(_coconut_igetitem, "123"))(1)
    assert (list)(_coconut.itertools.chain.from_iterable((f() for f in (lambda: (f() for f in (lambda: -1, lambda: 0)), lambda: range(1, 5))))) == [-1, 0, 1, 2, 3, 4]
    assert (list)(_coconut.itertools.chain.from_iterable((f() for f in (lambda: (f() for f in (lambda: 1,)), lambda: (f() for f in (lambda: 2,)))))) == [1, 2]
    assert not isinstance(map(_coconut.functools.partial(_coconut.operator.add, 2), [1, 2, 3]), list)
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
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
        _coconut_sentinel = _coconut.object()
        _coconut_match_key_0 = _coconut_match_to.get("text", _coconut_sentinel)
        _coconut_match_key_1 = _coconut_match_to.get("tags", _coconut_sentinel)
        if (_coconut_match_key_0 is not _coconut_sentinel) and (_coconut_match_key_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_key_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_key_1) >= 1):
            text = _coconut_match_key_0
            rest = _coconut.list(_coconut_match_key_1[1:])
            first = _coconut_match_key_1[0]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"text": text, "tags": [first] + rest} = {"text": "abc", "tags": [1, 2, 3]}\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = '{"text": text, "tags": [first] + rest} = {"text": "abc", "tags": [1, 2, 3]}'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert text == "abc"
    assert first == 1
    assert rest == [2, 3]
    assert isinstance("a", str)
    assert isinstance(b"a", bytes)
    global glob_a, glob_b
    glob_a, glob_b = 0, 0
    assert glob_a == 0 == glob_b
    def set_globs(x):
        global glob_a, glob_b
        glob_a, glob_b = x, x
    set_globs(2)
    assert glob_a == 2 == glob_b
    def set_globs_again(x):
        global glob_a, glob_b
        glob_a, glob_b = (x, x)
    set_globs_again(10)
    assert glob_a == 10 == glob_b
    assert _coconut_minus(1) == -1 == _coconut.functools.partial(_coconut_minus, 1)(2)
    assert (_coconut.operator.le)(3, 3)
    assert (list)((consume)(range(10))) == []
    assert (list)(consume(range(10), keep_last=2)) == [8, 9]
    i = int()
    try:
        i.x = 12
    except AttributeError as err:
        assert err
    else:
        assert False
    r = range(10)
    try:
        r.x = 12
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
    import email.mime.base
    assert q.Queue
    assert builtins.len([1, 1]) == 2
    assert email.mime.base
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
    class doc(_coconut.collections.namedtuple("doc", ""), _coconut.object):
        "doc"
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
    class doc_(_coconut.collections.namedtuple("doc_", ""), _coconut.object):
        """doc"""
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
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
    assert _coconut_igetitem((f() for f in (lambda: 1, lambda: 2)), -1) == 2
    assert (tuple)(_coconut_igetitem((f() for f in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), _coconut.slice(-2, None))) == (2, 3)
    assert (tuple)(_coconut_igetitem((f() for f in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), _coconut.slice(None, -2))) == (0, 1)
    assert _coconut_igetitem(map(_coconut.operator.add, (f() for f in (lambda: 10, lambda: 20)), (f() for f in (lambda: 1, lambda: 2))), -1) == 22 == map(_coconut.operator.add, (f() for f in (lambda: 10, lambda: 20)), (f() for f in (lambda: 1, lambda: 2)))[-1]
    assert _coconut_igetitem(map(lambda x: x + 1, range(10**9)), -1) == 10**9 == _coconut_igetitem(count(), 10**9)
    assert (tuple)(_coconut_igetitem(count(), _coconut.slice(10, 15))) == (10, 11, 12, 13, 14) == (tuple)(count()[10:15])
    assert (tuple)(zip((1, 2), (3, 4))) == ((1, 3), (2, 4)) == (tuple)(_coconut_igetitem(zip((1, 2), (3, 4)), _coconut.slice(None, None)))
    assert (tuple)(_coconut_igetitem(zip((f() for f in (lambda: 10, lambda: 20)), (f() for f in (lambda: 1, lambda: 2))), -1)) == (20, 2) == (tuple)(zip((f() for f in (lambda: 10, lambda: 20)), (f() for f in (lambda: 1, lambda: 2)))[-1])
    assert (tuple)(_coconut_igetitem(zip(count(), count()), 10**9)) == (10**9, 10**9) == (tuple)(zip(count(), count())[10**9])
    assert _coconut_igetitem(count(1.5, 0.5), 0) == 1.5 == _coconut_igetitem((1.5, 2, 2.5, 3), 0)
    assert (tuple)(_coconut_igetitem(count(1.5, 0.5), _coconut.slice(1, 3))) == (2, 2.5) == (tuple)(_coconut_igetitem((1.5, 2, 2.5, 3), _coconut.slice(1, 3)))
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
    if _coconut.isinstance(_coconut_match_to, get_int()):
        x = _coconut_match_to
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'x is get_int() = 5'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'x is get_int() = 5'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert x == 5
    class a(get_int()):
        pass
    assert isinstance(a(), int)
    assert (len)(map(_coconut.operator.add, range(5), range(6))) == 5 == (len)(zip(range(5), range(6)))
    assert map(_coconut_minus, range(5))._func(3) == -3
    assert (tuple)(map(_coconut_minus, range(5))._iters[0]) == (tuple)(range(5)) == (tuple)(zip(range(5), range(6))._iters[0])
    assert repr(zip((0, 1), (1, 2))) == "zip((0, 1), (1, 2))"
    assert repr(map(_coconut_minus, range(5))).startswith("map(")
    assert repr(parallel_map(_coconut_minus, range(5))).startswith("parallel_map(")
    assert (tuple)(parallel_map(_coconut_minus, range(5))) == (0, -1, -2, -3, -4) == (tuple)(_coconut_igetitem(parallel_map(_coconut.functools.partial(map, _coconut_minus), (range(5),)), 0))
    assert (tuple)(map(tuple, parallel_map(zip, (range(2),), (range(2),)))) == (((0, 0), (1, 1)),)
    assert (tuple)(map(_coconut.operator.add, *(range(0, 5), range(5, 10)))) == (5, 7, 9, 11, 13)
    assert (tuple)(parallel_map(_coconut_compose(_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 2)), range(5))) == (2, 4, 6, 8, 10)
    assert repr(concurrent_map(_coconut_minus, range(5))).startswith("concurrent_map(")
    assert (tuple)(concurrent_map(_coconut_minus, range(5))) == (0, -1, -2, -3, -4) == (tuple)(_coconut_igetitem(concurrent_map(_coconut.functools.partial(map, _coconut_minus), (range(5),)), 0))
    assert (tuple)(map(tuple, concurrent_map(zip, (range(2),), (range(2),)))) == (((0, 0), (1, 1)),)
    assert (tuple)(map(_coconut.operator.add, *(range(0, 5), range(5, 10)))) == (5, 7, 9, 11, 13)
    assert (tuple)(concurrent_map(_coconut_compose(_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 2)), range(5))) == (2, 4, 6, 8, 10)
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
    assert (len)(map(lambda x: x, [1, 2])) == 2
    assert repr("hello") == "'hello'" == ascii("hello")
    assert (count(1, 3)).index(1) == 0 == (_coconut.operator.methodcaller("index", 1))(count(1, 3))
    assert _coconut_igetitem(count(1).__copy__(), 0) == 1 == _coconut_igetitem(count(1), 0)
    assert _coconut_igetitem(map(_coconut.operator.add, count(1), count(1)).__copy__(), 0) == 2
    assert (tuple)(_coconut_igetitem(zip(count(1), count(1)).__copy__(), 0)) == (1, 1)
    assert (all)(map(lambda t: isinstance(t, count), tee(count())))
    assert (all)(map(lambda t: isinstance(t, range), tee(range(10))))
    assert (all)(map(lambda t: isinstance(t, list), tee([1, 2, 3])))
    assert (lambda _=None: 5)() == 5
    assert (lambda _=None: _[0])([1, 2, 3]) == 1
    assert (list)(_coconut_igetitem(iter(range(10)), _coconut.slice(-5, -8))) == [5, 6] == (list)(_coconut_igetitem(iter(range(10)), slice(-5, -8)))
    assert (list)(_coconut_igetitem(iter(range(10)), _coconut.slice(-2, None))) == [8, 9] == (list)(_coconut_igetitem(iter(range(10)), slice(-2, None)))
    assert (_coconut.operator.itemgetter(1))(range(1, 5)) == 2 == (_coconut.functools.partial(_coconut_igetitem, index=1))(range(1, 5))
    assert (range(1, 5))[1] == 2 == _coconut_igetitem(range(1, 5), 1)
    assert (list)((_coconut.operator.itemgetter(_coconut.slice(None, 5)))(range(10))) == [0, 1, 2, 3, 4] == (list)((_coconut.functools.partial(_coconut_igetitem, index=_coconut.slice(None, 5)))(range(10)))
    assert (list)((range(10))[_coconut.slice(None, 5)]) == [0, 1, 2, 3, 4] == (list)(_coconut_igetitem(range(10), _coconut.slice(None, 5)))
    def _coconut_lambda_0(x):
        y = x
    assert (list)(map(_coconut_lambda_0, range(10))) == [None] * 10
    def _coconut_lambda_1(x):
        yield x
    assert (list)(map(list, map(_coconut_lambda_1, range(5)))) == [[0], [1], [2], [3], [4]]
    def do_stuff(x):
        return True
    def _coconut_lambda_2(x=3):
        return do_stuff(x)
    assert (_coconut_lambda_2)() is True
    def _coconut_lambda_3(x=4):
        do_stuff(x)
        return x
    assert (_coconut_lambda_3)() == 4
    def _coconut_lambda_4(x=5):
        do_stuff(x)
    assert (_coconut_lambda_4)() is None
    def _coconut_lambda_5(x=6):
        do_stuff(x)
        assert x
    (_coconut_lambda_5)()
    def _coconut_lambda_8(x=7):
        do_stuff(x)
        assert x
        yield x
    assert (list)((_coconut_lambda_8)()) == [7]
    def _coconut_lambda_9(_=None):
        do_stuff(_)
        assert _
        return _
    assert (_coconut_lambda_9)(8) == 8
    def _coconut_lambda_10(x=9):
        return x
    assert (_coconut_lambda_10)() == 9
    def _coconut_lambda_11(x=10):
        do_stuff(x)
        return x
    assert (_coconut_lambda_11)() == 10
    def _coconut_lambda_14(_=None):
        def _coconut_lambda_13(_=None):
            return 11
        return _coconut_lambda_13
    assert (_coconut_lambda_14)()() == 11
    def _coconut_lambda_15(_=None):
        return 12
    def _coconut_lambda_16(_=None):
        return 12
    assert (_coconut_lambda_15)() == 12 == (_coconut_lambda_16)()
    def _coconut_lambda_17(x):
        return lambda _=None: x
    assert (list)(map(lambda _=None: _(), ((_coconut_lambda_17)(x) for x in range(5)))) == [0, 1, 2, 3, 4]
    herpaderp = 5
    def derp():
        herp = 10
        def _coconut_lambda_18(_=None):
            return herpaderp + herp
        return (_coconut_lambda_18)
    assert derp()() == 15
    class abc(_coconut.collections.namedtuple("abc", "xyz"), _coconut.object):
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
    assert abc(10).xyz == 10
    assert issubclass(abc, object)
    assert isinstance(abc(10), object)
    class aclass(_coconut.object): pass
    assert issubclass(aclass, object)
    assert isinstance(aclass(), object)
    assert (_coconut.operator.is_)(*tee((1, 2)))
    assert (_coconut.operator.is_)(*tee(_coconut.frozenset((1, 2))))
    assert (lambda x: 2 / x)(4) == 1 / 2
    _coconut_match_check = False
    _coconut_match_to = range(10)
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        _coconut_match_temp_0 = _coconut.list(_coconut_match_to)
        if _coconut.len(_coconut_match_temp_0) >= 2:
            b = _coconut_match_temp_0[1:-1]
            a = _coconut_match_temp_0[0]
            c = _coconut_match_temp_0[-1]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match [a, *b, c] = range(10)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'match [a, *b, c] = range(10)'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert a == 0
    assert b == [1, 2, 3, 4, 5, 6, 7, 8]
    assert c == 9
    _coconut_match_check = False
    _coconut_match_to = range(10)
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        _coconut_match_temp_0 = _coconut.list(_coconut_match_to)
        if (_coconut.len(_coconut_match_temp_0) >= 2) and (_coconut_match_temp_0[0] == _coconut_match_temp_0[-1]):
            b = _coconut_match_temp_0[1:-1]
            a = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        assert False
    else:
        assert True
    a = 1
    b = 1
    assert a == 1 == b
    assert count(5) == count(5)
    assert count(5) != count(3)
    assert {count(5): True}[count(5)]
    def _coconut_lambda_19(x):
        return x
    assert (_coconut_lambda_19)(1) == 1
    def _coconut_lambda_20(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
            xs = _coconut.list(_coconut_match_to_args[0][1:])
            x = _coconut_match_to_args[0][0]
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'assert (def ([x] + xs) -> x, xs) <| range(5) == (0, [1,2,3,4])'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'assert (def ([x] + xs) -> x, xs) <| range(5) == (0, [1,2,3,4])'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err
        return x, xs
    assert ((_coconut_lambda_20))(range(5)) == (0, [1, 2, 3, 4])
    s = "hello"  # type: str
    assert s == "hello"
    assert _coconut_partial(pow, {1: 2}, 2)(3) == 9
    assert (_coconut_partial(reduce, {0: _coconut.operator.add, 2: ()}, 3))([]) == ()
    assert (repr)(_coconut_partial(pow, {1: 2}, 2)) == "<built-in function pow>$(?, 2)"
    assert (tuple)(parallel_map(_coconut_partial(pow, {1: 2}, 2), range(10))) == (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
    assert _coconut_partial(pow, {1: 2}, 2).args == (None, 2)
    assert (tuple)((reversed)(filter(lambda x: x < 5, range(20)))) == (4, 3, 2, 1, 0) == (tuple)((reversed)(filter(lambda x: x < 5, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))))
    assert (isinstance)(((reversed)(map(lambda x: x, range(10)))), map)

    assert (tuple)((reversed)((reversed)(range(10)))) == (tuple)(range(10))
    assert (len)((reversed)(range(10))) == 10
    assert ((reversed)(range(10)))[1] == 8
    assert ((reversed)(range(10)))[-1] == 0
    assert (tuple)(((reversed)(range(10)))[_coconut.slice(None, -1)]) == (tuple)((reversed)(range(1, 10)))
    assert (tuple)(((reversed)(range(10)))[_coconut.slice(1, None)]) == (tuple)((reversed)(range(9)))
    assert (tuple)(((reversed)(range(10)))[_coconut.slice(2, -3)]) == (tuple)((reversed)(range(3, 8)))
    assert 5 in ((reversed)(range(10)))
    assert ((reversed)(range(10))).count(3) == 1
    assert ((reversed)(range(10))).count(10) == 0
    assert ((reversed)(range(10))).index(3)

    range10 = (list)(range(10))
    assert (reversed)((reversed)(range10)) == range10
    assert (len)((reversed)(range10)) == 10
    assert ((reversed)(range10))[1] == 8
    assert ((reversed)(range10))[-1] == 0
    assert (tuple)(((reversed)(range10))[_coconut.slice(None, -1)]) == (tuple)((reversed)(range(1, 10)))
    assert (tuple)(((reversed)(range10))[_coconut.slice(1, None)]) == (tuple)((reversed)(range(9)))
    assert (tuple)(((reversed)(range10))[_coconut.slice(2, -3)]) == (tuple)((reversed)(range(3, 8)))
    assert 5 in ((reversed)(range10))
    assert ((reversed)(range10)).count(3) == 1
    assert ((reversed)(range10)).count(10) == 0
    assert ((reversed)(range10)).index(3)

    assert (list)((enumerate)(range(1, 3))) == [(0, 1), (1, 2)]
    assert (list)(enumerate(range(2), start=1)) == [(1, 0), (2, 1)]
    assert (len)((enumerate)(range(10))) == 10
    assert ((enumerate)(range(10)))[1] == (1, 1)
    assert (list)(((enumerate)(range(10)))[_coconut.slice(None, 1)]) == [(0, 0)]
    assert (list)(((enumerate)(range(10)))[_coconut.slice(1, 3)]) == [(1, 1), (2, 2)]
    assert (list)(((enumerate)(range(10)))[_coconut.slice(-1, None)]) == [(9, 9)]
    assert (tuple)(range(3, 0, -1)) == (3, 2, 1)
    assert (tuple)(range(10, 0, -1)[9:1:-1]) == tuple(range(10, 0, -1))[9:1:-1]
    assert count(1)[1:] == count(2)
    assert (tuple)(reversed((x for x in range(10)))[2:-3]) == (tuple)((reversed)(range(3, 8)))
    assert (tuple)(count(1, 2)[:3]) == (1, 3, 5)
    assert (tuple)(count(0.5, 0.5)[:3]) == (0.5, 1, 1.5)
    assert fmap(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert fmap(lambda x: x + 1, (1, 2, 3)) == (2, 3, 4)
    assert fmap(lambda x: x + "!", "abc") == "a!b!c!"
    assert fmap(lambda k, v: (k + 1, v + "!"), {1: "2", 2: "3"}) == {2: "2!", 3: "3!"}
    assert fmap(lambda _=None: _ + 1, _coconut.set((1, 2, 3))) == _coconut.set((2, 3, 4))
    assert fmap(_coconut.functools.partial(_coconut.operator.add, [0]), [[1, 2, 3]]) == [[0, 1, 2, 3]]
    assert (tuple)(fmap(lambda _=None: _ + 1, range(3))) == (1, 2, 3) == (tuple)(fmap(lambda _=None: _ + 1, (f() for f in (lambda: 0, lambda: 1, lambda: 2))))
    assert issubclass(int, py_int)
    class pyobjsub(py_object): pass
    class objsub(object): pass
    assert not issubclass(pyobjsub, objsub)
    assert issubclass(objsub, object)
    assert issubclass(objsub, py_object)
    assert not issubclass(objsub, pyobjsub)
    pos = pyobjsub()
    os = objsub()
    assert not isinstance(pos, objsub)
    assert isinstance(os, objsub)
    assert isinstance(os, object)
    assert not isinstance(os, pyobjsub)
    assert [] == [ ]
    _coconut_match_check = False
    _coconut_match_to = "abc"
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.startswith("a")) and (_coconut_match_to.endswith("c")):
        b = _coconut_match_to[_coconut.len("a"):-_coconut.len("c")]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'"a" + b + "c" = "abc"\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = '"a" + b + "c" = "abc"'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert b == "b"
    _coconut_match_check = False
    _coconut_match_to = "abc"
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.startswith("a")):
        bc = _coconut_match_to[_coconut.len("a"):]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'"a" + bc = "abc"\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = '"a" + bc = "abc"'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert bc == "bc"
    _coconut_match_check = False
    _coconut_match_to = "abc"
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.endswith("c")):
        ab = _coconut_match_to[:-_coconut.len("c")]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'ab + "c" = "abc"\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'ab + "c" = "abc"'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert ab == "ab"
    _coconut_match_check = False
    _coconut_match_to = 5
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.startswith("a")):
        b = _coconut_match_to[_coconut.len("a"):]
        _coconut_match_check = True
    if _coconut_match_check:
        assert False
    assert 400 == (lambda x: (lambda x: x**2)(x * 2))(10)
    assert 100 == (lambda x: (lambda y: x**2)(x * 2))(10)
    assert 3 == (lambda x, y: x + y)(1, 2)
    _coconut_match_check = False
    _coconut_match_to = {"a": 2, "b": 3}
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
        _coconut_sentinel = _coconut.object()
        _coconut_match_key_0 = _coconut_match_to.get("a", _coconut_sentinel)
        if _coconut_match_key_0 is not _coconut_sentinel:
            a = _coconut_match_key_0
            rest = dict((k, v) for k, v in _coconut_match_to.items() if k not in set(("a",)))
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'match {"a": a, **rest} = {"a": 2, "b": 3}\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'match {"a": a, **rest} = {"a": 2, "b": 3}'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert a == 2
    assert rest == {"b": 3}
    _ = None
    _coconut_match_check = False
    _coconut_match_to = {"a": 4, "b": 5}
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
        _coconut_sentinel = _coconut.object()
        _coconut_match_key_0 = _coconut_match_to.get("a", _coconut_sentinel)
        if _coconut_match_key_0 is not _coconut_sentinel:
            a = _coconut_match_key_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'match {"a": a **_} = {"a": 4, "b": 5}\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
        _coconut_match_err.pattern = 'match {"a": a **_} = {"a": 4, "b": 5}'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert a == 4
    assert _ is None
    a = 1,
    assert a == (1,)
    (x,) = a
    assert x == 1 == a[0]
    assert (10,)[0] == 10
    x, x = 1, 2
    assert x == 2
    if _coconut_sys.version_info < (3,):
        from StringIO import StringIO
    else:
        from io import StringIO
    if _coconut_sys.version_info < (3,):
        from cStringIO import StringIO as BytesIO
    else:
        from io import BytesIO
    s = StringIO("derp")
    assert s.read() == "derp"
    b = BytesIO(b"herp")
    assert b.read() == b"herp"
    assert 2 if 1 is None else 1 == 1 == _coconut_none_coalesce(1, 2)
    assert 2 if None is None else None == 2 == _coconut_none_coalesce(None, 2)
    timeout = None  # type: _coconut.typing.Optional[int]
    local_timeout = 60  # type: _coconut.typing.Optional[int]
    global_timeout = 300  # type: int
    def ret_timeout():
# type: (...) -> _coconut.typing.Optional[int]
        return timeout
    def ret_local_timeout():
# type: (...) -> _coconut.typing.Optional[int]
        return local_timeout
    def ret_global_timeout():
# type: (...) -> int
        return global_timeout
    assert (lambda _coconut_none_coalesce_item: global_timeout if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(local_timeout) if timeout is None else timeout == 60
    assert (lambda _coconut_none_coalesce_item: (lambda _coconut_none_coalesce_item: ret_global_timeout() if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_local_timeout()) if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_timeout()) == 60
    local_timeout = None
    assert (lambda _coconut_none_coalesce_item: global_timeout if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(local_timeout) if timeout is None else timeout == 300
    assert (lambda _coconut_none_coalesce_item: (lambda _coconut_none_coalesce_item: ret_global_timeout() if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_local_timeout()) if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_timeout()) == 300
    timeout = 10 if timeout is None else timeout
    assert timeout == 10
    global_timeout = 10 if global_timeout is None else global_timeout
    assert global_timeout == 300
    assert (not True if None is None else None) is False
    assert 1 == 1 if None is None else None
    assert 'foo' in ['foo', 'bar'] if None is None else None
    assert 3 == 1 + (2 if None is None else None)
    requested_quantity = 0  # type: _coconut.typing.Optional[int]
    default_quantity = 1  # type: int
    price = 100
    assert 0 == ((lambda _coconut_none_coalesce_item: default_quantity if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(requested_quantity)) * price
    assert (_coconut_compose(_coconut.operator.itemgetter(_coconut.slice(1, None)), _coconut.operator.itemgetter(1)))(range(10)) == 2 == ((range(10))[_coconut.slice(1, None)])[1]
    assert (lambda x: None if x is None else x.herp(derp))(None) is None
    assert (lambda x: None if x is None else x[herp].derp)(None) is None
    assert (lambda x: None if x is None else x(derp)[herp])(None) is None
    assert (lambda x: None if x is None else _coconut.functools.partial(x, herp)(derp))(None) is None
    assert "a b c" == ((lambda _coconut_none_coalesce_item: "not gonna happen" if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(_coconut.functools.partial(_coconut.getattr, " ")))("join")("abc")
    a = None  # type: _coconut.typing.Optional[_coconut.typing.Sequence[int]]
    assert a is None
    return True

@_coconut_tco
def tco_func():
    while True:
        if tco_func is _coconut_recursive_func_8:
            continue
        else:
            return _coconut_tail_call(tco_func)
        return None

_coconut_recursive_func_8 = tco_func
def main(*args):
    """Asserts arguments and executes tests."""
    assert all(args)
    print(".", end="")  # ..
    assert main_test()
    print(".", end="")  # ...
    if sys.version_info >= (2, 7):
        from .specific import non_py26_test
        assert non_py26_test()
    if not (3,) <= sys.version_info < (3, 3):
        from .specific import non_py32_test
        assert non_py32_test
    print(".", end="")  # ....
    from .suite import suite_test
    from .suite import tco_test
    assert suite_test()
    print(".", end="")  # .....
    if hasattr(tco_func, "_coconut_tco_func"):
        assert tco_test()
    print(".", end="")  # ......
    if sys.version_info < (3,):
        from .py2_test import py2_test
        assert py2_test()
    else:
        from .py3_test import py3_test
        assert py3_test()
        if sys.version_info >= (3, 5):
            from .py35_test import py35_test
            assert py35_test()
    print(".", end="")  # .......
    from . import tutorial
    print("\n<success>")
