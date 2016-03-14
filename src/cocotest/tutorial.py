#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __coconut_hash__ = 0x7c602a76

# Compiled with Coconut version 0.3.6-post_dev [Odisha]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
if _coconut_sys.version_info < (3,):
    from __coconut__ import py2_filter, py2_hex, py2_map, py2_oct, py2_zip, py2_open, py2_range, py2_xrange, py2_int, py2_chr, py2_str, py2_print, py2_input, py2_raw_input, ascii, filter, hex, oct, open, range, int, chr, str, print, input, bytes, raw_input, xrange
from __coconut__ import __coconut__, __coconut_version__, map, zip, reduce, takewhile, dropwhile, tee, count, recursive, datamaker, consume, MatchError
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------------

def factorial(n):
    """Compute n! where n is an integer >= 0."""
    if (isinstance)(n, int) and n >= 0:
        acc = 1
        for x in range(1, n + 1):
            acc *= x
        return acc
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except (TypeError):
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except (TypeError):
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

def factorial(n):
    """Compute n! where n is an integer >= 0."""
    _coconut_match_check = False
    _coconut_match_to = n
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    if not _coconut_match_check:
        _coconut_match_to = n
        if (__coconut__.isinstance(_coconut_match_to, int)):
            if (n > 0):
                _coconut_match_check = True
        if _coconut_match_check:
            return n * factorial(n - 1)
    if not _coconut_match_check:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except (TypeError):
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except (TypeError):
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

def factorial(n):
    """Compute n! where n is an integer >= 0."""
    try:
        _coconut_match_check = False
        _coconut_match_to = n
        if (_coconut_match_to == 0):
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for '0 = n  # destructuring assignment' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'0 = n  # destructuring assignment'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
    except (MatchError):
        try:
            _coconut_match_check = False
            _coconut_match_to = n
            if (__coconut__.isinstance(_coconut_match_to, int)):
                _coconut_match_check = True
            if not _coconut_match_check:
                _coconut_match_err = __coconut__.MatchError("pattern-matching failed for '_ is int = n  # also destructuring assignment' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
                _coconut_match_err.pattern = "'_ is int = n  # also destructuring assignment'"
                _coconut_match_err.value = _coconut_match_to
                raise _coconut_match_err
        except (MatchError):
            pass
        else:
            if n > 0: # in Coconut, if, match, and try are allowed after else
                return n * factorial(n - 1)
    else:
        return 1
    raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except (TypeError):
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except (TypeError):
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

@recursive
def factorial(n, acc=1):
    """Compute n! where n is an integer >= 0."""
    _coconut_match_check = False
    _coconut_match_to = n
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return acc
    if not _coconut_match_check:
        _coconut_match_to = n
        if (__coconut__.isinstance(_coconut_match_to, int)):
            if (n > 0):
                _coconut_match_check = True
        if _coconut_match_check:
            return factorial(n - 1, acc * n)
    if not _coconut_match_check:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except (TypeError):
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except (TypeError):
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

def factorial(n):
    """Compute n! where n is an integer >= 0."""
    _coconut_match_check = False
    _coconut_match_to = n
    if (_coconut_match_to == 0):
        _coconut_match_check = True
    if _coconut_match_check:
        return 1
    if not _coconut_match_check:
        _coconut_match_to = n
        if (__coconut__.isinstance(_coconut_match_to, int)):
            if (n > 0):
                _coconut_match_check = True
        if _coconut_match_check:
            return (__coconut__.functools.partial(reduce, __coconut__.operator.__mul__))(range(1, n + 1))
    if not _coconut_match_check:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except (TypeError):
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except (TypeError):
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

def quick_sort(l):
    """Return a sorted iterator of l, using the quick sort algorithm, and without using any data until necessary."""
    _coconut_match_check = False
    _coconut_match_to = l
    if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Iterable)):
        tail = __coconut__.iter(_coconut_match_to)
        _coconut_match_iter_0 = __coconut__.tuple(__coconut__.igetitem(tail, __coconut__.slice(None, 1)))
        if (__coconut__.len(_coconut_match_iter_0) == 1):
            head = _coconut_match_iter_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        tail, tail_ = tee(tail)
        _coconut_yield_from = (__coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: quick_sort((x for x in tail if x <= head)), lambda: (head,), lambda: quick_sort((x for x in tail_ if x > head))))))
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


# Test cases:
assert (list)((quick_sort)([])) == []
assert (list)((quick_sort)([3])) == [3]
assert (list)((quick_sort)([0, 1, 2, 3, 4])) == [0, 1, 2, 3, 4]
assert (list)((quick_sort)([4, 3, 2, 1, 0])) == [0, 1, 2, 3, 4]
assert (list)((quick_sort)([3, 0, 4, 2, 1])) == [0, 1, 2, 3, 4]

class vector2(__coconut__.collections.namedtuple("vector2", "x, y")):
    """Immutable 2-vector."""
    __slots__ = ()
    def __abs__(self):
        """Return the magnitude of the 2-vector."""
        return (self.x**2 + self.y**2)**0.5

# Test cases:
assert (repr)(vector2(1, 2)) == "vector2(x=1, y=2)"
assert (abs)(vector2(3, 4)) == 5
v = vector2(2, 3)
try:
    v.x = 7
except (AttributeError):
    assert True
else:
    assert False

class vector(__coconut__.collections.namedtuple("vector", "pts")):
    """Immutable n-vector."""
    __slots__ = ()
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and (isinstance)(pts[0], vector):
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return (datamaker(cls))((tuple)(pts)) # accesses base constructor

# Test cases:
assert (repr)(vector(1, 2, 3)) == "vector(pts=(1, 2, 3))"
assert (repr)((vector)(vector(4, 5))) == "vector(pts=(4, 5))"

class vector(__coconut__.collections.namedtuple("vector", "pts")):
    """Immutable n-vector."""
    __slots__ = ()
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and (isinstance)(pts[0], vector):
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return (datamaker(cls))((tuple)(pts)) # accesses base constructor
    def __abs__(self):
        """Return the magnitude of the vector."""
        return ((lambda s: s**0.5))((sum)((__coconut__.functools.partial(map, lambda x: x**2))(self.pts)))
    def __add__(self, other):
        """Add two vectors together."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for 'vector(other_pts) = other' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'vector(other_pts) = other'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        assert len(other_pts) == len(self.pts)
        return (vector)(*map(__coconut__.operator.__add__, self.pts, other_pts))
    def __sub__(self, other):
        """Subtract one vector from another."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for 'vector(other_pts) = other' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'vector(other_pts) = other'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        assert len(other_pts) == len(self.pts)
        return (vector)(*map((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), self.pts, other_pts))
    def __neg__(self):
        """Retrieve the negative of the vector."""
        return (vector)(*(__coconut__.functools.partial(map, (lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args))))(self.pts))
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1) and (_coconut_match_to[0] == self.pts):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            assert len(other_pts) == len(self.pts)
            return (sum)(map(__coconut__.operator.__mul__, self.pts, other_pts)) # dot product
        else:
            return (vector)(*(__coconut__.functools.partial(map, __coconut__.functools.partial(__coconut__.operator.__mul__, other)))(self.pts)) # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other

# Test cases:
assert (repr)(vector(1, 2, 3)) == "vector(pts=(1, 2, 3))"
assert (repr)((vector)(vector(4, 5))) == "vector(pts=(4, 5))"
assert (abs)(vector(3, 4)) == 5
assert (repr)(vector(1, 2) + vector(2, 3)) == "vector(pts=(3, 5))"
assert (repr)(vector(2, 2) - vector(0, 1)) == "vector(pts=(2, 1))"
assert (repr)(-vector(1, 3)) == "vector(pts=(-1, -3))"
assert (vector(1, 2) == "string") is False
assert (vector(1, 2) == vector(3, 4)) is False
assert (vector(2, 4) == vector(2, 4)) is True
assert (repr)(2 * vector(1, 2)) == "vector(pts=(2, 4))"
assert vector(1, 2) * vector(1, 3) == 7

def diagonal_line(n): return (__coconut__.functools.partial(map, lambda i: (i, n - i)))(range(n + 1))

assert (isinstance)(diagonal_line(0), (list, tuple)) is False
assert (list)(diagonal_line(0)) == [(0, 0)]
assert (list)(diagonal_line(1)) == [(0, 1), (1, 0)]

def linearized_plane(n=0): return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: diagonal_line(n), lambda: linearized_plane(n + 1))))

# Note: these tests use $[] notation, which we haven't introduced yet
#  but will introduce later in this case study; for now, just run the
#  tests, and make sure you get the same result as is in the comment
assert __coconut__.igetitem(linearized_plane(), 0) == (0, 0)
assert (list)(__coconut__.igetitem(linearized_plane(), __coconut__.slice(None, 3))) == [(0, 0), (0, 1), (1, 0)]

def vector_field(): return (__coconut__.functools.partial(map, lambda xy: vector(*xy)))(linearized_plane())

# You'll need to bring in the vector class from earlier to make these work
assert (repr)(__coconut__.igetitem(vector_field(), 0)) == "vector(pts=(0, 0))"
assert (repr)((list)(__coconut__.igetitem(vector_field(), __coconut__.slice(2, 3)))) == "[vector(pts=(1, 0))]"

class vector(__coconut__.collections.namedtuple("vector", "pts")):
    """Immutable n-vector."""
    __slots__ = ()
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and (isinstance)(pts[0], vector):
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return (datamaker(cls))((tuple)(pts)) # accesses base constructor
    def __abs__(self):
        """Return the magnitude of the vector."""
        return ((lambda s: s**0.5))((sum)((__coconut__.functools.partial(map, lambda x: x**2))(self.pts)))
    def __add__(self, other):
        """Add two vectors together."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for 'vector(other_pts) = other' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'vector(other_pts) = other'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        assert len(other_pts) == len(self.pts)
        return (vector)(*map(__coconut__.operator.__add__, self.pts, other_pts))
    def __sub__(self, other):
        """Subtract one vector from another."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for 'vector(other_pts) = other' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'vector(other_pts) = other'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        assert len(other_pts) == len(self.pts)
        return (vector)(*map((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), self.pts, other_pts))
    def __neg__(self):
        """Retrieve the negative of the vector."""
        return (vector)(*(__coconut__.functools.partial(map, (lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args))))(self.pts))
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1) and (_coconut_match_to[0] == self.pts):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            assert len(other_pts) == len(self.pts)
            return (sum)(map(__coconut__.operator.__mul__, self.pts, other_pts)) # dot product
        else:
            return (vector)(*(__coconut__.functools.partial(map, __coconut__.functools.partial(__coconut__.operator.__mul__, other)))(self.pts)) # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other

def diagonal_line(n): return (__coconut__.functools.partial(map, lambda i: (i, n - i)))(range(n + 1))
def linearized_plane(n=0): return __coconut__.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: diagonal_line(n), lambda: linearized_plane(n + 1))))
def vector_field(): return (__coconut__.functools.partial(map, lambda xy: vector(*xy)))(linearized_plane())

# Test cases:
assert (isinstance)(diagonal_line(0), (list, tuple)) is False
assert (list)(diagonal_line(0)) == [(0, 0)]
assert (list)(diagonal_line(1)) == [(0, 1), (1, 0)]
assert __coconut__.igetitem(linearized_plane(), 0) == (0, 0)
assert (list)(__coconut__.igetitem(linearized_plane(), __coconut__.slice(None, 3))) == [(0, 0), (0, 1), (1, 0)]
assert (repr)(__coconut__.igetitem(vector_field(), 0)) == "vector(pts=(0, 0))"
assert (repr)((list)(__coconut__.igetitem(vector_field(), __coconut__.slice(2, 3)))) == "[vector(pts=(1, 0))]"

import math # necessary for math.acos in .angle

class vector(__coconut__.collections.namedtuple("vector", "pts")):
    """Immutable n-vector."""
    __slots__ = ()
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and (isinstance)(pts[0], vector):
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return (datamaker(cls))((tuple)(pts)) # accesses base constructor
    def __abs__(self):
        """Return the magnitude of the vector."""
        return ((lambda s: s**0.5))((sum)((__coconut__.functools.partial(map, lambda x: x**2))(self.pts)))
    def __add__(self, other):
        """Add two vectors together."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for 'vector(other_pts) = other' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'vector(other_pts) = other'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        assert len(other_pts) == len(self.pts)
        return (vector)(*map(__coconut__.operator.__add__, self.pts, other_pts))
    def __sub__(self, other):
        """Subtract one vector from another."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for 'vector(other_pts) = other' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'vector(other_pts) = other'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        assert len(other_pts) == len(self.pts)
        return (vector)(*map((lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args)), self.pts, other_pts))
    def __neg__(self):
        """Retrieve the negative of the vector."""
        return (vector)(*(__coconut__.functools.partial(map, (lambda *args: __coconut__.operator.__neg__(*args) if len(args) < 2 else __coconut__.operator.__sub__(*args))))(self.pts))
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1) and (_coconut_match_to[0] == self.pts):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (__coconut__.isinstance(_coconut_match_to, vector)) and (__coconut__.len(_coconut_match_to) == 1):
            other_pts = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            assert len(other_pts) == len(self.pts)
            return (sum)(map(__coconut__.operator.__mul__, self.pts, other_pts)) # dot product
        else:
            return (vector)(*(__coconut__.functools.partial(map, __coconut__.functools.partial(__coconut__.operator.__mul__, other)))(self.pts)) # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other
# New one-line functions necessary for finding the angle between vectors:
    def __truediv__(self, other): return (vector)(*(__coconut__.functools.partial(map, lambda x: x / other))(self.pts))
    def unit(self): return self / abs(self)
    def angle (*_coconut_match_to):
        _coconut_match_check = False
        if (__coconut__.isinstance(_coconut_match_to, __coconut__.abc.Sequence)) and (__coconut__.len(_coconut_match_to) == 2) and (__coconut__.isinstance(_coconut_match_to[1], vector)):
            self = _coconut_match_to[0]
            other = _coconut_match_to[1]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = __coconut__.MatchError("pattern-matching failed for 'def angle(self, other is vector) = math.acos(self.unit() * other.unit())' in " + __coconut__.ascii(__coconut__.ascii(_coconut_match_to)))
            _coconut_match_err.pattern = "'def angle(self, other is vector) = math.acos(self.unit() * other.unit())'"
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
        return math.acos(self.unit() * other.unit())


# Test cases:
assert (repr)(vector(3, 4) / 1) == "vector(pts=(3.0, 4.0))"
assert (repr)(vector(2, 4) / 2) == "vector(pts=(1.0, 2.0))"
assert (repr)(vector(0, 1).unit()) == "vector(pts=(0.0, 1.0))"
assert (repr)(vector(5, 0).unit()) == "vector(pts=(1.0, 0.0))"
assert vector(2, 0).angle(vector(3, 0)) == 0.0
assert vector(1, 0).angle(vector(0, 2)) == math.pi / 2
try:
    vector(1, 2).angle(5)
except (MatchError):
    assert True
else:
    assert False
