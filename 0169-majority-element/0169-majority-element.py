class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        shift = 1
        for _ in range(32):
            count0 , count1 = 0, 0
            for num in nums:
                if shift & num:
                    count1 += 1
                else:
                    count0 += 1
            if count1 > count0:
                ans |= shift
            shift <<= 1
        return  ans - (2**32) if ans > 5*10**4 else ans
                