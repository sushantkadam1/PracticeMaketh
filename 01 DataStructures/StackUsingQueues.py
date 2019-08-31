# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:49:51 2019
@author: Sushant Kadam
"""

"""
Simulate a Stack using Two Queues
"""

#1 Code for creating Queues
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
    

#2 Code for stack
class Stack:
    
    #init
    # Create two queues 
    # Do not assume one for insertion and another for deletion
    def __init__(self):
        
        self.q1 = Queue() # Queue1
        self.q2 = Queue() # Queue2
    
    #Empty
    # Check for emptiness of the stack
    # Returns true if the stack is empty
    def isEmpty(self):
        
        return self.q1.isEmpty() and self.q2.isEmpty()
    
    # PUSH element to stack
    # Pushing operation is easy. We just push elements in whichever Queue is
    # is not empty
    def push(self, data):
        
        # Push data to q2
        if self.q1.isEmpty():
            self.q2.enQ(data)
        else:
            self.q1.enQ(data)
            
      
    # pop element from stack
    # Pop operation is difficult as we manipulate the lists based on which 
    # queue is empty
    # Returns data that is at the top of the Stack, None if empty
    def pop(self):
        
        # Check if both are empty at first
        if self.isEmpty():
            return None
        # Check if q1 is empty move all the data from q2 to q1, to get the top element
        elif self.q1.isEmpty():
            while not self.q2.isEmpty():
                # get element from the front of the queue FIFO
                top = self.q2.deQ()
                # if queue is empty, you have the last element aka top element
                if self.q2.isEmpty():
                    return top
                else:
                # put element into another list to simulate LIFO
                    self.q1.enQ(top)
                    
        else: # else move data from q2, to get the top element
            while not self.q1.isEmpty():
                # get the element from the front FIFO
                top = self.q1.deQ()
                # if queue is empty, you have top
                if self.q1.isEmpty():
                    return top
                else:
                # put element into another list to simulate LIFO
                    self.q2.enQ(top)
            
   
#3 Create Stack
stack = Stack()

#4 Push elements 1,2,3,4,5
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

#5 Print output Expected: 5,4,3,2,1
print(stack.pop(),
stack.pop(),
stack.pop(),
stack.pop(),
stack.pop())


"""

The time complexity for storing the data into above stack is still O(1).
But we have made the push operation complex, hence the time required from the
top of the queue is no longer O(1), but O(n) as we have to dequeue/enqueue
all the element to get the topmost element(LIFO) of the stack.

The space complexity does not change much as the number of the elements 
stored always remain the same O(1)

"""
