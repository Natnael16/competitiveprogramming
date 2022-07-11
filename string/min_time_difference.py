class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            times.append(list(map(int , time.split(':'))))
        times.sort()
        # print(times)
        mini = sys.maxsize
        for i in range(1, len(times)):
            val = (times[i][0] - times[i - 1][0]) * 60  + (times[i][1] - times[i - 1][1])
            mini = min(mini , val)
        times[0][0] += 23
        times[0][1] += 60
        val = (times[0][0] - times[-1][0]) * 60  + (times[0][1] - times[-1][1])
        mini = min(mini , val)
        return mini