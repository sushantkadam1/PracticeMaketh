# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:30:36 2019
@author: Sushant Kadam
"""

"""
A Doubly Queue using Doubly Linked List
"""

# 1 DLL Node
class Node:
    # Initialize
    def __init__(self, data=None, next=None, prev=None):
        self.data = data # Save the Data
        self.next = next # Save the next node
        self.prev = prev # Save the previous Node

# 1 Doubly Linked List   
class DoublyLinkedList:

    # Initialize
    def __init__(self):
        self.head = None
        self.tail = None
     
    # Insert the element at the data at the begining of DLL
    def insertAtBegining(self, data):
        # Create a new node for the data assign it to the head
        newNode = Node(data)
        if newNode == None:
            return "Memory Full"
        newNode.next = self.head
        # if the head is not empty make changes to the previous of the 
        # first node
        if self.head is not None:
            self.head.prev = newNode
            self.tail = newNode
        # Make the new node the first node
        self.head = newNode
        
    # Insert the element at the end of the DLL
    # Traverse from left to right and then end
    def insertAtEnd(self, data):
        # Create a new node with the data
        newNode = Node(data)
        if newNode == None:
            return "Memory Full"
        # Temp is needed to traverse the DLL from head
        temp = self.head
        # If head is empty attach the newNode to the head
        if self.head is None:
            self.head = newNode
            return
        # Traverse until the last node
        while temp.next:
            temp = temp.next
        # attach the new node to the end
        temp.next = newNode
        newNode.prev = temp
        self.tail = newNode
      
    # Quicker way to insert at the end using the self.tail
    def insertAtEndFast(self, data):
        # Create a new node with the data
        newNode = Node(data)
        if newNode == None:
            return "Memory Full"
        
        # Check if the tail is not null
        if self.tail is not None:
            # Add the new element directly to the end
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        # There's nothing in the DLL so we add the newnode to the end
        else:
            self.insertAtBegining(data)
    
    # Remove data from the begining of DLL
    def removeFromBegining(self):
        # Perform the activity only of head is not empty
        if self.head is not None:
            # Save the first node to be sent back after removal
            first = self.head
            if(self.tail==self.head):
                self.tail = self.head.next
            self.head = self.head.next
            return first
    
    # Remove data from the end of the DLL
    def removeFromEnd(self):
        # Check for emptiness
        if self.head is None:
            return
        # Use temp for DLL traversal
        temp = self.head
        #Go to the end
        while temp.next:
            temp = temp.next
        # Save the end node before we remove it from LL
        end = temp
        self.tail = temp.prev
        temp.prev.next = None
        return end
    
    # Remove the element from the end
    def removeFromEndFast(self):
        if self.tail is None:
            return
        # Save element to return after deletion
        end = self.tail
        # Change the tail to the one previous it
        self.tail = self.tail.prev
        # reset the tail to remove the end node
        self.tail.next = None
        return end
        
    # Print the doubly linked list from LEFT to RIGHT
    def __str__(self):
        # Go to the end of the DLL
        current = self.head
        result = []
        if current == None:
            return None
        while (current != None):
            result.append(current.data) 
            current = current.next
        return str(result)

# 2 Doubly Queue
class DoublyQueue:
    
    # Intialize the linked list
    def __init__(self):
        self.DLL = DoublyLinkedList()

    # Add element to the front of the Queue
    def addLeft(self, data):
        self.DLL.insertAtBegining(data)

    # Add element to the back of the Queue
    def addRight(self, data):
        self.DLL.insertAtEnd(data)
    
    # Add element at back faster 
    def addRightFast(self, data):
        self.DLL.insertAtEndFast(data)

    # Remove element from the front
    def removeLeft(self):
        return self.DLL.removeFromBegining()

    # Remove element from the back
    def removeRight(self):
        return self.DLL.removeFromEnd()
    
    # Remove element from the back faster
    def removeRightFast(self):
        return self.DLL.removeFromEndFast()
    
    # Print the Queue
    def __str__(self):
        return str(self.DLL)

# 3 Create Queue and perform actions
dq = DoublyQueue()
dq.addLeft(2)
dq.addLeft(1)
dq.addLeft(22)
dq.addLeft(11)
dq.addRight(3)
dq.addRight(4)
dq.addRight(33)
dq.addRight(44)

print(dq)

left = dq.removeLeft()
right = dq.removeRight()

print("Removed from left", left.data)
print("Removed from right", right.data)

#print(dq)

dq.addRightFast(100)
print(dq)
right = dq.removeRightFast()

print("Removed from right(fast)", right.data)
print(dq)

"""
Enqueue and Dequeue operations for the element at the head(left) will be O(1).

But the Enqueue and Dequeue at the end will be different. I used two ways to
1) Just use the head(in Doubly Linked List) to traverse. The time complexity
   was O(n), as all elements had to be traveresed.
2) Use the tail parameter to keep the track of the last element. Hence we
   reduce the time complexity of enqueue and dequeue to O(1)

I used the "Fast" functions to reduce this time complexity to O(1)

Space Complexity will remain O(1)
"""