# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 00:01:20 2019
@author: Sushant Kadam
"""

"""
Implement Hash function with Linear Chaining (Not Linear Probing, using list)
"""

# 1 Create Hash
class Hashing:
    
    # To ensure minimum size
    minHashSize = 11
    
    # Initialize hash with minimum size
    def __init__(self, size=None):
        self.size = size or self.minHashSize
        # Used list to simplify the code
        self.hashTable = [[] for _ in range(self.size)]
     
    # Get the whole bucket
    def __getitem__(self, key):
    	return self.get(key)
    
    # Get the bucket for the key
    def get(self, key):
        return self.hashTable[self.hashFunction(key)]
    
    # Make insertion easy
    def __setitem__(self, key, value):
    	return self.put(key, value)
    
    # Simplest hash function using modulus
    def hashFunction(self, key):
        return key % self.size
    
    # 2
    # Put element in the hastable, if the key-value pair does not exists
    # Prints error if the data is already present
    def put(self, key, value):
        # get the hash index
        hashIndex = self.hashFunction(key)
        # boolean to check if the data is already present
        present = False
        # get the bucket where the data needs to be put
        bucket = self.hashTable[hashIndex]
        newTuple = (key, value)
        
        # Check in the bucket if the key value pair is present
        for bucketIndex, kvTuple in enumerate(bucket):
            if newTuple == kvTuple:
                present = True 
                break
            
        # Only add the key value in to the bucket if it does not exist
        if present:
            print(newTuple, "Key-value already present")
        else:
            bucket.append(newTuple)
    
    
    # Find if the Key value pair exists or not
    # Returns true if the pair exists or False if not
    def find(self, key, value):
        hashIndex = self.hashFunction(key)
        bucket = self.hashTable[hashIndex]
        # Check in bucket if the key-value exists
        for bucketIndex, kvTuple in enumerate(bucket):
            if kvTuple == (key, value):
                return True
        return False

    def resize():
        # Do something
        return None

# 3 Create a Hastable
h = Hashing()
#print(h.hashTable)
#print(h.get(3))
h.put(1, "one")
h.put(2, "two")
h.put(3, "three")
h.put(4, "four")
h.put(3, "three") # Duplicates
h.put(1, "one") # Duplicates

h[1] = "one"
h[1] = "two"
h[1] = "three"
h[1] = "four"
h[1] = "five"
h[1] = "six"
h[1] = "seven"
h[1] = "eight"
h[1] = "nine"
h[1] = "ten"

#print(h.find(1, "one"))
# 4 Print the table
print("Hashtable is:")
for i in range(h.size):
    print(h.hashTable[i])
    
"""
The time complexity to put the element into the hash would be O(1). As we
are just appending in the end of a list.

But retrieval time woulf be affected. The time complexity will be O(k), where
k is the size of the bucket.

We can reduce the value of k by resizing and rehasing. This would require
the time complexity of O(n + 1), to rehash and add new element.

"""
