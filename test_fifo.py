""" Test fifo.py
"""

from fifo import Fifo


def test_creator():
    fifo_obj = Fifo(3)

    assert (
        fifo_obj.elements == fifo_obj.pop_pos == fifo_obj.push_pos == 0
        and fifo_obj.size == 3
    ), "Failed. Initialization wrong"


def test_push():
    fifo_obj = Fifo(3)
    fifo_obj.push(4)

    assert fifo_obj.elements == 1, "Failed, problem on push"


def test_push():
    fifo_obj = Fifo(3)
    fifo_obj.push(4)
    fifo_obj.push(5)
    element = fifo_obj.pop()

    assert element == 4, "Failed, problem on pop"


def test_is_empty():
    fifo_obj = Fifo(3)

    assert fifo_obj.isEmpty() == True, "Failed, empty"
