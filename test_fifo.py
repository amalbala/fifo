""" Test fifo.py
"""

from fifo import Fifo


def test_creator():
    fifo_obj = Fifo(3)

    assert (
        fifo_obj.elements == fifo_obj.pop_pos == fifo_obj.push_pos == 0
        and fifo_obj.size == 3
    ), "Failed. Initialization wrong"


def test_pop():
    fifo_obj = Fifo()
    fifo_obj.push(4)

    assert fifo_obj.elements == 1, "Failed, problem on pop "
