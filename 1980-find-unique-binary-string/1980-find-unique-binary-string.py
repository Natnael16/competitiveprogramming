class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
#         numsset = set(nums)
#         self.ans = "" # assuming you submit it in leetcode 
#         def backTrack(s,target_len):
#             if len(s) == target_len:
#                 if s not in numsset:
#                     self.ans = s
#                 return
                                                                    
#             backTrack(s+"0",target_len)
#             backTrack(s+"1",target_len)
            
#         backTrack("",len(nums))
#         return self.ans
        ints = set()
        for binary in nums:
            ints.add(int(binary,base=2))
        for num in range(0,2**len(nums)): #itertates maximum 16 times
            if num not in ints:
                return ("000000000000000" + str(bin(num)).split("b")[1])[-len(nums):]
            