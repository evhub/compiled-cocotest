#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0xd41a209b

# Compiled with Coconut version 1.0.0-post_dev [Albatross]

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

def main(doc):
    """Executes Tests."""
    assert doc
    from .suite import main_test
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
