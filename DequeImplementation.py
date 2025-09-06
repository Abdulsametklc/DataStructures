"""Deque()

addLeft()
addRight()

removeRight()
removeLeft()

isEmpty()
size()"""

class Deque:
    def __init__(self):
        self.elements = []

    def addLeft(self, element):
        self.elements.insert(0,element)

    def addRight(self, element):
        self.elements.append(element)

    def removeRight(self):
        self.elements.pop()

    def removeLeft(self):
        self.elements.pop(0)

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

myDeque = Deque()