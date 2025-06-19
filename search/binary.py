# def search(array,num):
#     if len(array) == 0:
#         return None

#     mid=len(array)//2
#     if array[mid]== num:
#         return array[mid]   
#     if num>array[mid]:
#         return search(array[mid+1:],num)
#     else:
#         return search(array[:mid],num)

# Time complexity: O(n) because of slicing (each recursive call copies a sublist).

# Space complexity: O(n) due to the copied slices and recursion stack.

def search(array,num,low,high):
    '''
    Recursive binary search.
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    if len(array) == 0:
        return None
    if low > high:
        return None 
    mid=(low+high)//2
    if array[mid]==num:
        return array[mid]
    if num > array[mid]:
        return search(array,num,mid+1,high)
    else:
        return search(array,num,low,mid-1)
    
    '''

    #Iterative binary search.
    #Time Complexity: O(log n)
    #Space Complexity: O(1)
    while low <= high:
        mid = (low+high)//2
        if num == array[mid]:
            return num
        if num > array[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 3432, 4212]    
num=22
low=0
high=len(array)-1
sortedArr=sorted(array)
print(search(sortedArr,num,low,high))
