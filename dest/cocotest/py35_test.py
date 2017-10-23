#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe0c37f62

# Compiled with Coconut version 1.3.1 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

import asyncio

def py35_test():
    """Performs Python-3.5-specific tests."""
    async def async_map_0(args):
        return parallel_map(args[0], *args[1:])
    async def async_map_1(args):
        return parallel_map(args[0], *args[1:])
    async def async_map_2(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
            iters = _coconut.list(_coconut_match_to_args[0][1:])
            func = _coconut_match_to_args[0][0]
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'async def async_map_2([func] + iters) = parallel_map(func, *iters)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'async def async_map_2([func] + iters) = parallel_map(func, *iters)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return parallel_map(func, *iters)
    async def async_map_3(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
            iters = _coconut.list(_coconut_match_to_args[0][1:])
            func = _coconut_match_to_args[0][0]
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'async match def async_map_3([func] + iters) = parallel_map(func, *iters)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'async match def async_map_3([func] + iters) = parallel_map(func, *iters)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return parallel_map(func, *iters)
    async def async_map_4(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
            iters = _coconut.list(_coconut_match_to_args[0][1:])
            func = _coconut_match_to_args[0][0]
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'match async def async_map_4([func] + iters) = parallel_map(func, *iters)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'match async def async_map_4([func] + iters) = parallel_map(func, *iters)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return parallel_map(func, *iters)
    async def async_map_test():
        for async_map in (async_map_0, async_map_1, async_map_2, async_map_3, async_map_4):
            assert (tuple)((await ((async_map)((_coconut.functools.partial(pow, 2), range(5)))))) == (1, 2, 4, 8, 16)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(async_map_test())
    loop.close()
    try:
        2 @ 3
    except TypeError:
        assert True
    else:
        assert False
    assert (1, *(2, 3), 4) == (1, 2, 3, 4)
    assert {"a": 1, **{"b": 2}, "c": 3} == {"a": 1, "b": 2, "c": 3}
    assert (repr)(_coconut.operator.attrgetter("attr")) == "operator.attrgetter('attr')"
    assert (repr)(_coconut.operator.methodcaller("method", 1)) == "operator.methodcaller('method', 1)"
    assert (repr)(_coconut.functools.partial(pow, 1)) == "functools.partial(<built-in function pow>, 1)"
    assert (repr)(_coconut.operator.itemgetter(1)) == "operator.itemgetter(1)"
    return True
