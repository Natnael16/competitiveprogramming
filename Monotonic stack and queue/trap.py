class Solution:

    def trap(self, height: List[int]) -> int:
        monoStack = []
        wanted = []
        for i in range(len(height)):
            if len(monoStack) == 0:
                monoStack.append((height[i], i))
            elif monoStack and monoStack[-1][0] > height[i]:
                monoStack.append((height[i], i))
            else:
                count = 0
                while monoStack and monoStack[-1][0] < height[i]:
                    count += 1
                    last = monoStack.pop()[1]

                if monoStack:
                    leftMost = monoStack[-1][1]
                    wanted.append((leftMost, i, sum(height[leftMost + 1:i])))
                elif count > 1:
                    leftMost = last
                    wanted.append((leftMost, i, sum(height[leftMost + 1:i])))
                monoStack.append((height[i], i))

        j = len(wanted) - 1
        while j > 0:
            while j > 0 and wanted[j][0] <= wanted[
                    j - 1][0] and wanted[j][1] >= wanted[j - 1][1]:
                wanted[j - 1], wanted[j] = wanted[j], 0
                j -= 1
            j -= 1
        final = 0
        for i in wanted:
            if i == 0:
                continue
            final += (min(height[i[1]], height[i[0]]) *
                      (i[1] - i[0] - 1)) - i[2]
        return final


# can make it more fast by using prefix sum rather than calling sum function in eatch iteration