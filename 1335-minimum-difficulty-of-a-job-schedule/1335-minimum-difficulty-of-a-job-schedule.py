class Solution:
    def minDifficulty(self, job_difficulty: List[int], d: int) -> int:
#         [6,5,2,8,6,6]
#            |
#         consider as a day 
#         or consider as part of a day(hava to track maximum)
        n = len(job_difficulty)
        # def dp(ind,max_difficulty,days_left):
        #     if days_left == 0:
        #         return inf
        #     # if ind >= n:
        #     #     return inf
        #     if ind  == n - 1:
        #         return max_difficulty
        #     return min(max_difficulty + dp(ind + 1,job_difficulty[ind + 1], days_left - 1),\
        #                dp(ind + 1,max(job_difficulty[ind],max_difficulty),days_left)
        #               )
        # dp_res = dp(0,job_difficulty[0],d)
        # if dp_res == inf: return -1
        # return dp_res
        @lru_cache(None)
        def dp(i, cur_max, remain):
            if remain == 0:
                return float('inf')
            if len(job_difficulty) - i < remain:
                return float('inf')
            if i == n - 1:
                return cur_max
            cur_job = job_difficulty[i+1]
            include = dp(i+1, max(cur_max, cur_job), remain)
            not_include = cur_max + dp(i+1, cur_job, remain-1)
            return min(include, not_include)

        result = dp(0, job_difficulty[0], d)
        return -1 if result == float('inf') else result
        