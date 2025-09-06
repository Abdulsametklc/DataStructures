"""
Queue()
enqueue(element)
dequeue()
size()
isEmpty()
"""

class Queue:

    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def enqueue(self, element):
        self.elements.insert(0, element)

    def dequeue(self):
        return self.elements.pop()

myQueue = Queue()