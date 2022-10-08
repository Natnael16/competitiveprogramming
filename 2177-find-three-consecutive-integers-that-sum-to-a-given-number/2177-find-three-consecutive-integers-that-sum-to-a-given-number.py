class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        #0 1 2 3 4  5  6   7
        #  0 3 6 9 12 15   18
        
        if num % 3  == 0:
            last_num = num // 3 + 1
            return [i for i in range(last_num - 2,last_num+1)]
        else:
            return []
        
        
        