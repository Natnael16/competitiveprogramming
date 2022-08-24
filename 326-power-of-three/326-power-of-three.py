class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        total = 3
        def pow_three(total,num):
            if n == total:
                return True
            elif total > num:
                return False
            else:
                return pow_three(3*total,num)
        return pow_three(total,n)