class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
            c a b
          0 0 0 0
        a 0 0 1 1
        b 0 0 1 2
        a 0 0 1 2
        c 0 1 1 2
        '''
                  # a  b  a  c
#               [0, 0, 0, 0, 0]
#             c [0, 0, 0, 0, 1]
#             a [0, 1, 1, 1, 1]
#             b [0, 1, 2, 2, 2]
            
#             bac
        
        n,m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for s1 in range(1, n + 1):
            for s2 in range(1, m + 1):
                if str1[s1 - 1] == str2[s2 - 1]:
                    dp[s1][s2] = dp[s1 - 1][s2 - 1] + 1
                else:
                    dp[s1][s2] = max(dp[s1][s2 - 1] ,dp[s1 - 1][s2] )
        # for  i in range(n + 1): print(dp[i])
        queue = deque([])
        t1 = n
        t2 = m
        while t1 > 0 and t2 > 0:
            if str1[t1 - 1] == str2[t2 - 1]:
                queue.appendleft(str1[t1- 1])
                t1, t2 = t1 - 1, t2 - 1
            else:
                if dp[t1 - 1][t2] > dp[t1][t2 - 1]:
                    queue.appendleft(str1[t1 - 1])
                    t1 = t1 - 1
                else:
                    queue.appendleft(str2[t2 - 1])
                    t2 = t2 - 1
        
        ans = str1[:t1] + "".join(queue) if t1 else str2[:t2] + "".join(queue) 
        return ans
                        