print("peiurhg")
def arthimeticSubArray(nums,l,r):
    out = []
    for i in range(len(l)):
        temp = nums[l[i]:r[i]]
        print(l[i],r[i])
        temp = temp.sort(reverse = True)
        print(temp)
        dif = temp[0]-temp[1]
        count = 0
        for i in range(len(temp)-1):
            if temp[i] - temp[i+1] != dif:
                count += 1
                print(count)
        if count != 0:
            out.append(False)
        else: 
            out.append(True)

    return out

print(arthimeticSubArray([4,6,5,9,3,7],[0,0,2],[2,3,5]))
