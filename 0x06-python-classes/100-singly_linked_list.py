#!/usr/bin/python3

"""define a node of a singly linked list"""

class Node:

    """initialize"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
    """retrieve private instance attribute data"""

    @property
    def data(self):
        return (self.__data)

    """set the data field"""

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    """retrieve private instance attribute next_node"""

    @property
    def next_node(self):
        return self.__next_node

    """set next_node"""

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value

"""define singly linked list"""

class SinglyLinkedList:
    
    """initialize"""
    
    def __init__(self):
        self.__head = None

    """instance method sorted_insert"""

    def sorted_insert(self, value):

        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while(tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        lists = []
        tmp = self.__head
        while tmp is not None:
            lists.append(str(tmp.data))
            tmp = tmp.next_node
        return('\n'.join(lists))
