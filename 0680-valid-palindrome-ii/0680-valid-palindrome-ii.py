class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left +=1 ; right -= 1
            else:
                oneWay = s[:]
                oneWay.pop(left)
                another = s[:]
                another.pop(right)
        
                return oneWay == oneWay[::-1] or another == another[::-1]
                
        return True
            