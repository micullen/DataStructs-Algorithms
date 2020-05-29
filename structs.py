from typing import Any, Dict, Optional, List

class Stack:
    """
    A class to create an instance of a Stack data structure with methods of insertion and deletion, based
    on First In Last Out principle.
    """
    def __init__(self):
        self.stack = []

    def push(self, element: Any) -> List:
        """Insert element at top of stack (end of list)"""
        return self.stack.append(element)

    def pop(self) -> List:
        """Remove element from top of stack (end of list)"""
        return self.stack.pop()

    def length(self) -> int:
        """Returns the length of the stack"""
        return len(self.stack)

    def empty(self) -> List:
        """Empties the stack"""
        self.stack = []
        return self.stack

    def top(self) -> Any:
        """Returns the top of the stack"""
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def get_stack(self) -> List:
        return self.stack





class Queue:
    """
    A class to create an instance of a Queue data structure with methods of insertion and deletion, based on
    First In First Out principle.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, element) -> List:
        """Insert element at the back of the queue (start of list)"""
        return self.queue.insert(0, element)

    def dequeue(self) -> List:
        """Remove element from front of queue (end of list)"""
        return self.queue.pop()

    def length(self) -> int:
        """Returns the length of the queue"""
        return len(self.queue)

    def empty(self) -> List:
        """Empties the queue"""
        self.queue = []
        return self.queue

    def front(self) -> Any:
        """Returns the value at front of the queue"""
        if len(self.queue) == 0:
            return None
        return self.queue[-1]

    def get_queue(self) -> List:
        """Returns whole queue"""
        return self.queue


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        if self.head is None:
            return None
        else:
            n = self.head
            nodes = []
            while n is not None:
                nodes.append(n.data)
                n = n.next
            return str(nodes)

    def insert_at_start(self, data: Any) -> None:
        """Creates new node, links the node to the current head, and replaces itself as new head"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: Any) -> None:
        """Creates new node, checks if head is empty, if so create head. If not, loops through nodes until find one with
        no next node."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def insert_after_item(self, x: Any, data: Any) -> None:
        """Inserts a node after a specific item, can be within the linked list."""
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next

        if n is None:
            print('List is empty')
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_before_item(self, x: Any, data: Any) -> None:
        """Inserts a node before a specific item, can be within the linked list"""
        n = self.head
        if n is None:
            print("It's empty")

        elif n.data == x:
            new_node = Node(data)
            new_node.next = n.next
            self.head = new_node

        else:
            while n is not None:
                if n.next.data == x:
                    break
                n = n.next

            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_at_index(self, index: int, data: Any) -> None:
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.next
            i = i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
