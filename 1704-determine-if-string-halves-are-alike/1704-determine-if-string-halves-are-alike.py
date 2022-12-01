class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels =  ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        s1, s2 = s[:len(s)//2], s[len(s)//2:]
        count1, count2 = 0, 0
        for v in vowels:
            count1 += s1.count(v)
            count2 += s2.count(v)
        return count1 == count2