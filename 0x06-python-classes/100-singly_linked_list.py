#!/usr/bin/python3
"""
This module provides classes that defines a linked list.
"""


class Node:
    """Node that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initializing"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """initializing"""
        self.head = None

    def sorted_insert(self, value):
        """
        sorted_insert -inserts the new node
        into the linkedlist in such a way that
        the sorted order is maintained.
        """

        new_node = Node(value)
        if not self.head or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
