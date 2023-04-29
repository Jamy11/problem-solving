class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert( self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value :
            if current_node.left_child == None:
                current_node.left_child = Node(value)
                current_node.left_child.parent = current_node
            else:
                self._insert( current_node.left_child, value )

        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
                current_node.right_child.parent = current_node
            else:
                self._insert( current_node.right_child, value )

        else:
            print('ALready Added')

    def find(self,value):
        if self.root != None:
            return self._find( value, self.root)
        else:
            return 
        
    def _find(self ,value, current_node):
        if current_node == None:
            return None
        
        if value == current_node.value:
            return current_node
        
        elif value < current_node.value:
            return self._find(value, current_node.left_child)
        
        elif value > current_node.value:
            return self._find(value, current_node.right_child)
    
    def deleteValue(self,value):
        return self._deleteNode(self.find(value))
    
    def _deleteNode(self, node):

        if node == None or self.find(node.value) == None:
            return 'Value does not exist on the Tree'
        
        def numberOfChild(n):
            numberOfChild = 0
            if n.left_child != None: numberOfChild += 1
            if n.right_child != None: numberOfChild += 1
            return numberOfChild
        
        def minimumValue(n):
            while n.left_child != None:
                n = n.left_child

            return n

        nodeChildCount = numberOfChild(node)

        nodeParent = node.parent

        if nodeChildCount == 0:

            if nodeParent != None:
                if nodeParent.left_child == node:
                    nodeParent.left_child = None
                else:
                    nodeParent.right_child = None
            else:
                self.root == None

        if nodeChildCount == 1:
            if node.left_child != None:
                child  = node.left_child
            else:
                child = node.right_child
            if nodeParent != None:
                if node.left_child == node:
                    nodeParent.left_child = child
                else:
                    nodeParent.right_child = child
            else:
                self.root = child
            child.parent = nodeParent

        if nodeChildCount == 2:

            miniumValueOFCurrentNode = minimumValue(node.right_child)

            node.value = miniumValueOFCurrentNode.value

            self._deleteNode(miniumValueOFCurrentNode)


    def print(self):
        if self.root == None:
            return "Tree is empty"
        
        else:
            self._print(self.root)

    def _print(self, current_node):
        if current_node != None:
            self._print(current_node.left_child)
            print(current_node.value)
            self._print(current_node.right_child)

    def height(self):
        if self.root == None:
            return 0
        return self._height(self.root, 0)
    
    def _height(self, current_node, current_value):
        if current_node == None:
            return current_value
        left_max = self._height(current_node.left_child, current_value+1)
        right_max = self._height(current_node.right_child, current_value+1)
        return max(left_max,right_max)
    
    def search(self, value):
        if self.root == None:
            return False
        return self._search(self.root, value)
    
    def _search(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True
        elif value< current_node.value:
            return self._search(current_node.left_child, value)
        else:
            return self._search(current_node.right_child, value)


def fillMyBst(tree, max_item = 10, max_int = 100):
    from random import randint

    for x in range(max_item):
        tree.insert(randint(0,max_int))
    return tree

my_bst = BST()
# fillMyBst(my_bst)
my_bst.insert(5)
my_bst.insert(4)
my_bst.insert(6)
my_bst.insert(10)
my_bst.insert(9)
my_bst.insert(11)
my_bst.print()
# my_bst.deleteValue(5)
my_bst.deleteValue(11) # wrong logic

print('new print')
my_bst.print()

# print('height',my_bst.height())
# print(my_bst.root.right_child.parent.__dict__)