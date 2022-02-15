class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        count = 0
        for i in nums:
            if i == 0:
                count += 1
                continue
            prod *= i
        if count == 0:
            for i in nums:
                result.append(prod // i)
        elif count == 1:
            for i in nums:
                if i == 0:
                    result.append(prod)
                else:
                    result.append(0)
        elif count > 1:
            return [0] * len(nums)
        return result