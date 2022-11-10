class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = "".join(map(str, digits))
        return list(str(int(number) + 1))