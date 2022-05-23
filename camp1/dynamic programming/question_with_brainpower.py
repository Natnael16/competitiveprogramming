@lru_cache(maxsize=None)
        def dp(cur_idx ):
            if cur_idx >= len(questions):
                return 0
            if cur_idx == len(questions) - 1:
                return questions[cur_idx][0]
            max_return = max(dp(cur_idx + 1) ,dp(cur_idx + questions[cur_idx][1] + 1) + questions[cur_idx][0])
            return max_return 
        return dp(0)
