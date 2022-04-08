class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # inbound = lambda ind: 0<= ind < len(flowerbed)
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1
            n -= 1
        if len(flowerbed) > 1 and not flowerbed[0] and not flowerbed[1]:
            flowerbed[0] = 1
            n -= 1
        if len(flowerbed) > 1 and not flowerbed[-1] and not flowerbed[-2]:
            flowerbed[-1] = 1
            n -= 1

        inbound = lambda ind: 0 <= ind < len(flowerbed)
        for i in range(len(flowerbed)):
            back, forward = i - 1, i + 1
            if flowerbed[i]:
                continue
            if (inbound(back) and flowerbed[back]
                    == 0) and (inbound(forward) and flowerbed[forward] == 0):
                n -= 1
                flowerbed[i] = 1
        if n <= 0:
            return True