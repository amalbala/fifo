class Fifo:
    def __init__(self, size):
        self.__size = size
        self.__push_pos = 0
        self.__pop_pos = 0
        self.__elements = 0
        self.__container = [None] * size

    def push(self, element):
        if self.__elements < self.__size:
            self.__container[self.__push_pos] = element
            self.__push_pos = (self.__push_pos + 1) % self.__size
            self.__elements += 1

    def pop(self):
        if self.isEmpty():
            return None

        self.__elements -= 1
        current_pop_pos = self.__pop_pos
        self.__pop_pos = (self.__pop_pos + 1) % self.__size
        return self.__container[current_pop_pos]

    def isEmpty(self):
        return self.__elements == 0
