class Fifo:
    def __init__(self, size):
        self._size = size
        self._push_pos = 0
        self._pop_pos = 0
        self._elements = 0
        self._container = [None] * size

    def push(self, element):
        if self._elements < self._size:
            self._container[self._push_pos] = element
            self._push_pos = (self._push_pos + 1) % self._size
            self._elements = self._elements + 1

    def pop(self):
        if self.isEmpty():
            return None

        self._elements = self._elements - 1
        current_pop_pos = self._pop_pos
        self._pop_pos = (self._pop_pos + 1) % self._size
        return self._container[current_pop_pos]

    def isEmpty(self):
        return self._elements == 0
