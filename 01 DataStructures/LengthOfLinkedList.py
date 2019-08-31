# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:44:09 2019
@author: Sushant Kadam
"""

"""
In a linked list, find the length of the cycle (if any)
"""

# Node to Store the Actual Data and the Next Node
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for defining and performing auxilary operations 
# to a linked list
class LinkedList(object):
    
    # Constructor that initialise the head (empty until assigned)
    def __init__(self, head = None):
        
        self.head = head
    
    # Function to print the linked list
    def print_list(self):
        
        # Add the elements to a python list
        lList = []
        # Set head
        current = self.head
        while current:
            # Append the python list
            lList.append(current.data)
            current = current.next
        #display the python list
        print(lList) 
    
    # Function to find the length of a cycle in a linked list
    # Returns zero if no cycle is present or no elements present
    def getCycleLength(self):
        
        # Return 0 if the head is empty
        if self.head is None:
            return 0
        
        # Use Two pointer (slow and fast pointer)
        # One is slow aka Tortoise
        tort = self.head
        # Another is fast aka Rabbit
        # We know the head is not None so we set Rabbit one step ahead
        rbbt = self.head.next
        
        # We run the loop until either all elements are exhausted
        # or we find a loop and then stop when both tortoise and rabbit 
        # meet at the same node
        while tort and tort.next and rbbt and rbbt.next and rbbt.next.next:
            
            # Both rabbit and tortoise are at the same node 
            # and we have a cycle
            if tort == rbbt:
                
                # Now that we have a cycle increment the counter
                loopLength = 1
                # we move the tortoise
                tort = tort.next
                
                # move the tortoise until we come back to rabbit
                while tort != rbbt:
                    
                    tort = tort.next
                    loopLength += 1 # Increment the length
                
                # return the length of the cycle
                return loopLength
            
            # Tortoise goes one step, but the Rabbit moves two steps
            tort = tort.next
            rbbt = rbbt.next.next
        
        # return 0 if no cycle is present
        return 0

# Creating the nodes for the linked list
node1 = Node(1); node2 = Node(2); node3 = Node(3)
node4 = Node(4); node5 = Node(5); node6 = Node(6)
node7 = Node(7); node8 = Node(8); node9 = Node(9)
# Joining the linked list (without the loop)
node1.next=node2; node2.next=node3; node3.next=node4
node4.next=node5; node5.next=node6; node6.next=node7
node7.next=node8; node8.next=node9;

# Creating a linked list with node1 as the header
myll = LinkedList(node1)
# Display the linked list
myll.print_list()
# No loop exists at the begining which is 0
print("The length of the cycle is : ",myll.getCycleLength())

# Creating a loop with 5 lengths
node9.next = node5
# Displaying the calculated length which is 5
print("The length of the cycle is : ",myll.getCycleLength())

# Creating another loop now pointing to the start node
node9.next = node1
# Displaying the calculated length which is 9
print("The length of the cycle is : ",myll.getCycleLength())

# Creating another loop now pointing to the end node itself
node9.next = node9
# Displaying the calculated length which is 1
print("The length of the cycle is : ",myll.getCycleLength())


"""
The time complexity of finding the length of the loop will be
1. length of the loop divide by 2 to traverse (n/2)
2. length of the loop (m)

O(n/2 + n) ~~ O(n)

Space complexity O(constant number of extra variables used) ~~ O(1)

"""