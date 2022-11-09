class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        n = len(s)
        def permutation(index, path):
            nonlocal answer
            if index >= n:
                answer.append(path)
                return 
            
            if s[index].isdigit():
                permutation(index + 1, path + s[index])
            else:
                islower = s[index].islower()
                permutation(index + 1,path + s[index])
                permutation(index + 1, path + s[index].upper() if islower else  path + s[index].lower())
        permutation(0,"")
        return answer
                
                
            
                
            