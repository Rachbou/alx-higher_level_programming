#!/usr/bin/python3
# 6-square.py
# Rachid BOULMANI
"""Define a class SinglyLinkedList and a class Node."""


class Node:
    """class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property to retrieve data"""
        return (self.__data)

    @property
    def next_node(self):
        """property to retrieve next_node"""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """property setter def data(self, value): to set data
        with data must be an integer
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        """property setter def next_node(self, value): to set next_node
        with position must be a Node or None
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """Simple instantiation"""
        self.__head = None

    def sorted_insert(self, value):
        """Public instance method: def sorted_insert(self, value):
        that inserts a new Node into the correct sorted
        position in the list (increasing order)
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
