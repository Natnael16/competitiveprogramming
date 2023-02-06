class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        cur_x , cur_y = point
        count = 0
        points = self.points
        for new_x, new_y in points:
            if (cur_x, cur_y) != (new_x, new_y) and abs(cur_y - new_y) == abs(cur_x - new_x): # not same and diagonal 
                point_one, point_two = (cur_x, new_y), (new_x,cur_y)
                count += (self.points.get(point_one,0) * self.points.get(point_two,0) * self.points.get((new_x, new_y), 0)) # permutation

        return count





        
        




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)