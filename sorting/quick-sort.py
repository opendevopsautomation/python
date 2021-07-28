'''
In quicksort it will work similar to merge sort except in this we need to pick any pivot point.
1] Here we are assuming last element as pivot element.
2] we will use two pointers i & j. when jth element is smaller than pivot, increment the value of i & swap the ith element with jth elemennt.
3] repeat the 2nd step for j from start to end position.
4]to place the pivot at it's correct position, swap the (i+1)th element with the pivot.
5] return pivot element's position.
6] now repeat the 1 to 5 for left array & for the right array(recursively)
'''
def partition(arr,start,end):
    pivot=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1


def quicksort(arr,start,end):
    if (start < end):
        p=partition(arr,start,end)
        quicksort(arr,start,p-1)
        quicksort(arr,p+1,end)
    return arr


arr=[ 10, 7, 8, 9, 1, 5 ]
print(quicksort(arr,0,len(arr)-1))