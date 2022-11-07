class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for char in s:
            xor ^= ord(char)
        for char in t:
            xor ^= ord(char)
        return chr(xor)