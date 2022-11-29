class Solution:
    def countArrangement(self, n: int) -> int:
       
        def backtrack(index,path):
            
            if index > n:
                return 1
            count = 0
            for num in range(1,n + 1):
                if num not in path:
                    if num % index == 0 or index % num == 0:
                        path.add(num)
                        count += backtrack(index + 1, path)
                        path.remove(num)
            return count
        return backtrack(1,set())
         