class Fifo:
    def __init__(self, size):
        self.size = size
        self.push_pos = 0
        self.pop_pos = 0
        self.elements = 0
        self.container = [None] * size

    def push(self, element):
        self.container[self.push_pos] = element
        self.push_pos = (self.push_pos + 1) % self.size
        self.elements = self.elements + 1

    def pop(self):
        self.elements = self.elements - 1
        current_pop_pos = self.pop_pos
        self.pop_pos = self.pop_pos + 1
        return self.container[current_pop_pos]
