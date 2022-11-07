class Solution:
    def maximum69Number (self, num: int) -> int:
        st = str(num)
        for idx, digit in enumerate(st):
            if digit == "6":
                return int(st[:idx] + "9" + st[idx + 1:])
        return num