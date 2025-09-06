class Node: # Node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree: # Tree
    def __init__(self):
        self.root =None
    
    def insert(self, value): #Ekleme - binary search tree

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
                tempNode = tempNode.left
    
    def contains(self, value): # içeriyor mu?
        tempNode = self.root
        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False
    
    def minOfNode(self,currentNode): # minimum değer
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def maxOfNode(self, currentNode): # maksimum değer
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode

myTree = BinarySearchTree()