def heapify(arr,ln,i):
    largest=i
    left=2*i+1
    right=left+1
    if left < ln and arr[left] < arr[largest]:
        largest=left
    if right < ln and arr[right] < arr[largest]:
        largest=right
    if largest != i :
        arr[i],arr[largest]=arr[largest], arr[i]
        heapify(arr,ln,largest)
    return arr 
def heapsort(arr):
    ln=len(arr)
    y=ln-1
    x=(ln//2)-1
    print(x)
    while x >=0:
        heapify(arr,ln,x)
        x-=1
    while y >=0:
        arr[0],arr[y]=arr[y],arr[0]
        heapify(arr,y,0)
        y=y-1
    return arr
arr=[12, 11, 13, 5, 6, 7,1,0]
print(heapsort(arr))
