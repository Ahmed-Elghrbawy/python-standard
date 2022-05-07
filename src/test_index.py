import pytest
import index

def test_uncovered_if():
    assert index.uncovered_if() == False

def test_fully_covered():
    assert index.fully_covered() == True


def test_some_func():
    assert index.some_function(3)

def test_some_func_less():
    assert not index.some_function(2)

