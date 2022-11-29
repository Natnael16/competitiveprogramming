class Solution:
    def countArrangement(self, n: int,index=1, path = set()) -> int:  
        if index > n:
            return 1
        count = 0
        for num in range(1,n + 1):
            if num not in path:
                if num % index == 0 or index % num == 0:
                    path.add(num)
                    count += self.countArrangement(n,index + 1,path)
                    path.remove(num)
        return count
        
    
         