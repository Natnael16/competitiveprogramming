class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value , timestamp))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.timeMap[key]
        return self.bSearch(0,len(nums)- 1,timestamp,nums )
        
        
        
    def bSearch(self,left, right, target,arr):
        if not arr: return ""
        best = -1
        while left <= right:
            mid = left + (right - left)//2
            
            if arr[mid][1] > target:
                right = mid - 1
            elif arr[mid][1] < target:
                best = mid
                left = mid + 1
            else:
                best = mid
                
                return arr[mid][0]
        return arr[best][0] if best!= -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)