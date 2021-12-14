def insertionSort2(n, arr):
    
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[j+1] < arr[j] :
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
        print(*arr)  
insertionSort2(8,[8, 7, 6, 5, 4, 3, 2, 1])