def largerCombination(x, y):
    return y+x > x+y
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strnums = [str(i) for i in nums]
        
        largest = ""
        for i in strnums:
            largest += i
        allreached = True
        while allreached:
            count = 0
            
            for i in range(len(strnums)-1):
                strout= ""
                if largerCombination(strnums[i],strnums[i+1]):
                    temp = strnums[i+1]
                    strnums[i+1] = strnums[i]
                    strnums[i] = temp
                    for i in strnums:
                        strout +=i
                    if int(largest) < int(strout):
                        largest = strout
                    count +=1 
            if count == 0:
                allreached = False
                break
        return str(int(largest))