# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:38:41 2019
@author: Sushant Kadam
"""

"""
Binary Tree - find all the elements in range A to B(Unsorted)
"""
#1 Code for creating Queues
# We would be using this to traverse through the tree
class Queue:
    
    #Constructor
    def __init__(self):
        # We use python list and its functions to reduce coding
        self.q = []
    
    # Function takes in data to be inserted into the Queue
    # Enqueue using the list apeend function
    def enQ(self, data):
        self.q.append(data)
    
    # Function removes the first item in the Queue,
    # returns None when list is empty
    # Dequeue using the list functions
    def deQ(self):
        # check of emptiness
        if self.q:
            # Take the first element of the list
            data = self.q[0]
            # Remove it from the list (first occurence)
            self.q.remove(data)
            # Return the data
            return data
        else:
            # When Empty
            return None
       
    #empty
    # Check if the queue is empty
    # Returns TRUE if the list is empty
    def isEmpty(self):
        if not self.q:
            return True
        return False

#2 Create Binary Tree
class BinaryTree:
    
    #Initialize
	def __init__(self, data):
		self.data = data  # root node
		self.left = None  # left child
		self.right = None  # right child
	
    # Insert to the left of the root
	def insertLeft(self, newNode):
        # Add immediately to left
		if self.left == None:
			self.left = BinaryTree(newNode)
		else: # add to the left and move the existing leaf down
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp
            
    # Insert to the right of the root
	def insertRight(self, newNode):
        # Add immediately to the right
		if self.right == None:
			self.right = BinaryTree(newNode)
		else: # else add to the right and move the existing leaf down
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp
            
#3 Do level order traversal 
#Check for data whether it is greater(or equal) than A or less(or equal) than B
# Returns a list containing elements in the range (unsorted)
def rangelevelOrder(root, A, B):
    
    # Return if the tree is empty
    if root is None: 
        return None
    # Use the Queue to traverse through the tree
    q = Queue()
    # the result in range A and B
    result = []
    # Add the root node
    q.enQ(root)
    # Traverse through tree using Queue
    while(not q.isEmpty()):
        
        # get the element to compare data
        temp = q.deQ()
        # Compare the data if its in the given range
        if(temp.data >= A and temp.data <= B):
            # add the data if its in the range
            result.append(temp.data)
        
        # We add the elements to the queue
        # untill all the elements are traversed
        if temp.left:
            q.enQ(temp.left)
        if temp.right: 
            q.enQ(temp.right)
    # the list containing element in the range A and B
    return result
        
#5 Create a tree object
root = BinaryTree(11)
root.insertLeft(1)
root.insertLeft(10)
root.insertLeft(100)
root.insertRight(5)
root.insertRight(15)
root.insertRight(35)
root.insertRight(20)
root.insertRight(22)
root.insertRight(18)
root.insertRight(15)
root.insertRight(25)

# the list will be empty if the A and B are out of range
# [11, 10, 15, 18, 22, 20, 15]
print(rangelevelOrder(root, 10, 22))

"""
The time complexity for finding elements in binary tree would be the element
O(n). 

The space complexity would be O(n + k) where n is for storing values in Queue
and k are the element in the range
"""