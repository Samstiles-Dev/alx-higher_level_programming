#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """this is the Node class body."""

    def __init__(self, data, next_node=None):
        """Node function contructor.
        Args:
            data (int): This is the data of the new Node.
            next_node (Node): This is the next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """this sets and gets a Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """this gets and sets a  Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a node of a singly linked list"""

    def __init__(self):
        """Singly-LinkedList contructor."""
        self.__head = None

    def sorted_insert(self, value):
        """this Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            _tmp = self.__head
            while (_tmp.next_node is not None and
                    _tmp.next_node.data < value):
                _tmp = _tmp.next_node
            new.next_node = _tmp.next_node
            _tmp.next_node = new

    def __str__(self):
        """Defines the print() representation of a SinglyLinkedList."""
        values = []
        _tmp = self.__head
        while _tmp is not None:
            values.append(str(_tmp.data))
            _tmp = _tmp.next_node
        return ('\n'.join(values))
