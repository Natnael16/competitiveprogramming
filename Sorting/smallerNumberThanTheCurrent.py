class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            output.append(count)
        return output