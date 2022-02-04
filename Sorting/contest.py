def closestNumbers(arr):
    print(arr)
    sortedArr = sorted(arr)
    out = []
    small = sortedArr[1] - sortedArr[0]
    for i in range(1,len(arr)):
        temp = sortedArr[i]-sortedArr[i-1]
        if temp <= small:
            small = temp
    
          
    for i in range(1,len(arr)):
        tempo = sortedArr[i]-sortedArr[i-1]
        if tempo == small:
            out.append(sortedArr[i-1])
            out.append(sortedArr[i])
            
    return out