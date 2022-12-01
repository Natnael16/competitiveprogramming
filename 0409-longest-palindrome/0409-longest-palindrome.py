class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        count = 0
        
        odds = 0
        for k ,c in counter.items():
            if not c % 2:
                count += c
            else:
                count += c - 1
                odds += 1
        if odds:
            return count + 1
        return count