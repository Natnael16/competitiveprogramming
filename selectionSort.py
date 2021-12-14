def selectionSort(n,arr):
    for i in range(n-1):
        small = arr[i]
        index = i
        for j in range(i+1,n):
            if small > arr[j]:
                small = arr[j]
                index = j
        arr[index] = arr[i] 
        arr[i] = small
    print(arr)

selectionSort(15,[2,9,8,7,10,20,1,0,56,3,80,5,2,1,0])