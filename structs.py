class Stack:
    """
    A class to create an instance of a Stack data structure with methods of insertion and deletion, based
    on First In Last Out principle.
    """
    def __init__(self):
        self.stack = []

    def push(self, element):
        """Insert element at top of stack (end of list)"""
        return self.stack.append(element)

    def pop(self):
        """Remove element from top of stack (end of list)"""
        return self.stack[:-1]


class Queue:
    """
    A class to create an instance of a Queue data structure with methods of insertion and deletion, base on
    First In First Out principle.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        """Insert element at the back of the queue (start of list)"""
        return self.queue.insert(0, element)

    def dequeue(self):
        """Remove element from front of queue (end of list)"""
        return self.queue[:-1]

