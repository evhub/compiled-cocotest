#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1debce57

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

sys = _coconut_sys
if _coconut_sys.version_info < (3, 4):  # type: ignore
    import trollius as asyncio  # type: ignore
else:  # type: ignore
    import asyncio  # type: ignore


def assert_raises(c, exc):
    """Test whether callable c raises an exception of type exc."""
    try:
        c()
    except exc:
        return True
    else:
        raise AssertionError("%r failed to raise exception %r" % (c, exc))

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
    range10 = range(0, 10)
    reiter_range10 = reiterable(range10)
    reiter_iter_range10 = reiterable(iter(range10))
    for iter1, iter2 in [tee(range10), tee(iter(range10)), (reiter_range10, reiter_range10), (reiter_iter_range10, reiter_iter_range10),]:
        assert (list)(_coconut_igetitem(iter1, _coconut.slice(2, 8))) == [2, 3, 4, 5, 6, 7] == (list)(_coconut_igetitem(iter2, slice(2, 8))), (iter1, iter2)
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
    assert (list)(_coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: (_coconut_func() for _coconut_func in (lambda: -1, lambda: 0)), lambda: range(1, 5))))) == [-1, 0, 1, 2, 3, 4]
    assert (list)(_coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: (_coconut_func() for _coconut_func in (lambda: 1,)), lambda: (_coconut_func() for _coconut_func in (lambda: 2,)))))) == [1, 2]
    assert not isinstance(map(_coconut.functools.partial(_coconut.operator.add, 2), [1, 2, 3]), list)
    assert not isinstance(range(10), list)
    longint = 10**100  # type: int
    assert isinstance(longint, int)
    assert chr(1000)
    assert (abs)(3 + 4j) == 5
    assert 3.14j == 3.14j
    assert 10.j == 10.j
    assert 10j == 10j
    assert .001j == .001j
    assert 1e100j == 1e100j
    assert 3.14e-10j == 3.14e-10j
    _coconut_match_to = {"text": "abc", "tags": [1, 2, 3]}
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
        _coconut_match_temp_0 = _coconut_match_to.get("text", _coconut_sentinel)
        _coconut_match_temp_1 = _coconut_match_to.get("tags", _coconut_sentinel)
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_1) >= 1):
            text = _coconut_match_temp_0
            rest = _coconut.list(_coconut_match_temp_1[1:])
            first = _coconut_match_temp_1[0]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"text": text, "tags": [first] + rest} = {"text": "abc", "tags": [1, 2, 3]}\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
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
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    class doc_(_coconut.collections.namedtuple("doc_", ""), _coconut.object):
        """doc"""
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    assert doc.__doc__ == "doc" == doc_.__doc__
    assert 10000000.0 == 10000000.0
    assert (tuple)(_coconut.iter(())) == ()
    import collections
    if _coconut_sys.version_info < (3, 3):
        import collections as _coconut_import
        try:
            collections
        except:
            collections = _coconut.types.ModuleType("collections")
        else:
            if not _coconut.isinstance(collections, _coconut.types.ModuleType):
                collections = _coconut.types.ModuleType("collections")
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
    assert _coconut_igetitem((_coconut_func() for _coconut_func in (lambda: 1, lambda: 2)), -1) == 2
    assert (tuple)(_coconut_igetitem((_coconut_func() for _coconut_func in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), _coconut.slice(-2, None))) == (2, 3)
    assert (tuple)(_coconut_igetitem((_coconut_func() for _coconut_func in (lambda: 0, lambda: 1, lambda: 2, lambda: 3)), _coconut.slice(None, -2))) == (0, 1)
    assert _coconut_igetitem(map(_coconut.operator.add, (_coconut_func() for _coconut_func in (lambda: 10, lambda: 20)), (_coconut_func() for _coconut_func in (lambda: 1, lambda: 2))), -1) == 22 == map(_coconut.operator.add, (_coconut_func() for _coconut_func in (lambda: 10, lambda: 20)), (_coconut_func() for _coconut_func in (lambda: 1, lambda: 2)))[-1]
    assert _coconut_igetitem(map(lambda x: x + 1, range(10**9)), -1) == 10**9 == _coconut_igetitem(count(), 10**9)
    assert (tuple)(_coconut_igetitem(count(), _coconut.slice(10, 15))) == (10, 11, 12, 13, 14) == (tuple)(count()[10:15])
    assert (tuple)(zip((1, 2), (3, 4))) == ((1, 3), (2, 4)) == (tuple)(_coconut_igetitem(zip((1, 2), (3, 4)), _coconut.slice(None, None)))
    assert (tuple)(_coconut_igetitem(zip((_coconut_func() for _coconut_func in (lambda: 10, lambda: 20)), (_coconut_func() for _coconut_func in (lambda: 1, lambda: 2))), -1)) == (20, 2) == (tuple)(zip((_coconut_func() for _coconut_func in (lambda: 10, lambda: 20)), (_coconut_func() for _coconut_func in (lambda: 1, lambda: 2)))[-1])
    assert (tuple)(_coconut_igetitem(zip(count(), count()), 10**9)) == (10**9, 10**9) == (tuple)(zip(count(), count())[10**9])
    assert _coconut_igetitem(count(1.5, 0.5), 0) == 1.5 == _coconut_igetitem((1.5, 2, 2.5, 3), 0)
    assert (tuple)(_coconut_igetitem(count(1.5, 0.5), _coconut.slice(1, 3))) == (2, 2.5) == (tuple)(_coconut_igetitem((1.5, 2, 2.5, 3), _coconut.slice(1, 3)))
    import platform
    if sys.version_info < (3,) or platform.python_implementation() != "PyPy":  # TODO: remove when pypy3 fixes this error
        assert (tuple)(_coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, 2))) == (0, 2, 4), (iter((0, 1, 2, 3, 4)), _coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, 2)), (tuple)(_coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, 2))))
    assert (tuple)(_coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, -1))) == (4, 3, 2, 1, 0), (iter((0, 1, 2, 3, 4)), _coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, -1)), (tuple)(_coconut_igetitem(iter((0, 1, 2, 3, 4)), _coconut.slice(None, None, -1))))
    assert dict(((x), (x)) for x in range(5)) == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    _coconut_match_to = 12
    _coconut_match_check = False
    x = _coconut_match_to
    _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match x = 12'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match x = 12'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert x == 12
    get_int = lambda: int
    _coconut_match_to = 5
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, get_int()):
        x = _coconut_match_to
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'x is get_int() = 5'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'x is get_int() = 5'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert x == 5
    class a(get_int()):
        pass
    assert isinstance(a(), int)
    assert (len)(map(_coconut.operator.add, range(5), range(6))) == 5 == (len)(zip(range(5), range(6)))
    assert map(_coconut_minus, range(5)).func(3) == -3
    assert (tuple)(map(_coconut_minus, range(5)).iters[0]) == (tuple)(range(5)) == (tuple)(zip(range(5), range(6)).iters[0])
    assert repr(zip((0, 1), (1, 2))) == "zip((0, 1), (1, 2))"
    assert repr(map(_coconut_minus, range(5))).startswith("map(")
    assert repr(parallel_map(_coconut_minus, range(5))).startswith("parallel_map(")
    assert (tuple)(parallel_map(_coconut_minus, range(5))) == (0, -1, -2, -3, -4) == (tuple)(_coconut_igetitem(parallel_map(_coconut.functools.partial(map, _coconut_minus), (range(5),)), 0))
    assert (tuple)(map(tuple, parallel_map(zip, (range(2),), (range(2),)))) == (((0, 0), (1, 1)),)
    assert (tuple)(map(_coconut.operator.add, *(range(0, 5), range(5, 10)))) == (5, 7, 9, 11, 13)
    assert (tuple)(parallel_map(_coconut_forward_compose(_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 2)), range(5))) == (2, 4, 6, 8, 10)
    assert repr(concurrent_map(_coconut_minus, range(5))).startswith("concurrent_map(")
    assert (tuple)(concurrent_map(_coconut_minus, range(5))) == (0, -1, -2, -3, -4) == (tuple)(_coconut_igetitem(concurrent_map(_coconut.functools.partial(map, _coconut_minus), (range(5),)), 0))
    assert (tuple)(map(tuple, concurrent_map(zip, (range(2),), (range(2),)))) == (((0, 0), (1, 1)),)
    assert (tuple)(map(_coconut.operator.add, *(range(0, 5), range(5, 10)))) == (5, 7, 9, 11, 13)
    assert (tuple)(concurrent_map(_coconut_forward_compose(_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 2)), range(5))) == (2, 4, 6, 8, 10)
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
    assert (lambda _=None: 5)() == 5  # type: ignore
    assert (lambda _=None: _[0])([1, 2, 3]) == 1  # type: ignore
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
    def _coconut_lambda_6(x=7):
        do_stuff(x)
        assert x
        yield x
    assert (list)((_coconut_lambda_6)()) == [7]
    def _coconut_lambda_7(_=None):
        do_stuff(_)
        assert _
        return _
    assert (_coconut_lambda_7)(8) == 8
    def _coconut_lambda_8(x=9):
        return x
    assert (_coconut_lambda_8)() == 9
    def _coconut_lambda_9(x=10):
        do_stuff(x)
        return x
    assert (_coconut_lambda_9)() == 10
    def _coconut_lambda_11(_=None):
        def _coconut_lambda_10(_=None):
            return 11
        return _coconut_lambda_10
    assert (_coconut_lambda_11)()() == 11
    def _coconut_lambda_12(_=None):
        return 12
    def _coconut_lambda_13(_=None):
        return 12
    assert (_coconut_lambda_12)() == 12 == (_coconut_lambda_13)()
    def _coconut_lambda_14(x):  # type: ignore
        return lambda _=None: x  # type: ignore
    assert (list)(map(lambda _=None: _(), ((_coconut_lambda_14)(x) for x in range(5)))) == [0, 1, 2, 3, 4]  # type: ignore
    herpaderp = 5
    def derp():
        herp = 10
        def _coconut_lambda_15(_=None):  # type: ignore
            return herpaderp + herp  # type: ignore
        return (_coconut_lambda_15)  # type: ignore
    assert derp()() == 15
    class abc(_coconut.collections.namedtuple("abc", "xyz"), _coconut.object):
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)

    class abc_(_coconut.typing.NamedTuple("abc_", [("xyz", 'int')]), _coconut.object):
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)

    assert abc(10).xyz == 10 == abc_(10).xyz
    assert issubclass(abc, object)
    assert issubclass(abc_, object)
    assert isinstance(abc(10), object)
    assert isinstance(abc_(10), object)
    assert hash(abc(10)) == hash(abc(10))
    assert hash(abc(10)) != hash(abc_(10)) != hash((10,))
    class aclass(_coconut.object): pass
    assert issubclass(aclass, object)
    assert isinstance(aclass(), object)
    assert (_coconut.operator.is_)(*tee((1, 2)))
    assert (_coconut.operator.is_)(*tee(_coconut.frozenset((1, 2))))
    assert (lambda x: 2 / x)(4) == 1 / 2
    _coconut_match_to = range(10)
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable):
        _coconut_match_temp_0 = _coconut.list(_coconut_match_to)
        if _coconut.len(_coconut_match_temp_0) >= 2:
            b = _coconut_match_temp_0[1:-1]
            a = _coconut_match_temp_0[0]
            c = _coconut_match_temp_0[-1]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match [a, *b, c] = range(10)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match [a, *b, c] = range(10)'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert a == 0
    assert b == [1, 2, 3, 4, 5, 6, 7, 8]
    assert c == 9
    _coconut_match_to = range(10)
    _coconut_match_check = False
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
    def _coconut_lambda_16(x):
        return x
    assert (_coconut_lambda_16)(1) == 1
    def _coconut_lambda_17(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
            xs = _coconut.list(_coconut_match_to_args[0][1:])
            x = _coconut_match_to_args[0][0]
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'assert (def ([x] + xs) -> x, xs) <| range(5) == (0, [1,2,3,4])'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'assert (def ([x] + xs) -> x, xs) <| range(5) == (0, [1,2,3,4])'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err
        return x, xs
    assert ((_coconut_lambda_17))(range(5)) == (0, [1, 2, 3, 4])
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

    assert (list)(groupsof(1, range(1, 11))) == [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
    assert (list)(groupsof(2, range(1, 11))) == [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    assert (list)(groupsof(2.5, range(1, 11))) == [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    assert (list)(groupsof(3, range(1, 11))) == [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)]
    assert (list)(groupsof(4, range(1, 11))) == [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10)]
    assert_raises(lambda: groupsof("A", range(1, 11)), TypeError)
    assert_raises(lambda: groupsof(0, range(1, 11)), ValueError)
    assert_raises(lambda: groupsof(-1, range(1, 11)), ValueError)

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
    assert fmap(lambda _=None: _ + 1, _coconut.set((1, 2, 3))) == _coconut.set((2, 3, 4))  # type: ignore
    assert fmap(_coconut.functools.partial(_coconut.operator.add, [0]), [[1, 2, 3]]) == [[0, 1, 2, 3]]
    assert (tuple)(fmap(lambda _=None: _ + 1, range(3))) == (1, 2, 3) == (tuple)(fmap(lambda _=None: _ + 1, (_coconut_func() for _coconut_func in (lambda: 0, lambda: 1, lambda: 2))))  # type: ignore
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
    _coconut_match_to = "abc"
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.startswith("a")) and (_coconut_match_to.endswith("c")):
        b = _coconut_match_to[_coconut.len("a"):-_coconut.len("c")]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'"a" + b + "c" = "abc"\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = '"a" + b + "c" = "abc"'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert b == "b"
    _coconut_match_to = "abc"
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.startswith("a")):
        bc = _coconut_match_to[_coconut.len("a"):]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'"a" + bc = "abc"\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = '"a" + bc = "abc"'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert bc == "bc"
    _coconut_match_to = "abc"
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.endswith("c")):
        ab = _coconut_match_to[:-_coconut.len("c")]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'ab + "c" = "abc"\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'ab + "c" = "abc"'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert ab == "ab"
    _coconut_match_to = 5
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.startswith("a")):
        b = _coconut_match_to[_coconut.len("a"):]
        _coconut_match_check = True
    if _coconut_match_check:
        assert False
    assert 400 == (lambda x: (lambda x: x**2)(x * 2))(10)
    assert 100 == (lambda x: (lambda y: x**2)(x * 2))(10)
    assert 3 == (lambda x, y: x + y)(1, 2)
    _coconut_match_to = {"a": 2, "b": 3}
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
        _coconut_match_temp_0 = _coconut_match_to.get("a", _coconut_sentinel)
        if _coconut_match_temp_0 is not _coconut_sentinel:
            a = _coconut_match_temp_0
            rest = dict((k, v) for k, v in _coconut_match_to.items() if k not in set(("a",)))
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'match {"a": a, **rest} = {"a": 2, "b": 3}\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match {"a": a, **rest} = {"a": 2, "b": 3}'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert a == 2
    assert rest == {"b": 3}
    _ = None
    _coconut_match_to = {"a": 4, "b": 5}
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
        _coconut_match_temp_0 = _coconut_match_to.get("a", _coconut_sentinel)
        if _coconut_match_temp_0 is not _coconut_sentinel:
            a = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'match {"a": a **_} = {"a": 4, "b": 5}\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
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
    if _coconut_sys.version_info < (2, 7):
        from StringIO import StringIO
    else:
        from io import StringIO
    if _coconut_sys.version_info < (2, 7):
        from cStringIO import StringIO as BytesIO
    else:
        from io import BytesIO
    s = StringIO("derp")
    assert s.read() == "derp"
    b = BytesIO(b"herp")
    assert b.read() == b"herp"
    assert (2 if 1 is None else 1) == 1 == _coconut_none_coalesce(1, 2)
    assert (2 if None is None else None) == 2 == _coconut_none_coalesce(None, 2)
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
    assert ((lambda _coconut_none_coalesce_item: global_timeout if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(local_timeout) if timeout is None else timeout) == 60
    assert (lambda _coconut_none_coalesce_item: (lambda _coconut_none_coalesce_item: ret_global_timeout() if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_local_timeout()) if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_timeout()) == 60
    local_timeout = None
    assert ((lambda _coconut_none_coalesce_item: global_timeout if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(local_timeout) if timeout is None else timeout) == 300
    assert (lambda _coconut_none_coalesce_item: (lambda _coconut_none_coalesce_item: ret_global_timeout() if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_local_timeout()) if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(ret_timeout()) == 300
    timeout = 10 if timeout is None else timeout
    assert timeout == 10
    global_timeout = 10 if global_timeout is None else global_timeout
    assert global_timeout == 300
    assert (not (True if None is None else None)) is False
    assert 1 == (1 if None is None else None)
    assert 'foo' in (['foo', 'bar'] if None is None else None)
    assert 3 == 1 + ((2 if None is None else None))
    requested_quantity = 0  # type: _coconut.typing.Optional[int]
    default_quantity = 1  # type: int
    price = 100
    assert 0 == ((lambda _coconut_none_coalesce_item: default_quantity if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(requested_quantity)) * price
    assert (_coconut_forward_compose(_coconut.operator.itemgetter(_coconut.slice(1, None)), _coconut.operator.itemgetter(1)))(range(10)) == 2 == ((range(10))[_coconut.slice(1, None)])[1]
    assert (lambda x: None if x is None else x.herp(derp))(None) is None  # type: ignore
    assert (lambda x: None if x is None else x[herp].derp)(None) is None  # type: ignore
    assert (lambda x: None if x is None else x(derp)[herp])(None) is None  # type: ignore
    assert (lambda x: None if x is None else _coconut.functools.partial(x, herp)(derp))(None) is None  # type: ignore
    assert "a b c" == ((lambda _coconut_none_coalesce_item: "not gonna happen" if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(_coconut.functools.partial(_coconut.getattr, " ")))("join")("abc")
    a = None  # type: _coconut.typing.Optional[_coconut.typing.Sequence[int]]
    assert a is None
    assert ((reiterable)((iter)(range(5))))[1] == 1
    assert (list)(fmap(lambda _=None: _ + 1, (reiterable)(range(5)))) == [1, 2, 3, 4, 5]  # type: ignore

    a = _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: [1], lambda: [2], lambda: [3])))  # type: Iterable[int]
    a = (reiterable)(a)
    b = (reiterable)(a)
    assert (list)(b) == [1, 2, 3]
    assert (list)(b) == [1, 2, 3]
    assert (list)(a) == [1, 2, 3]
    assert (list)(a) == [1, 2, 3]

    assert (repr)(_coconut_base_compose(_coconut.operator.add, (_coconut.operator.add, 1))) == "<built-in function add> ..*> <built-in function add>"
    assert (list)(scan(_coconut.operator.add, [1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    assert (list)(scan(_coconut.operator.mul, [1, 2, 3, 4, 5])) == [1, 2, 6, 24, 120]
    assert (list)(scan(_coconut.operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert (list)(scan(_coconut.operator.mul, [1, 2, 3, 4], -1)) == [-1, -1, -2, -6, -24]
    input_data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    assert (list)(scan(_coconut.operator.mul, input_data)) == [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
    assert (list)(scan(max, input_data)) == [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
    a = "test"  # type: str
    assert a == "test" and isinstance(a, str)
    ten = 10
    where = ten
    assert where == 10 == where
    true = True
    assert true
    _coconut_match_to = {"a": 5}
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 1):
        _coconut_match_temp_0 = _coconut_match_to.get("a", _coconut_sentinel)
        if _coconut_match_temp_0 is not _coconut_sentinel:
            a = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"a": a} = {"a": 5}\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = '{"a": a} = {"a": 5}'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert a == 5
    assert ((False if None is None else None) is False) is True
    assert ((False if 1 is None else 1) is False) is False
    loop = asyncio.new_event_loop()
    loop.close()
    assert _coconut.Ellipsis is Ellipsis
    assert 1 or 2
    two = None
    _coconut_match_to = False
    _coconut_case_check_0 = False
    if _coconut_match_to is False:
        _coconut_case_check_0 = True
    if _coconut_case_check_0:
        _coconut_match_to = True
        _coconut_match_check = False
        if _coconut_match_to is False:
            _coconut_match_check = True
        if _coconut_match_check:
            two = 1
        else:
            two = 2
    if not _coconut_case_check_0:
        if _coconut_match_to is True:
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            two = 3
    if not _coconut_case_check_0:
        two = 4
    assert two == 2
    assert makedata(list, 1, 2, 3) == [1, 2, 3]
    assert makedata(str, "a", "b", "c") == "abc"
    assert makedata(dict, ("a", 1), ("b", 2)) == {"a": 1, "b": 2}
    _coconut_match_to = [1]
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, list)) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
        a = _coconut_match_to[0]
        _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'[a] is list = [1]'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = '[a] is list = [1]'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert a == 1
    assert makedata(type(_coconut.iter(())), 1, 2) == (1, 2) == makedata(type(_coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: (), lambda: ())))), 1, 2)
    all_none = (reversed)(count(None, 0))
    assert _coconut_igetitem(all_none, 0) is None
    assert (list)(_coconut_igetitem(all_none, _coconut.slice(None, 3))) == [None, None, None]
    assert None in all_none
    assert _coconut.operator.add not in all_none
    assert all_none.count(0) == 0
    assert all_none.count(None) == float("inf")
    assert all_none.index(None) == 0
    _coconut_match_to = [1]
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
        _coconut_match_check = True
    if not _coconut_match_check:
        assert True
    else:
        assert False
    _coconut_match_to = []
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) >= 1):
        t = _coconut.list(_coconut_match_to[1:])
        h = _coconut_match_to[0]
        _coconut_match_check = True
    if not _coconut_match_check:
        assert True
    else:
        assert False
    assert 4 == _coconut_igetitem(filter(lambda i: i > 3, range(2, 20)), 0)
    if _coconut_sys.version_info < (3, 4):
        from imp import reload
    else:
        from importlib import reload
    x = 1
    y = "2"
    assert "{_coconut_format_0} == {_coconut_format_1}".format(_coconut_format_0=(x), _coconut_format_1=(y)) == "1 == 2"
    assert "{_coconut_format_0!r} == {_coconut_format_1!r}".format(_coconut_format_0=(x), _coconut_format_1=(y)) == "1 == " + py_repr("2")
    assert "{_coconut_format_0}".format(_coconut_format_0=(({}))) == "{}" == "{_coconut_format_0!r}".format(_coconut_format_0=(({})))
    assert "{{".format() == "{"
    assert "}}".format() == "}"
    assert "{_coconut_format_0}".format(_coconut_format_0=(1, 2)) == "(1, 2)"
    assert "{_coconut_format_0}".format(_coconut_format_0=((len)([]))) == "0"
    _coconut_match_to = {"a": {"b": {"c": "x"}}}
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 1):
        _coconut_match_temp_0 = _coconut_match_to.get("a", _coconut_sentinel)
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_0, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_temp_0) == 1):
            _coconut_match_temp_1 = _coconut_match_temp_0.get("b", _coconut_sentinel)
            if _coconut_match_temp_1 is not _coconut_sentinel:
                x = _coconut_match_temp_1
                _coconut_match_check = True
    if (not _coconut_match_check) and (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 1):
        _coconut_match_temp_0 = _coconut_match_to.get("a", _coconut_sentinel)
        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_0, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_temp_0) == 1):
            _coconut_match_temp_1 = _coconut_match_temp_0.get("b", _coconut_sentinel)
            if (_coconut_match_temp_1 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_1, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_temp_1) == 1):
                _coconut_match_temp_2 = _coconut_match_temp_1.get("c", _coconut_sentinel)
                if _coconut_match_temp_2 is not _coconut_sentinel:
                    x = _coconut_match_temp_2
                    _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to)
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'match {"a": {"b": x }} or {"a": {"b": {"c": x}}} = {"a": {"b": {"c": "x"}}}\'' " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'match {"a": {"b": x }} or {"a": {"b": {"c": x}}} = {"a": {"b": {"c": "x"}}}'
        _coconut_match_err.value = _coconut_match_to
        raise _coconut_match_err

    assert x == {"c": "x"}
    assert py_repr("x") == ("u'x'" if sys.version_info < (3,) else "'x'")
    def foo(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
                x = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def foo(x is int) = x'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'def foo(x is int) = x'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return x
    try:
        foo(["foo"] * 100000)
    except MatchError as err:
        assert len(repr(err)) < 1000
    _coconut_assert(True)
    try:
        _coconut_assert(False, "msg")
    except AssertionError as err:
        assert str(err) == "msg"
    else:
        assert False
    try:
        _coconut_assert([])
    except AssertionError as err:
        assert str(err) == "(assert) got falsey value []"
    else:
        assert False
    if _coconut_sys.version_info < (3,):
        from itertools import ifilterfalse as filterfalse
    else:
        from itertools import filterfalse
    if _coconut_sys.version_info < (3,):
        from itertools import izip_longest as zip_longest
    else:
        from itertools import zip_longest
    assert reversed(reiterable(range(10)))[-1] == 0
    assert count("derp", None)[10] == "derp"
    assert (list)(count("derp", None)[5:10]) == ["derp"] * 5
    assert count("derp", None)[5:] == count("derp", None)
    assert (list)(count("derp", None)[:5]) == ["derp"] * 5
    def f(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "b" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("b")
            a = _coconut_match_to_args[0]
            if not _coconut_match_to_kwargs:
                b = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def f(a, /, b) = a, b'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def f(a, /, b) = a, b'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return a, b
    assert f(1, 2) == (1, 2)
    assert f(1, b=2) == (1, 2)
    try:
        f(a=1, b=2)
    except MatchError:
        assert True
    else:
        assert False
    return True

def easter_egg_test():
    _sys = _coconut_sys
    num_mods_0 = len(_sys.modules)
    import imp as _coconut_imp
    for _coconut_base_path in _coconut_sys.path:
        for _coconut_dirpath, _coconut_dirnames, _coconut_filenames in _coconut.os.walk(_coconut_base_path):
            _coconut_paths_to_imp = []
            for _coconut_fname in _coconut_filenames:
                if _coconut.os.path.splitext(_coconut_fname)[-1] == "py":
                    _coconut_fpath = _coconut.os.path.join(_coconut_dirpath, _coconut_fname)
                    _coconut_paths_to_imp.append(_coconut_fpath)
            for _coconut_dname in _coconut_dirnames:
                _coconut_dpath = _coconut.os.path.join(_coconut_dirpath, _coconut_dname)
                if "__init__.py" in _coconut.os.listdir(_coconut_dpath):
                    _coconut_paths_to_imp.append(_coconut_dpath)
            for _coconut_imp_path in _coconut_paths_to_imp:
                _coconut_imp_name = _coconut.os.path.splitext(_coconut.os.path.basename(_coconut_imp_path))[0]
                descr = _coconut_imp.find_module(_coconut_imp_name, [_coconut.os.path.dirname(_coconut_imp_path)])
                try:
                    _coconut_imp.load_module(_coconut_imp_name, *descr)
                except:
                    pass
            _coconut_dirnames[:] = []
    for _coconut_n, _coconut_m in _coconut.tuple(_coconut_sys.modules.items()):
        _coconut.locals()[_coconut_n] = _coconut_m
    assert sys == _sys
    assert len(_sys.modules) > num_mods_0
    orig_name = __name__
    import imp as _coconut_imp
    for _coconut_base_path in _coconut_sys.path:
        for _coconut_dirpath, _coconut_dirnames, _coconut_filenames in _coconut.os.walk(_coconut_base_path):
            _coconut_paths_to_imp = []
            for _coconut_fname in _coconut_filenames:
                if _coconut.os.path.splitext(_coconut_fname)[-1] == "py":
                    _coconut_fpath = _coconut.os.path.join(_coconut_dirpath, _coconut_fname)
                    _coconut_paths_to_imp.append(_coconut_fpath)
            for _coconut_dname in _coconut_dirnames:
                _coconut_dpath = _coconut.os.path.join(_coconut_dirpath, _coconut_dname)
                if "__init__.py" in _coconut.os.listdir(_coconut_dpath):
                    _coconut_paths_to_imp.append(_coconut_dpath)
            for _coconut_imp_path in _coconut_paths_to_imp:
                _coconut_imp_name = _coconut.os.path.splitext(_coconut.os.path.basename(_coconut_imp_path))[0]
                descr = _coconut_imp.find_module(_coconut_imp_name, [_coconut.os.path.dirname(_coconut_imp_path)])
                try:
                    _coconut_imp.load_module(_coconut_imp_name, *descr)
                except:
                    pass
            _coconut_dirnames[:] = []
    for _coconut_m in _coconut.tuple(_coconut_sys.modules.values()):
        _coconut_d = _coconut.getattr(_coconut_m, "__dict__", None)
        if _coconut_d is not None:
            for _coconut_k, _coconut_v in _coconut_d.items():
                if not _coconut_k.startswith("_"):
                    _coconut.locals()[_coconut_k] = _coconut_v
    assert __name__ == orig_name
    assert locals()["byteorder"] == _sys.byteorder
    return True

@_coconut_tco
def tco_func():
    while True:
        try:
            _coconut_is_recursive = tco_func is _coconut_recursive_func_12
        except _coconut.NameError:
            _coconut_is_recursive = False
        if _coconut_is_recursive:
            continue
        else:
            return _coconut_tail_call(tco_func)


        return None
_coconut_recursive_func_12 = tco_func
def main(test_easter_eggs=False):
    """Asserts arguments and executes tests."""
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
    if "_coconut_tco" in globals() or "_coconut_tco" in locals():
        assert hasattr(tco_func, "_coconut_tco_func")
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
        if sys.version_info >= (3, 6):
            from .py36_test import py36_test
            assert py36_test()

    print(".", end="")
    from .target_sys_test import target_sys_test
    assert target_sys_test()  # type: ignore

    print(".", end="")  # ........
    from . import tutorial  # type: ignore

    if test_easter_eggs:
        print(".", end="")  # .........
        assert easter_egg_test()

    print("\n<success>")
