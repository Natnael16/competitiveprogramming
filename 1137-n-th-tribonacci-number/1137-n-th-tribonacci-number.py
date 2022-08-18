class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1: return n
        if n == 2 : return 1
        zero = 0
        one = 1
        two = 1
        for i in range(n-2):
            three = one + two + zero
            
            one, zero = zero , one
            one = two
            two = three
        return three
        