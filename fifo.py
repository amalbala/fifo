class Fifo:
    """Class for code interview FIFO with fixed lenght known in advance, focus on speed

    All operation are O(1)
    """

    def __init__(self, size):
        """Constructor of the container to reserve memory upfront

        Args:
            size (int): Size of the vector, to simulate a circular vector
        """
        self.__size = size
        self.__push_pos = 0
        self.__pop_pos = 0
        self.__elements = 0
        self.__container = [None] * size

    def push(self, element):
        """Push an element at the end of the container

        Args:
            element (Any): Element to introduce if the container is not full
        """
        if self.__elements < self.__size:
            self.__container[self.__push_pos] = element
            self.__push_pos = (self.__push_pos + 1) % self.__size
            self.__elements += 1

    def pop(self):
        """Pop an element from the container

        Returns:
            Any: Element to remove or None if the container is empty
        """
        if self.isEmpty():
            return None

        self.__elements -= 1
        current_pop_pos = self.__pop_pos
        self.__pop_pos = (self.__pop_pos + 1) % self.__size
        return self.__container[current_pop_pos]

    def isEmpty(self):
        """Test empty

        Returns:
            bool: If the container is empty or not.
        """
        return self.__elements == 0
