class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        bin_string = ""
        for num in range(1, n + 1):
            bin_string += bin(num).split("b")[1]
        return int(bin_string,base=2) % mod