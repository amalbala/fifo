""" Test fifo.py
"""

from fifo import Fifo


def test_creator():
    fifo_obj = Fifo(3)
    assert True, "Failed, initialization"


def test_push():
    fifo_obj = Fifo(3)
    fifo_obj.push(4)

    assert fifo_obj.isEmpty() == False, "Failed, problem on push"


def test_push():
    fifo_obj = Fifo(3)
    fifo_obj.push(4)
    fifo_obj.push(5)
    element = fifo_obj.pop()

    assert element == 4, "Failed, problem on pop"


def test_is_empty():
    fifo_obj = Fifo(3)

    assert fifo_obj.isEmpty() == True, "Failed, empty"


def test_many_pop_and_push():
    fifo_obj = Fifo(3)
    fifo_obj.push(1)
    fifo_obj.pop()
    fifo_obj.push(1)
    fifo_obj.pop()
    fifo_obj.push(1)
    fifo_obj.pop()
    fifo_obj.push(1)
    fifo_obj.pop()
    fifo_obj.push(1)
    fifo_obj.pop()
    fifo_obj.push(1)
    fifo_obj.pop()

    assert fifo_obj.isEmpty() == True, "Failed, several inputs"


def test_many_push():
    fifo_obj = Fifo(3)
    fifo_obj.push(1)
    fifo_obj.push(1)
    fifo_obj.push(1)
    fifo_obj.push(1)
    fifo_obj.push(1)
    fifo_obj.push(1)

    assert fifo_obj.isEmpty() == False, "Failed, several inputs"


def test_popWhenEmpty():
    fifo_obj = Fifo(3)
    fifo_obj.pop()

    assert fifo_obj.isEmpty() == True, "Failed, several inputs"
