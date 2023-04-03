# Binary search anyone 🤔 🤭
def bin_search(list_a, item1):
    first = 0
    last = len(list_a) - 1
    
    while first <= last:
    mid_point = (first + last) // 2 # i.e., the first letter index + the last letter index then divide by two to get an absolute value not floats
    if list_a[mid_point]  == item1:
        return True # if the mid_point is the item1 that we are searching in the sorted list, the function return True
    else:
        if item1 < list_a[mid_point]:
            last = mid_point - 1 # if the item1 is not the mid-point index, then proceed and search the left half of the list from the mid-point
        else:
            first = mid_point + 1
    return False # if the above fails to yield anything as item1 in question, the search goes on in the right half of the midpoint in the list
    
    
def bin_search_recurs(list_a, first, last, item1):
    if len(list_a) == 0:
        return False
    else:
        mid_point = (first + last ) // 2 # start by finding the midpoint by adding the last index and the first index and divide that by two to get an absolute value Not a float
        if list_a[mid_point] == item1:
            return True # should the mid-point of the above be equal to the item1 in question then return True
        else:
            if item1 < list_a[mid_point]:
                last = mid_point - 1 # If not not found, the code searches for item one in the left half of the list from the mid-point.
                return bin_search_recurs(list_a, first, last, item1)
            else:
                first = mid_point + 1 # if the above fails to give an off item1, the search is now done to right of the mid-point in the list
                return bin_search_recurs(list_a, first, last, item1)
                
                
if __name__ == '__main__':
    list_a = [1, 4, 7, 10, 14, 19, 102, 2575, 10000] # List in question

    print("Binary Search:", bin_search(list_a, 4))
    print("Recursive Binary Search:", bin_search_recurs, 0, len(list_a), -1, 4))
            
            
            
            
            
            
            
            
            
    
