class Solution:
    def answerValid(self,min_power , cities , radius, k):
        left = 0 
        r = 2*radius 
        window_sum = sum(cities[left:r])
        
        for right in range(r, len(cities)):
        
            window_sum += cities[right]
            
            additional = min_power - window_sum
            if additional > k:
                return False
            elif additional > 0:
                k -= additional
                cities[right] += additional
                window_sum += additional
            
            window_sum -= cities[left]
            left += 1
        return True


    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        low , high = 0 , sum(stations) + k
        stations = [0] * r + stations + [0] * r
        best = low
        while low <= high:
            mid = (low + high)//2
            valid = self.answerValid(mid,stations[:],r, k)
            if valid:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
            
        return best

