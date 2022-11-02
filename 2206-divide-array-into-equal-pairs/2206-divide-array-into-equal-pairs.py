class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        xor = 0
        nums.sort()
        for num in range(0, len(nums) ,2 ):
            if nums[num] ^ nums[num + 1]:
                return False
        return True