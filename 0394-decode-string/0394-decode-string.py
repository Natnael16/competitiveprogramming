class Solution:
    def decodeString(self,s: str) -> str:
       
        result = ""
        start = 0
        while start < len(s):
            if s[start].isdigit():
                num = ""
                while s[start].isdigit():
                    num += s[start]
                    start += 1
                openings = 0
                num = int(num)
                next_call = ""
                start += 1
                while start < len(s):
                    if s[start] == "[":
                        openings += 1
                    elif s[start] == "]" and openings:
                        openings -= 1
                    elif s[start] == "]":
                        start += 1
                        break
                    next_call += s[start]
                    start += 1
                result += num * self.decodeString(next_call)
            else:
                result += s[start]
                start += 1
        return result