"""
OWNERSHIP: This program (Lab 5) was written ENTIRELY
by Alexander Pickering on Tuesday, Feb 14, 2023.

PURPOSE: The goal of this lab is to practice the implementation and application of queues.
"""

import numpy as np


class CircularQueueArray:
    """
    This class represents a basic circular queue data structure.
    """
    def __init__(self, capacity: int):
        """
        Initializes the data structure.
        :param capacity:
        """
        self.capacity = capacity
        self.size = 0
        self.contents = np.empty(capacity, dtype='U100')
        self.front = 0
        self.back = 0

    def __len__(self):
        """
        :return: the length of the circular queue.
        """
        return int(self.size)

    def __str__(self):
        """
        :return: A string representation of the circular queue.
        """
        _res = ", ".join([i for i in " ".join([j for j in self.contents]).split()]).strip()
        return "<< " + _res + " >>"

    def __getitem__(self, item):
        """
        :param item: the item index
        :return: the item at a given index in the circular queue.
        """
        return self.contents[item]

    def is_full(self):
        """
        :return: True if the queue is populated, False if not.
        """
        return self.capacity == self.size

    def is_empty(self):
        """
        :return: True if the queue is empty, False if not.
        """
        return self.size == 0

    def enqueue(self, value: str):
        """
        Enqueues a value to the beginning of the queue.
        :param value:
        :return: Nothing
        """
        if self.is_full():
            raise IndexError("Queue is full")
        self.contents[self.back] = value
        self.back = (self.back + 1) % self.capacity
        self.size += 1

    def dequeue(self) -> str:
        """
        Dequeues the front of the queue.
        :return: The list of value dequeued.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        _value = self.contents[self.front]
        self.front = (self.front + 1) % self.capacity
        self.contents[self.front - 1] = ''
        self.size -= 1

        return _value


class HexadecimalCounter:
    """
    This class represents a hexadecimal counter.
    """
    def __init__(self, terms: int):
        """
        Initialize the counter.
        :param terms: How many terms to count in hex.
        """
        self.terms = terms
        self.pos0 = CircularQueueArray(16)
        self.pos1 = CircularQueueArray(16)
        self.pos2 = CircularQueueArray(16)

    def init_hex_arrays(self):
        """
        Initializes the three position arrays.
        :return: Nothing
        """
        _hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        for h in _hex:
            self.pos0.enqueue(h)
            self.pos1.enqueue(h)
            self.pos2.enqueue(h)

    def counter(self):
        """
        Prints the given amount of terms in hexadecimal and returns the values as a list.
        :return: A list containing the printed terms.
        """
        _res = []

        self.init_hex_arrays()

        for x in range(len(self.pos0)):
            for y in range(len(self.pos1)):
                for z in range(len(self.pos2)):
                    _res.append(self.pos0[x] + self.pos1[y] + self.pos2[z])

        print(" ".join([i for i in _res[:self.terms]]))
        return _res[:self.terms]


counter = HexadecimalCounter(25)
counter.counter()
