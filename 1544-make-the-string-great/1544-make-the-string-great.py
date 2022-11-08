class Solution:
    def makeGood(self, s: str) -> str:
        lowers = string.ascii_lowercase
        uppers = string.ascii_uppercase
        while True:
            initial_len = len(s)
            for i in range(len(lowers)):
                delete = lowers[i] + uppers[i]
                s = s.replace(delete,"")
                delete = uppers[i] + lowers[i]
                s = s.replace(delete,"")
            if initial_len == len(s):
                break
        return s