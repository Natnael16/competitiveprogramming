class Solution:
    def maximumSwap(self, num: int) -> int:
        max_num = num
        num = list(str(num))

        for i in range(len(num)):
            for j in range(len(num)):
                if i != j:
                    num[i], num[j] = num[j],num[i]
                    int_rep = int("".join(num))
                    max_num = max(max_num, int_rep)
                    num[i], num[j] = num[j],num[i]
        return max_num
