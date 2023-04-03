# Queue Data Structure
# This a common data structure especially when dealing with First-In-Fisrt-Out scenarios in computer science.


class Queue:

    def __init__(self): # initiate an empty list to store items in the list
        self.items = []
        
    def __rep__(self): # Return a string representation of the queue object # Simply put what does the queue look like
        return f'Queue object: data={self.items}'
        
    def empty(self): # Check whether the queue is empty or not because the rest of the code depends on queue having data
        return not self.items
        
    def inqueue(self, item): # Here, we take an item as a parameter and put (or adds) it to the end of the queue
        self.items.append(item)
        
    def outqueue(self): # remove and return the first item of the queue
        return self.items.pop(0)
        
    def size(self): # Return the number of items available in the queue
        return len(self.items)
        
    def peek(self): # show the first item in the queue without removing it
        return self.items[0]
        
if __name__ == '__main__': # Run the Queue class functionality
q = Queue() # create a new queue object
print(q.empty())
q.inqueue('First')
q.inqueue('Second') # add two items to it using the inqueue method
print(q) # Print the contents 
print(q.outqueue()) # remove the first item from the queue
print(q) # print the updated queue
print(q.size()) # return the size of the queue
print(q.peek()) # return the first item in the queue



























        
        
        
        
        
