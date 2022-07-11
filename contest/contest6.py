# 6 5
# 7 6 8 9 10 5

# people , height = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# tot = 0
# for num in arr:
#     if num > height: tot += 2
#     else: tot += 1
# print(tot)
# import sys


# length = int(input())

# sequence = list(map(int, input().split()))

# maxi = -sys.maxsize
# prev = -1
# cur_len = 0
# for num in sequence:
#     if num > prev:
#         cur_len += 1
#         maxi = max(maxi , cur_len)
#     else:
#         maxi = max(maxi , cur_len)
#         cur_len = 1
#     prev = num
# print(maxi)
# stairs_len = int(input())
# stairs = list(map(int, input().split()))

# boxes = int(input())

# for box in range(boxes):
#     width , height = list(map(int, input().split()))

#     print(max(stairs[0] , stairs[width - 1]))

#     stairs[0] = max(stairs[0], stairs[width - 1]) + height

# 10 10
# 1 4
# 6 8
# 2 5
# 3 7
# 9 4
# 5 6
# 3 4
# 8 10
# 8 9
# 1 10

from collections import defaultdict
from heapq import *

graph = defaultdict(list)

nodes , edges = list(map(int, input().split()))

for con in range(edges):
    par , child = list(map(int, input().split()))
    heappush(graph[par],child)
    heappush(graph[child] , par)


path = []

visited = set()
def dfs(node):
    visited.add(node)
    if not graph[node]: return
    path.append(node)
   
    while graph[node]:
        child = heappop(graph[node])
        if child not in visited:
            dfs(child)

dfs(1)
for p in path:
    print(p, end = ' ')
