#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x42cae892

# Compiled with Coconut version 1.1.1-post_dev [Brontosaurus]

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

def non_py26_test():
    """Tests for any non-py26 version."""
    def _coconut_lambda_0(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x):\n    y = x', vars)
        return vars["_coconut_lambda_func"]
    assert (list)((_coconut.functools.partial(map, _coconut_lambda_0(_coconut.locals())))(range(10))) == [None] * 10
    def _coconut_lambda_1(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x):\n    yield x', vars)
        return vars["_coconut_lambda_func"]
    assert (list)((_coconut.functools.partial(map, list))((_coconut.functools.partial(map, _coconut_lambda_1(_coconut.locals())))(range(5)))) == [[0], [1], [2], [3], [4]]
    def do_stuff(x): return True
    def _coconut_lambda_2(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x=3):\n    return do_stuff(x)', vars)
        return vars["_coconut_lambda_func"]
    assert (_coconut_lambda_2(_coconut.locals()))() is True
    def _coconut_lambda_3(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x=4):\n    do_stuff(x)\n    return x', vars)
        return vars["_coconut_lambda_func"]
    assert (_coconut_lambda_3(_coconut.locals()))() == 4
    def _coconut_lambda_4(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x=5):\n    do_stuff(x)', vars)
        return vars["_coconut_lambda_func"]
    assert (_coconut_lambda_4(_coconut.locals()))() is None
    def _coconut_lambda_5(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x=6):\n    do_stuff(x)\n    assert x', vars)
        return vars["_coconut_lambda_func"]
    (_coconut_lambda_5(_coconut.locals()))()
    def _coconut_lambda_6(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x=7):\n    do_stuff(x)\n    assert x\n    yield x', vars)
        return vars["_coconut_lambda_func"]
    assert (list)((_coconut_lambda_6(_coconut.locals()))()) == [7]
    def _coconut_lambda_7(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(_=None):\n    do_stuff(_)\n    assert _\n    return _', vars)
        return vars["_coconut_lambda_func"]
    assert (_coconut_lambda_7(_coconut.locals()))(8) == 8
    def _coconut_lambda_8(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x=9):\n    return x', vars)
        return vars["_coconut_lambda_func"]
    assert (_coconut_lambda_8(_coconut.locals()))() == 9
    def _coconut_lambda_9(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x=10):\n    do_stuff(x)\n    return x', vars)
        return vars["_coconut_lambda_func"]
    assert (_coconut_lambda_9(_coconut.locals()))() == 10
    def _coconut_lambda_1(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x):\n    yield x', vars)
        return vars["_coconut_lambda_func"]
    def _coconut_lambda_11(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(_=None):\n    def _coconut_lambda_1(closure):\n        vars = _coconut.globals().copy()\n        vars.update(closure)\n        exec(\'def _coconut_lambda_func(x):\\n    yield x\', vars)\n        return vars["_coconut_lambda_func"]\n    def _coconut_lambda_10(closure):\n        vars = _coconut.globals().copy()\n        vars.update(closure)\n        exec(\'def _coconut_lambda_func(_=None):\\n    return 11\', vars)\n        return vars["_coconut_lambda_func"]\n    return _coconut_lambda_10(_coconut.locals())', vars)
        return vars["_coconut_lambda_func"]
    assert (_coconut_lambda_11(_coconut.locals()))()() == 11
    def _coconut_lambda_1(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(x):\n    yield x', vars)
        return vars["_coconut_lambda_func"]
    def _coconut_lambda_12(closure):
        vars = _coconut.globals().copy()
        vars.update(closure)
        exec('def _coconut_lambda_func(_=None):\n    return x', vars)
        return vars["_coconut_lambda_func"]
    assert (list)((_coconut.functools.partial(map, lambda _=None: _()))(((_coconut_lambda_12(_coconut.locals())) for x in range(5)))) == [0, 1, 2, 3, 4]
