# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:52:30 2019
@author: Sushant Kadam
"""

"""
Binary Search Tree - find all the elements in range A to B(sorted)
"""
# 1 Binary Search Tree
class BinarySearchTree:
    
    # Initialize
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    # Insert data to the tree
    def insert(self, data):
        self.insertNode(BinarySearchTree(data))
    
    # Insert Node recursively
    def insertNode(self, node):
        # Put the node in the begining if empty
        if self.data is None:
            self = node
        else:
            # Else insert recursively
            if self.data > node.data:
                if self.left == None:
                    self.left = node
                else:
                    self.left.insertNode(node)
            else:
                if self.right == None:
                    self.right = node
                else:
                    self.right.insertNode(node)

# 2 Inorder Traversal
def inorderRecursive(root):
    
	if not root:
		return
	inorderRecursive(root.left)
	print(root.data, end=" ")
	inorderRecursive(root.right)

# 3 Using Inorder traversal to print data
# Printing the data between range A and B (including A and B)
# Does not returns anything
def inorderRecursiveRange(root, A, B):
    
    if not root: 
    	return
    # Check at the child only if the data is in the range
    if root.data > A: 
    	inorderRecursiveRange(root.left, A, B)
    # Print the data
    if A <= root.data and root.data <= B: 
        print(root.data, end = " ")
    # Dont check the child if not in the range
    if root.data < B: 
    	inorderRecursiveRange(root.right, A, B)

# 4 Create Binary Search Tree
root = BinarySearchTree(11)
root.insert(10)
root.insert(2)
root.insert(32)
root.insert(4)
root.insert(12)
root.insert(18)
root.insert(22)
root.insert(29)
root.insert(31)
root.insert(15)
root.insert(25)
root.insert(28)

# 5 Print range
#inorderRecursive(root)
inorderRecursiveRange(root, 4, 25)
print()
inorderRecursiveRange(root, 12, 28)
"""
The time complexity to find the range is approximately equal to O(k)
Where k is range A to B.
It would be worst O(n), if the tree is skewed

The space complexity is O(1)
"""