#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x6c447b6a

# Compiled with Coconut version 1.2.3-post_dev2 [Colonel]

# Coconut Header: --------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
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
except TypeError:
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except TypeError:
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
        if (_coconut.isinstance(_coconut_match_to, int)):
            _coconut_match_check = True
        if _coconut_match_check and not (n > 0):
            _coconut_match_check = False
        if _coconut_match_check:
            return n * factorial(n - 1)
    if not _coconut_match_check:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except TypeError:
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except TypeError:
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
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'0 = n   # destructuring assignment'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = '0 = n   # destructuring assignment'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err
# destructuring assignment
    except MatchError:
        try:
            _coconut_match_check = False
            _coconut_match_to = n
            if (_coconut.isinstance(_coconut_match_to, int)):
                _coconut_match_check = True
            if not _coconut_match_check:
                _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'_ is int = n   # also destructuring assignment'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
                _coconut_match_err.pattern = '_ is int = n   # also destructuring assignment'
                _coconut_match_err.value = _coconut_match_to
                raise _coconut_match_err
# also destructuring assignment
        except MatchError:
            pass
        else:
            if n > 0:  # in Coconut, if, match, and try are allowed after else
                return n * factorial(n - 1)
    else:
        return 1
    raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except TypeError:
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except TypeError:
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

@_coconut_tco
def factorial(n, acc=1):
    def _coconut_mock_func(n, acc=1): return n, acc
    while True:
        """Compute n! where n is an integer >= 0."""
        _coconut_match_check = False
        _coconut_match_to = n
        if (_coconut_match_to == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return acc
        if not _coconut_match_check:
            _coconut_match_to = n
            if (_coconut.isinstance(_coconut_match_to, int)):
                _coconut_match_check = True
            if _coconut_match_check and not (n > 0):
                _coconut_match_check = False
            if _coconut_match_check:
                if factorial is _coconut_recursive_func_3:
                    n, acc = _coconut_mock_func(n - 1, acc * n)
                    continue
                else:
                    raise _coconut_tail_call(factorial, n - 1, acc * n)

        if not _coconut_match_check:
            raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
        return None
_coconut_recursive_func_3 = factorial
try:
    (factorial)(-1)
except TypeError:
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except TypeError:
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

@_coconut_tco
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
        if (_coconut.isinstance(_coconut_match_to, int)):
            _coconut_match_check = True
        if _coconut_match_check and not (n > 0):
            _coconut_match_check = False
        if _coconut_match_check:
            raise _coconut_tail_call(reduce, _coconut.operator.mul, range(1, n + 1))
    if not _coconut_match_check:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
try:
    (factorial)(-1)
except TypeError:
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except TypeError:
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

def factorial(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def factorial(0) = 1'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def factorial(0) = 1'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return 1

@addpattern(factorial)
@_coconut_tco
def factorial(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            n = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check and not (n > 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def factorial(n is int if n > 0) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def factorial(n is int if n > 0) ='
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    """Compute n! where n is an integer >= 0."""
    raise _coconut_tail_call(reduce, _coconut.operator.mul, range(1, n + 1))

# Test cases:
try:
    (factorial)(-1)
except MatchError:
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except MatchError:
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

def factorial(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def factorial(0) = 1'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def factorial(0) = 1'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return 1

@addpattern(factorial)
def factorial(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "n" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("n")
        if (_coconut.isinstance(_coconut_match_temp_0, int)) and (not _coconut_match_to_kwargs):
            n = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check and not (n > 0):
        _coconut_match_check = False
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def factorial(n is int if n > 0) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def factorial(n is int if n > 0) ='
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    """Compute n! where n is an integer >= 0."""
    return n * factorial(n - 1)

# Test cases:
try:
    (factorial)(-1)
except MatchError:
    assert True
else:
    assert False
try:
    (factorial)(0.5)
except MatchError:
    assert True
else:
    assert False
assert (factorial)(0) == 1
assert (factorial)(3) == 6

def quick_sort(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 0):
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def quick_sort([]) = []'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def quick_sort([]) = []'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return []

@addpattern(quick_sort)
def quick_sort(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
        tail = _coconut.list(_coconut_match_to_args[0][1:])
        head = _coconut_match_to_args[0][0]
        if (not _coconut_match_to_kwargs):
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def quick_sort([head] + tail) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def quick_sort([head] + tail) ='
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    """Sort the input sequence using the quick sort algorithm."""
    return (quick_sort([x for x in tail if x < head]) + [head] + quick_sort([x for x in tail if x >= head]))

# Test cases:
assert (quick_sort)([]) == []
assert (quick_sort)([3]) == [3]
assert (quick_sort)([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]
assert (quick_sort)([4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4]
assert (quick_sort)([3, 0, 4, 2, 1]) == [0, 1, 2, 3, 4]

def quick_sort(l):
    """Sort the input iterator, using the quick sort algorithm, and without using any data until necessary."""
    _coconut_match_check = False
    _coconut_match_to = l
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Iterable)):
        tail = _coconut.iter(_coconut_match_to)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1):
            head = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if _coconut_match_check:
        tail, tail_ = tee(tail)
        _coconut_yield_from = (_coconut.itertools.chain.from_iterable((_coconut_lazy_item() for _coconut_lazy_item in (lambda: quick_sort((x for x in tail if x < head)), lambda: (head,), lambda: quick_sort((x for x in tail_ if x >= head))))))
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


# Test cases:
assert (list)((quick_sort)([])) == []
assert (list)((quick_sort)([3])) == [3]
assert (list)((quick_sort)([0, 1, 2, 3, 4])) == [0, 1, 2, 3, 4]
assert (list)((quick_sort)([4, 3, 2, 1, 0])) == [0, 1, 2, 3, 4]
assert (list)((quick_sort)([3, 0, 4, 2, 1])) == [0, 1, 2, 3, 4]

class vector2(_coconut.collections.namedtuple("vector2", "x y"), _coconut.object):
    """Immutable 2-vector."""
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __abs__(self):
        """Return the magnitude of the 2-vector."""
        return (self.x**2 + self.y**2)**0.5

# Test cases:
assert (str)(vector2(1, 2)) == "vector2(x=1, y=2)"
assert (abs)(vector2(3, 4)) == 5
(str)((_coconut.functools.partial(fmap, lambda x: x * 2))(vector2(1, 2))) == "vector2(x=2, y=4)"
v = vector2(2, 3)
try:
    v.x = 7
except AttributeError:
    assert True
else:
    assert False

class vector(_coconut.collections.namedtuple("vector", "pts"), _coconut.object):
    """Immutable n-vector."""
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __new__(_cls, *pts):
        return _coconut.tuple.__new__(_cls, pts)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=None):
        return new(cls, iterable)
    def _asdict(self):
        return _coconut.OrderedDict([("pts", self[:])])
    def __repr__(self):
        return "vector(*pts=%r)" % (self[:],)
    def _replace(_self, **kwds):
        result = self._make(kwds.pop("pts", _self))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: %r" % kwds.keys())
        return result
    @_coconut.property
    def pts(self):
        return self[:]
    @_coconut_tco
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        _coconut_match_check = False
        _coconut_match_to = pts
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1) and (_coconut.isinstance(_coconut_match_to[0], vector)):
            v = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return v  # vector(v) where v is a vector should return v
        else:
            raise _coconut_tail_call((datamaker(cls)), *pts)  # accesses base constructor

# Test cases:
assert (str)(vector(1, 2, 3)) == "vector(*pts=(1, 2, 3))"
assert (str)((vector)(vector(4, 5))) == "vector(*pts=(4, 5))"

class vector(_coconut.collections.namedtuple("vector", "pts"), _coconut.object):
    """Immutable n-vector."""
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __new__(_cls, *pts):
        return _coconut.tuple.__new__(_cls, pts)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=None):
        return new(cls, iterable)
    def _asdict(self):
        return _coconut.OrderedDict([("pts", self[:])])
    def __repr__(self):
        return "vector(*pts=%r)" % (self[:],)
    def _replace(_self, **kwds):
        result = self._make(kwds.pop("pts", _self))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: %r" % kwds.keys())
        return result
    @_coconut.property
    def pts(self):
        return self[:]
    @_coconut_tco
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        _coconut_match_check = False
        _coconut_match_to = pts
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1) and (_coconut.isinstance(_coconut_match_to[0], vector)):
            v = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return v  # vector(v) where v is a vector should return v
        else:
            raise _coconut_tail_call((datamaker(cls)), *pts)  # accesses base constructor
    @_coconut_tco
    def __abs__(self):
        """Return the magnitude of the vector."""
        raise _coconut_tail_call((_coconut_partial(pow, {1: 0.5}, 2)), (sum)((_coconut.functools.partial(map, _coconut_partial(pow, {1: 2}, 2)))(self.pts)))
    @_coconut_tco
    def __add__(self, other):
        """Add two vectors together."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'vector(*other_pts) = other'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'vector(*other_pts) = other'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert len(other_pts) == len(self.pts)
        raise _coconut_tail_call((vector), *map(_coconut.operator.add, self.pts, other_pts))
    @_coconut_tco
    def __sub__(self, other):
        """Subtract one vector from another."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'vector(*other_pts) = other'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'vector(*other_pts) = other'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert len(other_pts) == len(self.pts)
        raise _coconut_tail_call((vector), *map(_coconut_minus, self.pts, other_pts))
    @_coconut_tco
    def __neg__(self):
        """Retrieve the negative of the vector."""
        raise _coconut_tail_call((vector), *(_coconut.functools.partial(map, _coconut_minus))(self.pts))
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut_match_to[0:] == self.pts):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
    @_coconut_tco
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if _coconut_match_check:
            assert len(other_pts) == len(self.pts)
            raise _coconut_tail_call((sum), map(_coconut.operator.mul, self.pts, other_pts))  # dot product
        else:
            raise _coconut_tail_call((vector), *(_coconut.functools.partial(map, _coconut.functools.partial(_coconut.operator.mul, other)))(self.pts))  # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other

# Test cases:
assert (str)(vector(1, 2, 3)) == "vector(*pts=(1, 2, 3))"
assert (str)((vector)(vector(4, 5))) == "vector(*pts=(4, 5))"
assert (abs)(vector(3, 4)) == 5
assert (str)(vector(1, 2) + vector(2, 3)) == "vector(*pts=(3, 5))"
assert (str)(vector(2, 2) - vector(0, 1)) == "vector(*pts=(2, 1))"
assert (str)(-vector(1, 3)) == "vector(*pts=(-1, -3))"
assert (vector(1, 2) == "string") is False
assert (vector(1, 2) == vector(3, 4)) is False
assert (vector(2, 4) == vector(2, 4)) is True
assert (str)(2 * vector(1, 2)) == "vector(*pts=(2, 4))"
assert vector(1, 2) * vector(1, 3) == 7

@_coconut_tco
def diagonal_line(n):
    raise _coconut_tail_call((_coconut.functools.partial(map, lambda i: (i, n - i))), range(n + 1))

assert (isinstance)(diagonal_line(0), (list, tuple)) is False
assert (list)(diagonal_line(0)) == [(0, 0)]
assert (list)(diagonal_line(1)) == [(0, 1), (1, 0)]

@_coconut_tco
def linearized_plane(n=0):
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: diagonal_line(n), lambda: linearized_plane(n + 1))))

# Note: these tests use $[] notation, which we haven't introduced yet
#  but will introduce later in this case study; for now, just run the
#  tests, and make sure you get the same result as is in the comment
assert _coconut_igetitem(linearized_plane(), 0) == (0, 0)
assert (list)(_coconut_igetitem(linearized_plane(), _coconut.slice(None, 3))) == [(0, 0), (0, 1), (1, 0)]

@_coconut_tco
def vector_field():
    raise _coconut_tail_call((_coconut.functools.partial(map, lambda xy: vector(*xy))), linearized_plane())

# You'll need to bring in the vector class from earlier to make these work
assert (str)(_coconut_igetitem(vector_field(), 0)) == "vector(*pts=(0, 0))"
assert (str)((list)(_coconut_igetitem(vector_field(), _coconut.slice(2, 3)))) == "[vector(*pts=(1, 0))]"

class vector(_coconut.collections.namedtuple("vector", "pts"), _coconut.object):
    """Immutable n-vector."""
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __new__(_cls, *pts):
        return _coconut.tuple.__new__(_cls, pts)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=None):
        return new(cls, iterable)
    def _asdict(self):
        return _coconut.OrderedDict([("pts", self[:])])
    def __repr__(self):
        return "vector(*pts=%r)" % (self[:],)
    def _replace(_self, **kwds):
        result = self._make(kwds.pop("pts", _self))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: %r" % kwds.keys())
        return result
    @_coconut.property
    def pts(self):
        return self[:]
    @_coconut_tco
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        _coconut_match_check = False
        _coconut_match_to = pts
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1) and (_coconut.isinstance(_coconut_match_to[0], vector)):
            v = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return v  # vector(v) where v is a vector should return v
        else:
            raise _coconut_tail_call((datamaker(cls)), *pts)  # accesses base constructor
    @_coconut_tco
    def __abs__(self):
        """Return the magnitude of the vector."""
        raise _coconut_tail_call((_coconut_partial(pow, {1: 0.5}, 2)), (sum)((_coconut.functools.partial(map, _coconut_partial(pow, {1: 2}, 2)))(self.pts)))
    @_coconut_tco
    def __add__(self, other):
        """Add two vectors together."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'vector(*other_pts) = other'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'vector(*other_pts) = other'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert len(other_pts) == len(self.pts)
        raise _coconut_tail_call((vector), *map(_coconut.operator.add, self.pts, other_pts))
    @_coconut_tco
    def __sub__(self, other):
        """Subtract one vector from another."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'vector(*other_pts) = other'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'vector(*other_pts) = other'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert len(other_pts) == len(self.pts)
        raise _coconut_tail_call((vector), *map(_coconut_minus, self.pts, other_pts))
    @_coconut_tco
    def __neg__(self):
        """Retrieve the negative of the vector."""
        raise _coconut_tail_call((vector), *(_coconut.functools.partial(map, _coconut_minus))(self.pts))
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut_match_to[0:] == self.pts):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
    @_coconut_tco
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if _coconut_match_check:
            assert len(other_pts) == len(self.pts)
            raise _coconut_tail_call((sum), map(_coconut.operator.mul, self.pts, other_pts))  # dot product
        else:
            raise _coconut_tail_call((vector), *(_coconut.functools.partial(map, _coconut.functools.partial(_coconut.operator.mul, other)))(self.pts))  # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other

@_coconut_tco
def diagonal_line(n):
    raise _coconut_tail_call((_coconut.functools.partial(map, lambda i: (i, n - i))), range(n + 1))
@_coconut_tco
def linearized_plane(n=0):
    raise _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_lazy_item() for _coconut_lazy_item in (lambda: diagonal_line(n), lambda: linearized_plane(n + 1))))
@_coconut_tco
def vector_field():
    raise _coconut_tail_call((_coconut.functools.partial(map, lambda xy: vector(*xy))), linearized_plane())

# Test cases:
assert (isinstance)(diagonal_line(0), (list, tuple)) is False
assert (list)(diagonal_line(0)) == [(0, 0)]
assert (list)(diagonal_line(1)) == [(0, 1), (1, 0)]
assert _coconut_igetitem(linearized_plane(), 0) == (0, 0)
assert (list)(_coconut_igetitem(linearized_plane(), _coconut.slice(None, 3))) == [(0, 0), (0, 1), (1, 0)]
assert (str)(_coconut_igetitem(vector_field(), 0)) == "vector(*pts=(0, 0))"
assert (str)((list)(_coconut_igetitem(vector_field(), _coconut.slice(2, 3)))) == "[vector(*pts=(1, 0))]"

import math  # necessary for math.acos in .angle

class vector(_coconut.collections.namedtuple("vector", "pts"), _coconut.object):
    """Immutable n-vector."""
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __new__(_cls, *pts):
        return _coconut.tuple.__new__(_cls, pts)
    @_coconut.classmethod
    def _make(cls, iterable, new=_coconut.tuple.__new__, len=None):
        return new(cls, iterable)
    def _asdict(self):
        return _coconut.OrderedDict([("pts", self[:])])
    def __repr__(self):
        return "vector(*pts=%r)" % (self[:],)
    def _replace(_self, **kwds):
        result = self._make(kwds.pop("pts", _self))
        if kwds:
            raise _coconut.ValueError("Got unexpected field names: %r" % kwds.keys())
        return result
    @_coconut.property
    def pts(self):
        return self[:]
    @_coconut_tco
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        _coconut_match_check = False
        _coconut_match_to = pts
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1) and (_coconut.isinstance(_coconut_match_to[0], vector)):
            v = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return v  # vector(v) where v is a vector should return v
        else:
            raise _coconut_tail_call((datamaker(cls)), *pts)  # accesses base constructor
    @_coconut_tco
    def __abs__(self):
        """Return the magnitude of the vector."""
        raise _coconut_tail_call((_coconut_partial(pow, {1: 0.5}, 2)), (sum)((_coconut.functools.partial(map, _coconut_partial(pow, {1: 2}, 2)))(self.pts)))
    @_coconut_tco
    def __add__(self, other):
        """Add two vectors together."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'vector(*other_pts) = other'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'vector(*other_pts) = other'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert len(other_pts) == len(self.pts)
        raise _coconut_tail_call((vector), *map(_coconut.operator.add, self.pts, other_pts))
    @_coconut_tco
    def __sub__(self, other):
        """Subtract one vector from another."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'vector(*other_pts) = other'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
            _coconut_match_err.pattern = 'vector(*other_pts) = other'
            _coconut_match_err.value = _coconut_match_to
            raise _coconut_match_err

        assert len(other_pts) == len(self.pts)
        raise _coconut_tail_call((vector), *map(_coconut_minus, self.pts, other_pts))
    @_coconut_tco
    def __neg__(self):
        """Retrieve the negative of the vector."""
        raise _coconut_tail_call((vector), *(_coconut.functools.partial(map, _coconut_minus))(self.pts))
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)) and (_coconut_match_to[0:] == self.pts):
            _coconut_match_check = True
        if _coconut_match_check:
            return True
        else:
            return False
    @_coconut_tco
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        _coconut_match_check = False
        _coconut_match_to = other
        if (_coconut.isinstance(_coconut_match_to, vector)):
            other_pts = _coconut_match_to[0:]
            _coconut_match_check = True
        if _coconut_match_check:
            assert len(other_pts) == len(self.pts)
            raise _coconut_tail_call((sum), map(_coconut.operator.mul, self.pts, other_pts))  # dot product
        else:
            raise _coconut_tail_call((vector), *(_coconut.functools.partial(map, _coconut.functools.partial(_coconut.operator.mul, other)))(self.pts))  # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other
# New one-line functions necessary for finding the angle between vectors:
    @_coconut_tco
    def __truediv__(self, other):
        raise _coconut_tail_call((vector), *(_coconut.functools.partial(map, lambda x: x / other))(self.pts))
    def unit(self):
        return self / abs(self)
    @_coconut_tco
    def angle(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "self" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "other" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("self")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("other")
            if (_coconut.isinstance(_coconut_match_temp_1, vector)) and (not _coconut_match_to_kwargs):
                self = _coconut_match_temp_0
                other = _coconut_match_temp_1
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def angle(self, other is vector) = math.acos(self.unit() * other.unit())'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def angle(self, other is vector) = math.acos(self.unit() * other.unit())'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        raise _coconut_tail_call(math.acos, self.unit() * other.unit())

# Test cases:
assert (str)(vector(3, 4) / 1) == "vector(*pts=(3.0, 4.0))"
assert (str)(vector(2, 4) / 2) == "vector(*pts=(1.0, 2.0))"
assert (str)(vector(0, 1).unit()) == "vector(*pts=(0.0, 1.0))"
assert (str)(vector(5, 0).unit()) == "vector(*pts=(1.0, 0.0))"
assert vector(2, 0).angle(vector(3, 0)) == 0.0
assert vector(1, 0).angle(vector(0, 2)) == math.pi / 2
try:
    vector(1, 2).angle(5)
except MatchError:
    assert True
else:
    assert False
