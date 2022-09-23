class Solution:
    def concatenatedBinary(self, n: int) -> int:
        con = []
        for i in range(1,n+1):
            con.append(bin(i).split("b")[1])
        binary  = "".join(con)
        return int(binary,base=2)%(10**9 + 7)
    