class Solution:
    def findMinArrowShots(self, points) -> int:
        points = sorted(points)
       
        x , y = points[0]
        count = 1
        for ind in range(1 , len(points)):
            if points[ind][0] <= y :
                x = max(x , points[ind][0])
                y = min(y , points[ind][1])
            else:
                x , y = points[ind]
                count += 1
        return count