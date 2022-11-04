class Solution:
    def reverseVowels(self, s: str) -> str:
        seed = ""
        vowles = {"a","e","i", "o", "u","A","I","E", "O", "U"}
        for i in range(len(s) - 1, -1, -1):
            if s[i] in vowles:
                seed+=s[i]
        modify = list(s)
        j = 0
        for i in range(len(s)):
            if modify[i] in vowles:
                modify[i] = seed[j]
                j+=1
        return "".join(modify)