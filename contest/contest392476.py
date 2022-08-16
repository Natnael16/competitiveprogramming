# tc = int(input())

# for _ in range(tc):
#     num = input()
#     count = 0
#     if int(num) % 2 == 0: 
#         print(0)
#     elif int(num[0]) %2 == 0: print(1)
#     else:
#         for i in num:
#             if int(i) % 2 == 0:
#                 print(2)
#                 count += 1
#                 break
#         if count == 0: print(-1)
            



# grid_size = int(input())
# queen = tuple(map(int , input().split()))
# king = tuple(map(int , input().split()))
# to_reach = tuple(map(int , input().split()))

# if to_reach[0] < queen[0] and king[0] < queen[0]:
#     if to_reach[1] < queen[1] and king[1] < queen[1]:
#         print("yes")
#     elif to_reach[1] > queen[1] and king[1] > queen[1]:
#         print("yes")
#     else:
#         print("no")
# elif to_reach[0] > queen[0] and king[0] > queen[0]:
#     if to_reach[1] < queen[1] and king[1] < queen[1]:
#         print("yes")
#     elif to_reach[1] > queen[1] and king[1] > queen[1]:
#         print("yes")
#     else:
#         print("no")
# else: 
#     print("no")

from collections import defaultdict
import sys
tc = int(input())
def dp(nums: str , tar, cache , tot , steps):
    
    if tot < tar or not nums: return sys.maxsize
    if tot == tar: return steps
    if nums in cache: return cache[nums]
    left = 0
    right = 0
    if nums[0] == '1': left += 1
    if nums[-1] == '1': right += 1
    cache[nums] = min(dp(nums.removeprefix(nums[0]), tar , cache ,tot - left ,  steps + 1)
    ,dp(nums.removesuffix(nums[-1]), tar , cache , tot - right, steps + 1))
    return cache[nums]

for _ in range(tc):
    length , target = tuple(map(int , input().split()))
    arr = input().split()
    initial = 0
    for i in arr:
        initial += int(i)
    str_arr = "".join(arr)
    res = dp(str_arr,target , defaultdict() , initial , 0 )
    if res == sys.maxsize: print(-1)
    else: print(res)

    




