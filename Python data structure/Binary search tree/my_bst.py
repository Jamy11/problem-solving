class Node:
    def __init__(self, value , parent = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, currentNode, value):
        if currentNode == None:
            return None
        
        if value < currentNode.value:
            if currentNode.leftChild == None:
                currentNode.leftChild = Node(value, currentNode)
            else:
                self._insert( currentNode.leftChild, value )
        
        elif value > currentNode.value:
            if currentNode.rightChild == None:
                currentNode.rightChild = Node(value, currentNode)
            else:
                self._insert( currentNode.rightChild, value)
        
        else:
            print('Value is Already Added')
            return 'Value is Already Added'
    
    def height(self):
        if self.root == None:
            return 
        return self._height(self.root , 0)
    
    def _height(self, currentNode, depth):
        if currentNode == None:
            return depth
        leftMax = self._height(currentNode.leftChild, depth+1)
        rightMax = self._height(currentNode.rightChild, depth+1)
        return max(leftMax,rightMax)

    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, currentNode , value):
        if currentNode == None:
            return False
        if value == currentNode.value:
            return True
        elif value < currentNode.value:
            return self._search(currentNode.leftChild, value)
        else:
            return self._search(currentNode.rightChild, value)

    def find(self, value):
        return self._find(self.root, value)
    
    def _find(self, currentNode, value):
        if currentNode == None:
            return
        
        if value == currentNode.value:
            return currentNode
        elif value < currentNode.value:
            return self._find(currentNode.leftChild, value)
        else:
            return self._find(currentNode.rightChild, value)

    def deleteValue(self, value):
        if self.root == None:
            print('Tree is empty')
            return 'Tree is empty'
        self._deleteNode( self.find(value) )

    def _deleteNode( self, currentNode ):
       
        if currentNode == None:
            return None
        
        def countChild(n):
            count = 0
            if n.leftChild != None: count +=1
            if n.rightChild != None: count +=1
            return count
        
        def minimumChildValue(n):
            while n.leftChild != None:
                n = n.leftChild
            return n
        
        childNumber = countChild(currentNode)
        parentNode = currentNode.parent

        if childNumber == 0:
            if parentNode != None:
                if parentNode.leftChild == currentNode:
                    parentNode.leftChild = None
                else:
                    parentNode.rightChild = None
            else:
                self.root = None

        if childNumber == 1:
            if currentNode.leftChild != None:
                child = currentNode.leftChild
            else:
                child = currentNode.rightChild
            if parentNode != None:
                if parentNode.leftChild == currentNode:
                    parentNode.leftChild = child
                else:
                    parentNode.rightChild = child
            else:
                self.root = child
        
        if childNumber == 2:
            minimumChildValue = minimumChildValue(currentNode.rightChild)
            currentNode.value = minimumChildValue.value
            self._deleteNode(minimumChildValue)




        

    def print(self):
        if self.root == None:
            print('Tree Empty')
            return 'Tree Empty'
        else:
            self._print(self.root)
    
    def _print(self, currentNode):
        if currentNode == None:
            return
        self._print(currentNode.leftChild)
        print(currentNode.value)
        self._print(currentNode.rightChild)

def fillMyBst(tree, maxValue = 10, maxRotation= 10):
    from random import randint

    for x in range(maxRotation):
        tree.insert( randint(0,maxValue) )
    
    return tree

myBST = BST()
# fillMyBst(myBST)
myBST.insert(5)
myBST.insert(4)
myBST.insert(6)
myBST.insert(10)
myBST.insert(9)
myBST.insert(11)
myBST.print()

# print('------------------------------- Height ------------')
# print(myBST.height())
myBST.deleteValue(10)
myBST.deleteValue(11)
print('------------------------------- New Print ------------')
myBST.print()