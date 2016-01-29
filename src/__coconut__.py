#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

"""Built-in Coconut functions."""

# Coconut Header: --------------------------------------------------------------

version = "0.3.6-post_dev"

import imp, functools, operator, itertools, collections
try:
    import collections.abc as abc
except ImportError:
    abc = collections

object, int, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii = object, int, set, frozenset, tuple, list, slice, len, iter, isinstance, getattr, ascii

def recursive(func):
    """Returns tail-call-optimized function."""
    state = [True, None] # toplevel, (args, kwargs)
    recurse = object()
    @functools.wraps(func)
    def tailed_func(*args, **kwargs):
        """Tail Recursion Wrapper."""
        if state[0]:
            state[0] = False
            try:
                while True:
                    result = func(*args, **kwargs)
                    if result is recurse:
                        args, kwargs = state[1]
                        state[1] = None
                    else:
                        return result
            finally:
                state[0] = True
        else:
            state[1] = args, kwargs
            return recurse
    return tailed_func

def datamaker(data_type):
    """Returns base data constructor of data_type."""
    return functools.partial(super(data_type, data_type).__new__, data_type)

def consume(iterable, keep_last=0):
    """Fully exhaust iterable and return the last keep_last elements."""
    return collections.deque(iterable, maxlen=keep_last)

class MatchError(Exception):
    """Pattern-matching error."""
