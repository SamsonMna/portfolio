# Merge & sort

def sort_merge(list_a):
    print("Dividing ", list_a)
    
    if len(list_a) > 1:
        mid_point = len(list_a) // 2
        left = list_a[:mid_point]
        right = list_a[mid_point:] # Divides the list given into two section at the mid-point 
        
        sort_merge(left)
        sort_merge(right)# Then make two recursive calls sort_merge "The function above, one with the left half of the list and one with the right half of the list
        
        x = y = z = 0
                
        while x < len(left) and y < len(right): # we loop through the two sub-list to the left and to the right
            if left[x] <= right[y]:
                list_a[z] = left[x] # Compare the current indices of 'x' and 'y' of the elemet in the right sublist to the ones in the left sublist
                x += 1 # should the element in left be smaller or equal to the element in the in the right, the element is placed in the merged list at the index x
            else:
                list_a[z] = right[y]
                y += 1
            z += 1 # This increases the variable z to the point next position in the merged list
            
            while x < len(left):
                list_a[z] = left[x]
                x += 1
                z += 1 # check if the are elements remaining in the left that have not been merged. if any, those elements are placed in the merged list at index z, x and y and increased accordingly
                
    print("Merging ", list_a)

if __name__ =='__main__':
    list_a = [47, 9, 90, 30, 73, 21, 41, 67, 1]
    sort_merge(list_a)
    print(list_a)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
