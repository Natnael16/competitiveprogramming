class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        total = 4
        def powOf4(total,num):
            if n == total:
                return True
            elif total > num:
                return False
            else:
                return powOf4(4*total,num)
        return powOf4(total,n)