class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        pass
        '''1 9 4 6 7
        start from last and for all of them ( bruteforce)
        go to left until you find someone bigger than you
        if you dont return the original if you do swap it
        optimal 
        
        prepare an array that holds the maximum value so far 
        [(3 ,0) , (3 , 0) , (3 , 0) ]
        ex, (1 , 0) (1 , 1) 5 , 2
        1 9 9 9 9 
        
        iterate from last to front and if cur is < the possible max to left we swap and return 
        
        
        '''

        for left in range(len(arr) - 2 ,-1, -1):
            if arr[left] > arr[left + 1]:
                maxi = left + 1
                
                for right in range(left + 1 , len(arr)):
                    if arr[left] > arr[right] > arr[maxi]:
                        maxi = right
                arr[left] , arr[maxi] = arr[maxi] , arr[left]
                break
        return arr
         # 9 > 7 > 4