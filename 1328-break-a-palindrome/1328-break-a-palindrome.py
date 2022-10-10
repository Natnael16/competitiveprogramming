class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        i = 0
        while i < len(palindrome):
            if palindrome[i] == 'a':
                i += 1
            else:
                if len(palindrome) % 2 != 0 and i == len(palindrome) // 2:
                    i += 1
                    continue
                return palindrome[:i] + 'a' + palindrome[i + 1:]
                
            if i == len(palindrome):
                return palindrome[:i - 1] + 'b'
        return ""