class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return ""
        n = len(s)
        conc = s + "#" + s[::-1]
        kmp = [0] * (2*n)
        slow, fast = 0 , 1
        while fast < 2*n:
            if conc[fast] == conc[slow]:
                slow += 1
                kmp[fast] = slow
                fast += 1
            elif slow == 0:
                fast += 1
            else:
                slow = kmp[slow - 1]
    
        longest_palindromic_substring = kmp[-1] + 1
        to_add = n - longest_palindromic_substring 
        return s[::-1][:to_add] + s