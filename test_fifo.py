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


def test_many_imputs():
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
