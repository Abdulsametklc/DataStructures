class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):

        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return True

        tempNode = self.root

        while True:
            if newNode.value == tempNode.value:
                return False

            if newNode.value > tempNode.value:
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = newNode.right

            else:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = newNode.left

    def contains(self, value):
        tempNode = self.root
        while tempNode:
            if value < tempNode:
                tempNode = tempNode.left
            elif value > tempNode:
                tempNode = tempNode.right
            else:
                return True
        return False

    def minOfNode(selfsel, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def maxOfNode(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode

    def BFS(self): # --> Breadth First Search - BFS
        currentNode = self.root
        myQueue = []
        values = []
        myQueue.append(currentNode)

        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.value)
            if currentNode.left is not None:
                myQueue.append(currentNode.left)
            if currentNode.right is not None:
                myQueue.append(currentNode.right)
        return values

myTree = BinarySearchTree()