class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        while ".L" in dominoes or "R." in dominoes:
            dominoes = dominoes.replace("R.L","sss").replace(".L", "LL").replace("R.","RR")
        return dominoes.replace("sss","R.L")
     
#         def LorR(rind,doms):
#             # print(rind)
    
#             for i in range(rind + 1, len(doms)):
#                 if doms[i] == "R":
#                     return (False , i)
#                 elif doms[i] == "L":
#                     return (True, i)
#             return (False , len(doms) - 1)
#         doms = list(dominoes) 
#         ind = 0
#         while ind < len(doms):
#             if doms[ind] == ".":
#                 ind += 1
#                 continue
#             elif doms[ind] == "L":
#                 k = ind - 1
#                 while k >= 0 and doms[k] == ".":
#                     doms[k] = "L"
#                     k -= 1
#                 ind += 1
#             elif doms[ind] == "R":
#                 if ind == len(doms) - 1: break
#                 # print(ind)
#                 res = LorR(ind, doms)
#                 # print(res)
#                 if res[0] == False:
#                     for i in range(ind, res[1] + 1):
#                         doms[i] = "R"
#                     ind = res[1]
#                 else:
#                     l , r = ind, res[1]
#                     length = r - l + 1
#                     if length % 2 == 1:
#                         mid = (r + l )// 2
#                         # print(l,r,mid)
#                         for back in range(mid - 1 , ind - 1, -1):
#                             doms[back] = "R"
#                         for forw in range(mid + 1 , res[1]):
#                             doms[forw] = "L"
#                         doms[mid] = "."
                       
#                     else:
#                         for forw in range(ind + 1, (res[1] - length // 2) + 1 ):
#                             doms[forw] = "R"
#                         back = res[1] - 1
#                         while doms[back] != "R":
#                             doms[back] = "L"
#                             back -= 1
#                     ind = res[1] + 1
                
            
#         return "".join(doms)    
        