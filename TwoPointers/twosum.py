class Solution(object):
    def twoSum(self, numbers, target):
        i , j = 0 , len(numbers) - 1
        while i != j-1:
            if numbers[i]+ numbers[j] > target:
                j -= 1 
            elif numbers[i] + numbers[j] <target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                break
        return [i + 1,j+1]