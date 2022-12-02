class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a , 2)
        int_b = int(b , 2)
        carry = (int_a & int_b) << 1
        xor = (int_a ^ int_b)
        while carry != 0:
            carry, xor = (carry & xor) << 1, (xor ^ carry)
        return bin(xor).split("b")[1]
    
    