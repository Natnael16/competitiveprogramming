class Solution:

    def isEnough(self, arr, time, target):
        total = 0
        for i in arr:
            total += (time // i)
        if total >= target:
            return True

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        left = 0
        right = totalTrips * time[0]
        best = totalTrips * time[0]
        while left <= right:
            mid = left + (right - left) // 2

            if self.isEnough(time, mid, totalTrips):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best