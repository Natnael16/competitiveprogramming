class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 2**32 -1
        num = n ^ mask
        bitsUsed = len(bin(n).split('b')[1])
        trim = bin(num).split('b')[1][-bitsUsed:]
        return int(trim,base=2)