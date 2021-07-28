def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))