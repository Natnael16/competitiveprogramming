# 3
# 8 7
# 4 3 3 1 1 4 5 9
# 1
# 10
# 50
# 14
# 15
# 22
# 30
# 4 1
# 1 2 3 4
# 3
# 1 2
# 5
# 4
# 6
# import sys
from bisect import bisect, bisect_left


tc = int(input())

for _ in range(tc):
    prifix = []
    pair = list(map(int , input().split()))
    candies = sorted(map(int , input().split()), reverse=True)
    tot = 0
    for candy in candies:
        tot += candy
        prifix.append(tot)
    
    for _ in range(pair[1]):
        q = int(input())
        if q > prifix[-1]:
             print(-1)
             continue
        
        
        print(bisect_left(prifix , q , 0 , len(prifix) - 1) + 1)
        
