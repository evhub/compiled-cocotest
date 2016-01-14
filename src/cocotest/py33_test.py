#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xd38929bc

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

def py33_test():
    """Performs Python-3.3-specific tests."""
    def chain2(a, b):
        yield from a
        yield from b
    assert (list)(chain2((_coconut_lazy_item() for _coconut_lazy_item in (lambda: 1, lambda: 2)), (_coconut_lazy_item() for _coconut_lazy_item in (lambda: 3, lambda: 4)))) == [1, 2, 3, 4]
