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
