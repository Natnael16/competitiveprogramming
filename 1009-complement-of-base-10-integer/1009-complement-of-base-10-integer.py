class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(bin(n ^ 2**32 -1).split('b')[1][-len(bin(n).split('b')[1]):],base=2)