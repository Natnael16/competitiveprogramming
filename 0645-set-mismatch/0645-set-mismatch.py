class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        nums_len = len(nums)
        duplicate, missing = -1, -1
        for num in range(1,nums_len + 1):
            if counter[num] == 0:
                missing = num
            if counter[num] == 2:
                duplicate = num
        return [duplicate,missing]

        
        