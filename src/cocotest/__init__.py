#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xf68cf3de

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

"""
Author: Evan Hubinger
License: Apache 2.0
Description: The Coconut test suite.
"""

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    import os as _coconut_os    
    py2_filter, py2_hex, py2_map, py2_oct, py2_zip, py2_open, py2_range, py2_int, py2_chr, py2_str, py2_print, py2_input, py2_raw_input = filter, hex, map, oct, zip, open, range, int, chr, str, print, input, raw_input
    _coconut_isinstance, _coconut_int, _coconut_long, _coconut_str, _coconut_bytearray, _coconut_print, _coconut_unicode, _coconut_raw_input, _coconut_xrange, _coconut_slice, _coconut_reversed = isinstance, int, long, str, bytearray, print, unicode, raw_input, xrange, slice, reversed
    chr, str = unichr, unicode
    from future_builtins import *
    from io import open
    class range(object):
        """Python 3 range."""
        def __init__(self, *args):
            self._xrange = _coconut_xrange(*args)
        def __iter__(self):
            return iter(self._xrange)
        def __reversed__(self):
            return _coconut_reversed(self._xrange)
        def __len__(self):
            return len(self._xrange)
        def _slice(self, index):
            start, stop, step = index.start, index.stop, index.step
            if start is None:
                start = 0
            elif start < 0:
                start += len(self._xrange)
            if stop is None:
                stop = len(self._xrange)
            elif stop is not None and stop < 0:
                stop += len(self._xrange)
            if step is None:
                step = 1
            for i in _coconut_xrange(start, stop, step):
                yield self._xrange[i]
        def __getitem__(self, index):
            if _coconut_isinstance(index, _coconut_slice):
                return self._slice(index)
            else:
                return self._xrange[index]
    class _coconut_metaint(type):
        def __instancecheck__(cls, inst):
            return _coconut_isinstance(inst, (_coconut_int, _coconut_long))
    class int(_coconut_int):
        """Python 3 int."""
        __metaclass__ = _coconut_metaint
        __slots__ = ()
    class _coconut_metabytes(type):
        def __instancecheck__(cls, inst):
            return _coconut_isinstance(inst, _coconut_str)
    class bytes(_coconut_str):
        """Python 3 bytes."""
        __metaclass__ = _coconut_metabytes
        __slots__ = ()
        def __new__(cls, *args, **kwargs):
            return _coconut_str.__new__(cls, _coconut_bytearray(*args, **kwargs))
    def print(*args, **kwargs):
        """Python 3 print."""
        return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
    def input(*args, **kwargs):
        """Python 3 input."""
        return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
    def raw_input(*args):
        """Raises NameError."""
        raise NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')

import os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
import __coconut__
_coconut_sys.path.remove(_coconut_file_path)

__coconut_version__ = __coconut__.version
map = __coconut__.imap
zip = __coconut__.izip
reduce = __coconut__.functools.reduce
takewhile = __coconut__.itertools.takewhile
dropwhile = __coconut__.itertools.dropwhile
tee = __coconut__.itertools.tee
count = __coconut__.itertools.count
recursive = __coconut__.recursive
datamaker = __coconut__.datamaker
consume = __coconut__.consume
MatchError = __coconut__.MatchError

# Compiled Coconut: ------------------------------------------------------------
